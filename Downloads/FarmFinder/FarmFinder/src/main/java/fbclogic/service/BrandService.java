package fbclogic.service;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import fbclogic.model.Brand;
import fbclogic.repository.BrandRepository;

@Service
public class BrandService {
    @Autowired
    private BrandRepository brandRepository;
    /*
     * saves brand
     * @param brand the brand to save
     */
    public Brand saveBrand(Brand brand){
        return brand;
    }
    /*
    * fetches list of brand entities
    * @return list of brands
    */
    public List<Brand> getBrands() {
        return brandRepository.findAll();
    }
    /*
     * updates existing brand
     * @param brand the brand with updated info
     * @param brandID the ID of the brand to update
     */
    public Brand updateBrand(Brand brand, Integer brandID)
    {
        return brandRepository.findById(brandID).map(existingBrand -> {
            // Update fields
            existingBrand.setBrandName(brand.getBrandName());
            // (Repeat for other fields as necessary)
            return brandRepository.save(existingBrand);
        }).orElse(null);
    }
    /*
     * deletes existing brand
     * @param brandID the ID of the brand to delete
     */
    public void deleteBrandByID(Integer brandID){
        brandRepository.deleteById(brandID);
    }

    public List<Brand> getBrandsFromCriteria(String scorecardName, short starRating, String products, String brandMarketArea, String organic, String plantBased, String parentCompany, String companyType, String participatedInSurvey) {
        return brandRepository.getBrandsFromCriteria(scorecardName, starRating, products, brandMarketArea, organic, plantBased, parentCompany, companyType, participatedInSurvey);
    }
    
}
