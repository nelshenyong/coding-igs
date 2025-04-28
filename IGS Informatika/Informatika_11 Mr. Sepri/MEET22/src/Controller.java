
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class Controller {

    @FXML
    private Button btnSend;

    @FXML
    private TextField tfNama;

    @FXML
    void actionSend(ActionEvent event) {
        String namaOk = tfNama.getText();
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Popup");
            alert.setHeaderText("Text: ");
            alert.setContentText(namaOk);
            alert.showAndWait();
    }

}
