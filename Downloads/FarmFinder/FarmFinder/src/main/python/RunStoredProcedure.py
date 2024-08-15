import pyodbc

class DBConnection:
    def __init__(self, server, databaseName, username, password):
        if (server is None or databaseName is None or username is None or password is None):
            raise Exception("One value is null")
        self.server = server
        self.database = databaseName
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.getServer()+';DATABASE=' +
                              self.getDatabase()+';UID='+self.getUsername()+';PWD=' + self.getPassword())
            
            print("Connection successful")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def getServer(self):
        return self.server

    def getDatabase(self):
        return self.database

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    def runStoredProcedure(self):
        if self.connection:
            print("running stored procedure")
            cursor = self.connection.cursor()

            scorecardName = 'Plant-Based Beverages Scorecard'
            starRating = 1
            products = None
            brandMarketArea = 'CA'
            organic = 'Yes'
            plantBased = 'SOY'
            parentCompany = None
            companyType = None
            participatedInSurvey = None

            sql = """\
        SET NOCOUNT ON;
        DECLARE @RC int;
        EXEC @RC = [FarmFinderDB].[dbo].[getBrandsFromCriteria] @ScorecardName = ?, @StarRating = ?, @Products = ?, @BrandMarketArea = ?, @Organic = ?, @PlantBased = ?, @ParentCompany = ?, @CompanyType = ?, @ParticipatedInSurvey = ?;
        SELECT @RC AS rc;
        """
            values = (scorecardName, starRating, products, brandMarketArea, organic, plantBased, parentCompany, companyType, participatedInSurvey)
            cursor.execute(sql, values)
            results = cursor.fetchall()
            print("Results: ")
            for row in results:
                print(row)
        else:
            print("no connection established")
def main():
    server = 'MTN-LAPTOP\SQLEXPRESS'  # for a named instance
    databaseName = 'FarmFinderDB'
    username = 'FarmFinderDBA'
    password = 'ab'
    dbConnection = DBConnection(server, databaseName, username, password)
    dbConnection.connect()
    dbConnection.runStoredProcedure()

if __name__ == "__main__":
    main()