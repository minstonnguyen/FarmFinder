package fbclogic.model;


import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "BrandMaster")
public class Brand {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int brandID;
    private int scorecardID;
    private int farmID;
    private short starRating;
    private int score;
    private String products;
    private String brandMarketArea;
    private String organic;
    private String plantBased;
    private String parentCompany;
    private String companyType;
    private String participatedInSurvey;
    private String description;
    private String brandName;
    public Brand(int brandID, int scorecardID, int farmID, short starRating, int score, String products, String brandMarketArea, String organic, String plantBased, String parentCompany, String companyType, String participatedInSurvey, String description, String brandName) {
        this.brandID = brandID;
        this.scorecardID = scorecardID;
        this.farmID = farmID;
        this.starRating = starRating;
        this.score = score;
        this.products = products;
        this.brandMarketArea = brandMarketArea;
        this.organic = organic;
        this.plantBased = plantBased;
        this.parentCompany = parentCompany;
        this.companyType = companyType;
        this.participatedInSurvey = participatedInSurvey;
        this.description = description;
        this.brandName = brandName;
    }
    public int getBrandID() {
        return brandID;
    }

    public void setBrandID(int brandID) {
        this.brandID = brandID;
    }

    public int getScorecardID() {
        return scorecardID;
    }

    public void setScorecardID(int scorecardID) {
        this.scorecardID = scorecardID;
    }

    public int getFarmID() {
        return farmID;
    }

    public void setFarmID(int farmID) {
        this.farmID = farmID;
    }

    public short getStarRating() {
        return starRating;
    }

    public void setStarRating(short starRating) {
        this.starRating = starRating;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public String getProducts() {
        return products;
    }

    public void setProducts(String products) {
        this.products = products;
    }

    public String getBrandMarketArea() {
        return brandMarketArea;
    }

    public void setBrandMarketArea(String brandMarketArea) {
        this.brandMarketArea = brandMarketArea;
    }

    public String getOrganic() {
        return organic;
    }

    public void setOrganic(String organic) {
        this.organic = organic;
    }

    public String getPlantBased() {
        return plantBased;
    }

    public void setPlantBased(String plantBased) {
        this.plantBased = plantBased;
    }

    public String getParentCompany() {
        return parentCompany;
    }

    public void setParentCompany(String parentCompany) {
        this.parentCompany = parentCompany;
    }

    public String getCompanyType() {
        return companyType;
    }

    public void setCompanyType(String companyType) {
        this.companyType = companyType;
    }

    public String getParticipatedInSurvey() {
        return participatedInSurvey;
    }

    public void setParticipatedInSurvey(String participatedInSurvey) {
        this.participatedInSurvey = participatedInSurvey;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getBrandName() {
        return brandName;
    }

    public void setBrandName(String brandName) {
        this.brandName = brandName;
    }
    @Override
    public String toString(){
        return "Brand{" + brandName;
    }
}
