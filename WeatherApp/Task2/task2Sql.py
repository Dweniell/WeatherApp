
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, text

engine = create_engine("sqlite:///task2.db", echo=True)
metadata=MetaData()
statement= text("CREATE TABLE persons (ID VARCHAR(20) PRIMARY KEY,Status VARCHAR(10),First_Name VARCHAR(50),Last_Name VARCHAR(50),Email_Address VARCHAR(100),Locatie VARCHAR(50));")
statementu= text("CREATE TABLE Votes (ID INT PRIMARY KEY,voting_date DATETIME,chosen_person VARCHAR(20),voter INT,message VARCHAR(100),valid BIT,quality VARCHAR(20));")
# CREATE TABLE persons (
# ID VARCHAR(20) PRIMARY KEY,
# Status VARCHAR(10),
# First_Name VARCHAR(50),
# Last_Name VARCHAR(50),
# Email_Address VARCHAR(100),
# Locatie VARCHAR(50)
# );

with engine.connect() as con:
    # con.execute(statement)
    # con.execute(statement2)
    con.commit()