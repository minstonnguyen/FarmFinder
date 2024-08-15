package fbclogic.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import fbclogic.model.Brand;

@Repository
public interface BrandRepository extends JpaRepository<Brand, Integer>{
    
}
