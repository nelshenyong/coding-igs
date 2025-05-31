package main.java;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.Parent;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/main/java/test.fxml"));
        Parent root = loader.load();
        primaryStage.setScene(new Scene(root, 700, 500));
        primaryStage.show();
    }
    public static void main(String[] args) throws Exception {
        launch(args);
    }
} 