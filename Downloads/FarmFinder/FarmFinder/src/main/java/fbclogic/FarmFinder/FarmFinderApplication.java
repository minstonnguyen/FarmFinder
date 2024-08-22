package fbclogic.FarmFinder;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@SpringBootApplication
@RestController
public class FarmFinderApplication {

	public static void main(String[] args) {
		SpringApplication.run(FarmFinderApplication.class, args);
		
	}
	@RequestMapping("/bye")
	public String bye() {
		return "bye";
	}
	
}
