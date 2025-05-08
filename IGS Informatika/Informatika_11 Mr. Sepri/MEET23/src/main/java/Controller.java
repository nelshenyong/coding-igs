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
    private TextField tfKelas;

    @FXML
    private TextField tfUsia;

    @FXML
    private TextField tfBahasa;

    @FXML
    void actionSend(ActionEvent event) {
        String nama = tfNama.getText();
        String kelas = tfKelas.getText();
        String usia = tfUsia.getText();
        String bahasa = tfBahasa.getText();

        String pesan = "Nama saya " + nama + " di kelas " + kelas + " dan berusia " + usia + " sekarang sedang belajar " + bahasa;

        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Popup");
        alert.setHeaderText("Informasi");
        alert.setContentText(pesan);
        alert.showAndWait();
    }
}