package fbclogic;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;




@ComponentScan(basePackages = {
        "fbclogic.controller",
        "fbclogic.repository",
        "fbclogic.model",
        "fbclogic.service"
    },
    excludeFilters = {
        @ComponentScan.Filter(type = FilterType.ANNOTATION, value = Configuration.class)
    })
@SpringBootApplication
public class FarmFinderApplication {

	public static void main(String[] args) {
		SpringApplication.run(FarmFinderApplication.class, args);
		
	}

	
	
}
