package fbclogic.FarmFinder;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FarmFinderController {
    @RequestMapping("/")
    public String helloWorld()
    {
        return "Hello World from Spring Boot";
    }

    @RequestMapping("/bye")
    public String byeWorld()
    {
        return "bye world";
    }
}
