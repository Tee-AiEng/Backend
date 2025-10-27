from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os

load_dotenv()


db_url = f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"



engine = create_engine(db_url)

engine = create_engine(db_url, connect_args = {"client_flag":CLIENT.MULTI_STATEMENTS})
session = sessionmaker(bind=engine)


db = session()


create_tables_query = text(""" 
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    );
CREATE TABLE IF NOT EXISTS course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    level VARCHAR(255) NOT NULL
    );
CREATE TABLE IF NOT EXISTS Enrollment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    courseid INT,
    FOREIGN KEY (userid) REFERENCES user(id),
    FOREIGN KEY (courseid) REFERENCES course(id)
    );                          
""")
# create_tables_course = text(""" CREATE TABLE IF NOT EXISTS course (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     level VARCHAR(255) NOT NULL
#     );
#     """)
# create_tables_enrollrmrnt= text("""
# CREATE TABLE IF NOT EXISTS Enrollment (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     userid INT,
#     courseid INT,
#     FOREIGN KEY (userid) REFERENCES user(id),
#     FOREIGN KEY (courseid) REFERENCES course(id)
#     );
#     """)
db.execute(create_tables_query)
print("Tables habe been created sucessfully")
# db.execute(create_tables_course)
# print("Tables habe been created sucessfully")
# db.execute(create_tables_enrollrmrnt)
# print("Tables habe been created sucessfully")