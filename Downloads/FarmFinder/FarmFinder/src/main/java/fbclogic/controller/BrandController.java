package fbclogic.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import fbclogic.model.Brand;
import fbclogic.service.BrandService;


@RestController
@RequestMapping(path = "api/v1/brand")
public class BrandController {
    private final BrandService brandService;

    @Autowired
    public BrandController(BrandService brandService)
    {
        this.brandService = brandService;
    }
    @GetMapping()
    public List<Brand> getBrands() {
        return brandService.fetchBrandList();
    }
    
}

