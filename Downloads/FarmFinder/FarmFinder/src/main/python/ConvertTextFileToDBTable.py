# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:47:59 2024

@author: minston
"""

from html.parser import HTMLParser
import requests
import pyodbc
import datetime

class DBTableData:
    
    def __init__(self, numColumns, numRows):
        self.numColumns = numColumns
        self.numRows = numRows
        self.arr = [[None for i in range(numColumns)] for j in range(numRows)]
    def printDBTableData(self):
        for r in self.arr:
            for c in r:
                print(c, end=" ")
            print()
    def setValue(self, x, y, value):
        self.arr[x][y] = value
    def getValue(self, x, y):
        return self.arr[x][y]
class TextFile:
    def __init__(self, textFileLocation, delimeter):
        self.textFileLocation = textFileLocation
        self.delimeter = delimeter
    def getTextFileLocation(self):
        return self.textFileLocation
    def getDelimeter(self):
        return self.delimeter
class DBConnection:
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
    def __init__(self, filename, dbConnectionInfo, delimeter, tableName):
        self.filename = filename
        self.dbConnectionInfo = dbConnectionInfo
        self.delimeter = delimeter
        self.tableName = tableName
    def run(self):
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.split('^_')
                numRows = len(lines) -1 #length of rows - 1 to remove top header      
                columnNames = lines[0].strip().split(self.getDelimeter()) #column names extraction ei ID, Name
                numColumns = len(columnNames)
                dbTableData = DBTableData(len(columnNames), numRows) #create the dataTable2D array
                
                self.insertFromDBTableDataToSQL(lines, dbTableData, numColumns, numRows, columnNames, tableName)
                    
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist.")
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
        
    def insertFromDBTableDataToSQL(self, lines, dbTableData, numColumns, numRows, columnNames, tableName):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.dbConnectionInfo.getServer()+';DATABASE=' +
                              self.dbConnectionInfo.getDatabase()+';UID='+self.dbConnectionInfo.getUsername()+';PWD=' + self.dbConnectionInfo.getPassword())
        cursor = cnxn.cursor()
        for index, line in enumerate(lines[1:]):
            values = line.strip().split(self.getDelimeter())
            for columnIndex, value in enumerate(values):
                dbTableData.setValue(index, columnIndex, value if value != 'NULL' else None)
        print(tableName) 
           
        for row in range(numRows):
             values = [dbTableData.getValue(row, col) for col in range(numColumns)]
             insert_query = f"""
             INSERT INTO {self.tableName} ({', '.join(columnNames)}) VALUES ({', '.join(['?' for _ in range(numColumns)])})
                """
             cursor.execute(insert_query, values)
             cnxn.commit()
             
    def getDelimeter(self):
        return self.delimeter
    
#x = LoadConnInfo(inputfilepath);
#y = LoadSchemaMetaData(inputfilepath);

server = 'MTN-LAPTOP\SQLEXPRESS'  # for a named instance
database = 'FarmFinderDB'
username = 'FarmFinderDBA'
password = 'a'
fileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\BrandNameTextFileTest.txt"

delimeter = '|'

eggTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\EggScorecardsWebscrapedTextFile.txt"
dairyTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\DairyScorecardsWebscrapedTextFile.txt"
beefTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\BeefScorecardsWebscrapedTextFile.txt"
poultryTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\PoultryScorecardsWebscrapedTextFile.txt"
yougurtTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\YogurtScorecardsWebscrapedTextFile.txt"
plantBasedBeverageTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\PlantBasedBeveragesScorecardsWebscrapedTextFile.txt"
snackbarTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\SnackBarScorecardsWebscrapedTextFile.txt"
cottageCheeseTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\CottageCheeseScorecardsWebscrapedTextFile.txt"
cerealTextFileName = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir\\CerealScorecardsWebscrapedTextFile.txt"

eggTextFile = TextFile(eggTextFileName, delimeter)
dairyTextFile = TextFile(dairyTextFileName, delimeter)
beefTextFile = TextFile(beefTextFileName, delimeter)
poultryTextFile = TextFile(poultryTextFileName, delimeter)
yogurtTextFile = TextFile(yougurtTextFileName, delimeter)
plantBasedBeverageTextFile = TextFile(plantBasedBeverageTextFileName, delimeter)
snackbarTextFile = TextFile(snackbarTextFileName, delimeter)
cottageCheeseTextFile = TextFile(cottageCheeseTextFileName, delimeter)
cerealTextFile = TextFile(cerealTextFileName, delimeter)
tableName = 'BrandMaster'
dbInfo = DBConnection(server, database, username, password)

eggConverter = ConvertTextFileToDBTable(eggTextFile.getTextFileLocation(), dbInfo, eggTextFile.getDelimeter(), tableName)
dairyConverter = ConvertTextFileToDBTable(dairyTextFile.getTextFileLocation(), dbInfo, dairyTextFile.getDelimeter(), tableName)
beefConverter = ConvertTextFileToDBTable(beefTextFile.getTextFileLocation(), dbInfo, beefTextFile.getDelimeter(), tableName)
poultryConverter = ConvertTextFileToDBTable(poultryTextFile.getTextFileLocation(), dbInfo, poultryTextFile.getDelimeter(), tableName)
yogurtConverter = ConvertTextFileToDBTable(yogurtTextFile.getTextFileLocation(), dbInfo, yogurtTextFile.getDelimeter(), tableName)
plantBasedBeverageConverter = ConvertTextFileToDBTable(plantBasedBeverageTextFile.getTextFileLocation(), dbInfo, plantBasedBeverageTextFile.getDelimeter(), tableName)
snackBarConverter = ConvertTextFileToDBTable(snackbarTextFile.getTextFileLocation(), dbInfo, snackbarTextFile.getDelimeter(), tableName)
cottageCheeseConverter = ConvertTextFileToDBTable(cottageCheeseTextFile.getTextFileLocation(), dbInfo, cottageCheeseTextFile.getDelimeter(), tableName)
cerealConverter = ConvertTextFileToDBTable(cerealTextFile.getTextFileLocation(), dbInfo, cerealTextFile.getDelimeter(), tableName)
#eggConverter.run()
#dairyConverter.run()
#beefConverter.run()
#poultryConverter.run()
#yogurtConverter.run()
#plantBasedBeverageConverter.run()
#snackBarConverter.run()
#cottageCheeseConverter.run()
cerealConverter.run()