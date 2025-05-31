import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.Parent;
import javafx.stage.Stage;
import java.io.File;

public class App extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(new File("main.fxml").toURI().toURL());
        Parent root = loader.load();
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setTitle("Kalkulator Fisika");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        // Add JavaFX modules
        System.setProperty("javafx.verbose", "true");
        System.setProperty("javafx.verbose.exceptions", "true");
        
        // Launch the application
        launch(args);
    }
} 