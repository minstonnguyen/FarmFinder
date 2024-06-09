# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:47:59 2024

@author: minston
"""

from html.parser import HTMLParser
import requests
import pyodbc
import datetime


class DataObject:
    def __init__(self, server, databaseName, username, password):
        if (server is None or databaseName is None or username is None or password is None):
            raise Exception("One value is null")
        self.server = server
        self.database = databaseName
        self.username = username
        self.password = password

    def getServer(self):
        return self.server

    def getDatabase(self):
        return self.database

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


class ConvertTextFileToDBTable:
    def __init__(self, filename, dbConnectionInfo):
        self.filename = filename
        self.dbConnectionInfo = dbConnectionInfo

    def run(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.dbConnectionInfo.getServer()+';DATABASE=' +
                              self.dbConnectionInfo.getDatabase()+';UID='+self.dbConnectionInfo.getUsername()+';PWD=' + self.dbConnectionInfo.getPassword())
        cursor = cnxn.cursor()
        try:
            with open(self.filename, 'r') as file:
                scorecards = file.read().split(',')
                for index, line in enumerate(scorecards):
                    print(line + " " + str(index))
                    count = cursor.execute(
                        "INSERT INTO ScorecardMaster (Scorecard) VALUES (?)", line)
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist.")
        cnxn.commit()

x = LoadConnInfo(inputfilepath);
y = LoadSchemaMetaData(inputfilepath);

server = 'MTN-LAPTOP\SQLEXPRESS'  # for a named instance
database = 'FarmFinderDB'
username = 'FarmFinderDBA'
password = 'a'
fileName = 'C:\\Users\\minston\\Documents\\DBInput.txt'
dbInfo = DataObject(server, database, username, password)
converter = ConvertTextFileToDBTable(fileName, dbInfo)
converter.run()
