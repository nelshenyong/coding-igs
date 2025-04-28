import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.Parent;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage PrimaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("scene.fxml"));
        Parent root = loader.load();
        PrimaryStage.setScene(new Scene(root, 500, 500));
        PrimaryStage.show();
    }
    public static void main(String[] args) throws Exception {
        launch(args);
    }
}