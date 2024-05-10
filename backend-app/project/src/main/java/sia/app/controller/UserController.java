package sia.app.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import sia.app.model.User;
import sia.app.service.UserService;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;
import java.util.List;

import static org.springframework.http.HttpHeaders.CONTENT_TYPE;

@RestController
@RequestMapping(path = "api/v1")
public class UserController {
    //private static final URI premiumURI = new URI("");
    //private static final URI standardURI = "";

    private final UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("")
    public List<User> getUsers() {
        return userService.getAllUsers();
    }

    @PostMapping("login")
    public ResponseEntity<User> loginUser(@RequestParam String login,
                                          @RequestParam String password) {
        final User user = userService.loginUser(login, password);
        if (user == null) {
            return ResponseEntity.badRequest().build();
        }
        return ResponseEntity.ok(user);
    }


    @PostMapping("/sendRequest")
    public String sendInputText(@RequestParam String inputText,
                                @RequestParam Boolean isPremium) throws URISyntaxException, IOException, InterruptedException {
        // Set up the request headers
        //URI uri = isPremium ? premiumURI : standardURI;


        java.net.http.HttpRequest httpRequest = java.net.http.HttpRequest.newBuilder()
                .uri(new URI("https://078d-5-77-254-70.ngrok-free.app/generate"))
                .header(CONTENT_TYPE, String.valueOf(MediaType.APPLICATION_JSON))
                .POST(java.net.http.HttpRequest.BodyPublishers.ofString("{\"text\": \"" + inputText + "\"}"))
                .build();
        HttpClient httpClient = HttpClient.newHttpClient();
        HttpResponse<String> response = httpClient.send(httpRequest, HttpResponse.BodyHandlers.ofString());
        return response.body();
    }
}
