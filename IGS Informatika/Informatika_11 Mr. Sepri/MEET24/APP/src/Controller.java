import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.ListView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.beans.property.SimpleStringProperty;

import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable {

    @FXML
    private Button ok;

    @FXML
    private ComboBox<Siswa> cb;

    @FXML
    private ListView<Siswa> list;

    @FXML
    private TableView<Siswa> tbl;
    
    @FXML
    private TableColumn<Siswa, String> kolom1;
    
    private ObservableList<Siswa> daftarSiswa;

    @FXML
    void actionOk(ActionEvent event) {
        daftarSiswa.add(new Siswa("Nana"));
        daftarSiswa.add(new Siswa("Nini"));
        daftarSiswa.add(new Siswa("Nunu"));
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        // Inisialisasi data siswa
        daftarSiswa = FXCollections.observableArrayList(
            new Siswa("Nana"),
            new Siswa("Nini"),
            new Siswa("Nunu")
        );

        // Set up ListView
        list.setItems(daftarSiswa);
        
        // Set up ComboBox
        cb.setItems(daftarSiswa);
        cb.getSelectionModel().select(0);
        
        // Set up TableView
        tbl.setItems(daftarSiswa);
        
        // Set up TableColumn
        if (kolom1 != null) {
            kolom1.setCellValueFactory(cellData -> 
                new SimpleStringProperty(cellData.getValue().getNama()));
        } else {
            System.err.println("Warning: kolom1 is null!");
        }
    }
}