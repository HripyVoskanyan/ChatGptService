package sia.app.service;

import org.springframework.stereotype.Service;
import sia.app.model.User;
import sia.app.repository.UserRepository;

import java.util.List;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User loginUser(String login, String password) {
        final User user = userRepository.findByLoginAndPassword(login, password);
        // Check if user exists and if password matches
        if (user != null && user.getPassword().equals(password)) {
            return user; // Authentication successful
        } else {
            return null; // Authentication failed
        }
    }
}
