package fbclogic.FarmFinder;
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CallStoredProcedure {
    private String server;
    private String database;
    private String username;
    private String password;
    private Connection connection;

    public CallStoredProcedure(String server, String databaseName, String username, String password) throws Exception {
        if (server == null || databaseName == null || username == null || password == null) {
            throw new Exception("One value is null");
        }
        this.server = server;
        this.database = databaseName;
        this.username = username;
        this.password = password;
        this.connection = null;
    }

    public void connect() {
        try {
            String connectionUrl = "jdbc:sqlserver://" + getServer() + ";databaseName=" + getDatabase() + ";user=" + getUsername() + ";password=" + getPassword();
            connection = DriverManager.getConnection(connectionUrl);
            System.out.println("Connection successful");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public String getServer() {
        return server;
    }

    public String getDatabase() {
        return database;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void runStoredProcedure() {
        if (connection != null) {
            System.out.println("running stored procedure");

            String scorecardName = "Plant-Based Beverages Scorecard";
            int starRating = 1;
            String products = null;
            String brandMarketArea = null;
            String organic = "Yes";
            String plantBased = "SOY";
            String parentCompany = null;
            String companyType = null;
            String participatedInSurvey = null;

            String sql = "SET NOCOUNT ON; " +
                    "DECLARE @RC int; " +
                    "EXEC @RC = [FarmFinderDB].[dbo].[getBrandsFromCriteria] " +
                    "@ScorecardName = ?, @StarRating = ?, @Products = ?, @BrandMarketArea = ?, @Organic = ?, @PlantBased = ?, @ParentCompany = ?, @CompanyType = ?, @ParticipatedInSurvey = ?; " +
                    "SELECT @RC AS rc;";

            try (CallableStatement stmt = connection.prepareCall(sql)) {
                stmt.setString(1, scorecardName);
                stmt.setInt(2, starRating);
                stmt.setString(3, products);
                stmt.setString(4, brandMarketArea);
                stmt.setString(5, organic);
                stmt.setString(6, plantBased);
                stmt.setString(7, parentCompany);
                stmt.setString(8, companyType);
                stmt.setString(9, participatedInSurvey);

                boolean hasResults = stmt.execute();

                if (hasResults) {
                    try (ResultSet rs = stmt.getResultSet()) {
                        System.out.println("Results: ");
                        while (rs.next()) {
                            System.out.println(rs.getString(1));
                        }
                    }
                } else {
                    System.out.println("No results returned from stored procedure.");
                }
            } catch (SQLException e) {
                System.out.println("Error executing stored procedure: " + e.getMessage());
            }
        } else {
            System.out.println("no connection established");
        }
    }

    public static void main(String[] args) {
        String server = "MTN-LAPTOP\\SQLEXPRESS";  // for a named instance
        String databaseName = "FarmFinderDB";
        String username = "FarmFinderDBA";
        String password = "ab";
        System.out.println("yes");
        try {
            CallStoredProcedure dbConnection = new CallStoredProcedure(server, databaseName, username, password);
            dbConnection.connect();
            dbConnection.runStoredProcedure();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
