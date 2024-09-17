package fbclogic.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.query.Procedure;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import fbclogic.model.Brand;



@Repository
public interface BrandRepository extends JpaRepository<Brand, Integer>{
    List<Brand> findByBrandID(int brandID);

    //@ManyToOne(fetch = FetchType.LAZY)
    /* 
    @Query("SELECT b.farmID FROM Brand b WHERE b.brandName = :brandName")
    Farm getFarm(@Param("brandName") String brandName);
    */
    @Procedure(procedureName = "getBrandsFromCriteria")
    List<Brand> getBrandsFromCriteria(
        @Param("ScorecardName") String scorecardName,
        @Param("StarRating") short starRating,
        @Param("Products") String products,
        @Param("BrandMarketArea") String brandMarketArea,
        @Param("Organic") String organic,
        @Param("PlantBased") String plantBased,
        @Param("ParentCompany") String parentCompany,
        @Param("CompanyType") String companyType,
        @Param("ParticipatedInSurvey") String participatedInSurvey
    );
}
