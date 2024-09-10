package fbclogic.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import fbclogic.model.Brand;
import fbclogic.repository.BrandRepository;
import fbclogic.service.BrandService;



@RestController
@RequestMapping("/api/brands")
public class BrandController {
    private final BrandRepository brandRepository;
    private final BrandService brandService;

    @Autowired
    public BrandController(BrandRepository brandRepository, BrandService brandService) {
        this.brandRepository = brandRepository;
        this.brandService = brandService;
    }
    
    
    
    
    @RequestMapping("/getBrands")
    public List<Brand> getBrands(Model model) {
        
        List<Brand> listBrands = brandService.getBrands();
        model.addAttribute("listBrands", listBrands);
        return listBrands;
    }

    @RequestMapping("/bye")
    public String bye() {
        return "bye";
    }

    @RequestMapping("/hi")
    public String hi() {
        return "hi";
    }

    @GetMapping("/getBrandsByCriteria")
    public List<Brand> getBrandsByCriteria(
        @RequestParam String scorecardName,
        @RequestParam short starRating,
        @RequestParam String products,
        @RequestParam String brandMarketArea,
        @RequestParam String organic,
        @RequestParam String plantBased,
        @RequestParam String parentCompany,
        @RequestParam String companyType,
        @RequestParam String participatedInSurvey
        ) {
            return brandService.getBrandsFromCriteria(scorecardName, starRating, products, brandMarketArea, organic, plantBased, parentCompany, companyType, participatedInSurvey);
    }

    
    


}
    


