package fbclogic.service;
import java.util.ArrayList;
import java.util.List;


import org.springframework.stereotype.Service;

import fbclogic.model.Brand;

@Service
public class BrandService {
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
    public List<Brand> fetchBrandList(){
        return new ArrayList<Brand>();
       
    }
    /*
     * updates existing brand
     * @param brand the brand with updated info
     * @param brandID the ID of the brand to update
     */
    public Brand updateBrand(Brand brand, Integer brandID)
    {
        return brand;
    }
    /*
     * deletes existing brand
     * @param brandID the ID of the brand to delete
     */
    public void deleteBrandByID(Integer brandID){

    }
}
