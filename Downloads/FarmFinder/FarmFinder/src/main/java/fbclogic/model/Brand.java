package fbclogic.model;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Brand {
    @Id
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
}
