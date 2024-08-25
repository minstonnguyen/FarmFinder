package fbclogic.model;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Farm {
    @Id
    private int farmID;
    private String farmName;
    private String city;
    private String state;
    private byte[] logo; // For varbinary(MAX)
    private String website;

    // Parameterized constructor
    public Farm(int farmID, String farmName, String city, String state, byte[] logo, String website) {
        this.farmID = farmID;
        this.farmName = farmName;
        this.city = city;
        this.state = state;
        this.logo = logo;
        this.website = website;
    }

    // Getters and setters

    public int getFarmID() {
        return farmID;
    }

    public void setFarmID(int farmID) {
        this.farmID = farmID;
    }

    public String getFarmName() {
        return farmName;
    }

    public void setFarmName(String farmName) {
        this.farmName = farmName;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public byte[] getLogo() {
        return logo;
    }

    public void setLogo(byte[] logo) {
        this.logo = logo;
    }

    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
}