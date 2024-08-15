package fbclogic.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import fbclogic.model.Farm;

@Repository
public interface FarmRepository extends JpaRepository<Farm, Integer>{
    
}