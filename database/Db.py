import mysql.connector
from mysql.connector import Error
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import *

Base = declarative_base()
engine = create_engine('mysql+pymysql://test:password@127.0.0.1/toDoDb')


# Connection to db from pure mysql to create database if not exists
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user='test',
                                       password='password')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS toDoDb')
    conn.close()
    Base.metadata.create_all(bind=engine)


# Check login and password in database then return instance
def getLogFromDb(usr, passwd):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter(User.username == usr and User.password == passwd).first()
    session.close()
    return user


def readData(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    tasks = []
    userTasks = session.query(Task).filter(Task.user_id == user.id).all()
    session.close()
    for t in userTasks:
        tasks.append([t.id, t.text, t.date, t.done, False])
    return tasks


def addTask(text, user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    newTask = Task()
    newTask.text = text
    newTask.user_id = user_id
    session.add(newTask)
    session.commit()
    session.close()


def addNewUser(username, password):
    Session = sessionmaker(bind=engine)
    session = Session()
    newUser = User()
    newUser.username = username
    newUser.password = password
    session.add(newUser)
    session.commit()
    session.close()


# User Table
class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True, )
    username = Column('username', String(20), unique=True, nullable=False)
    password = Column('password', String(20), unique=False, nullable=False)
    tasks = relationship("Task")


# Task table
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column('task', Text(), nullable=False)
    date = Column('date', DateTime, default=datetime.now)
    done = Column('done', Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
