import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.geometry.Insets;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.HashMap;
import java.util.Map;

public class Controller implements Initializable {

    @FXML private ComboBox<String> physicsTopicCombo;
    @FXML private VBox inputFields;
    @FXML private TextArea resultArea;
    @FXML private TextArea informationArea;
    @FXML private Button calculateButton;

    private Map<String, PhysicsTopic> physicsTopics;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        // Initialize physics topics
        physicsTopics = new HashMap<>();
        
        // Mekanika
        physicsTopics.put("Gaya Gravitasi", new PhysicsTopic(
            "Gaya Gravitasi",
            "Gaya tarik-menarik antara dua benda bermassa.\nRumus: F = G * (m1 * m2) / r²\nDimana:\nG = Konstanta gravitasi (6.67430 × 10^-11 N⋅m²/kg²)\nm1, m2 = massa kedua benda (kg)\nr = jarak antara kedua benda (m)",
            new String[]{"Massa Benda 1 (kg)", "Massa Benda 2 (kg)", "Jarak (m)"},
            (inputs) -> {
                double m1 = Double.parseDouble(inputs[0]);
                double m2 = Double.parseDouble(inputs[1]);
                double r = Double.parseDouble(inputs[2]);
                double G = 6.67430e-11;
                double F = G * (m1 * m2) / (r * r);
                return String.format("Gaya Gravitasi = %.2e N", F);
            }
        ));

        physicsTopics.put("Energi Kinetik", new PhysicsTopic(
            "Energi Kinetik",
            "Energi yang dimiliki benda karena geraknya.\nRumus: Ek = ½ * m * v²\nDimana:\nm = massa benda (kg)\nv = kecepatan benda (m/s)",
            new String[]{"Massa (kg)", "Kecepatan (m/s)"},
            (inputs) -> {
                double m = Double.parseDouble(inputs[0]);
                double v = Double.parseDouble(inputs[1]);
                return String.format("Energi Kinetik = %.2f J", 0.5 * m * v * v);
            }
        ));

        physicsTopics.put("Energi Potensial", new PhysicsTopic(
            "Energi Potensial",
            "Energi yang dimiliki benda karena posisinya.\nRumus: Ep = m * g * h\nDimana:\nm = massa benda (kg)\ng = percepatan gravitasi (m/s²)\nh = ketinggian (m)",
            new String[]{"Massa (kg)", "Ketinggian (m)", "Percepatan Gravitasi (m/s²)"},
            (inputs) -> {
                double m = Double.parseDouble(inputs[0]);
                double h = Double.parseDouble(inputs[1]);
                double g = Double.parseDouble(inputs[2]);
                return String.format("Energi Potensial = %.2f J", m * g * h);
            }
        ));

        // Listrik
        physicsTopics.put("Hukum Ohm", new PhysicsTopic(
            "Hukum Ohm",
            "Hubungan antara tegangan, arus, dan hambatan dalam rangkaian listrik.\nRumus: V = I * R\nDimana:\nV = tegangan (Volt)\nI = arus (Ampere)\nR = hambatan (Ohm)",
            new String[]{"Arus (A)", "Hambatan (Ω)"},
            (inputs) -> {
                double I = Double.parseDouble(inputs[0]);
                double R = Double.parseDouble(inputs[1]);
                return String.format("Tegangan = %.2f V", I * R);
            }
        ));

        physicsTopics.put("Daya Listrik", new PhysicsTopic(
            "Daya Listrik",
            "Laju perubahan energi listrik.\nRumus: P = V * I\nDimana:\nP = daya (Watt)\nV = tegangan (Volt)\nI = arus (Ampere)",
            new String[]{"Tegangan (V)", "Arus (A)"},
            (inputs) -> {
                double V = Double.parseDouble(inputs[0]);
                double I = Double.parseDouble(inputs[1]);
                return String.format("Daya Listrik = %.2f W", V * I);
            }
        ));

        // Gelombang
        physicsTopics.put("Frekuensi", new PhysicsTopic(
            "Frekuensi",
            "Jumlah getaran per detik.\nRumus: f = 1/T\nDimana:\nf = frekuensi (Hz)\nT = periode (s)",
            new String[]{"Periode (s)"},
            (inputs) -> {
                double T = Double.parseDouble(inputs[0]);
                return String.format("Frekuensi = %.2f Hz", 1/T);
            }
        ));

        // Set up ComboBox
        physicsTopicCombo.setItems(FXCollections.observableArrayList(physicsTopics.keySet()));
        physicsTopicCombo.setOnAction(e -> updateInputFields());
    }

    private void updateInputFields() {
        inputFields.getChildren().clear();
        String selectedTopic = physicsTopicCombo.getValue();
        if (selectedTopic != null) {
            PhysicsTopic topic = physicsTopics.get(selectedTopic);
            informationArea.setText(topic.getDescription());
            
            for (String label : topic.getInputLabels()) {
                VBox field = new VBox(5);
                field.setPadding(new Insets(5));
                field.getChildren().add(new Label(label));
                TextField textField = new TextField();
                textField.setPromptText("Masukkan nilai " + label.toLowerCase());
                field.getChildren().add(textField);
                inputFields.getChildren().add(field);
            }
        }
    }

    @FXML
    private void handleCalculate(ActionEvent event) {
        String selectedTopic = physicsTopicCombo.getValue();
        if (selectedTopic != null) {
            PhysicsTopic topic = physicsTopics.get(selectedTopic);
            String[] inputs = new String[topic.getInputLabels().length];
            
            for (int i = 0; i < inputs.length; i++) {
                VBox field = (VBox) inputFields.getChildren().get(i);
                TextField textField = (TextField) field.getChildren().get(1);
                inputs[i] = textField.getText();
            }
            
            try {
                String result = topic.calculate(inputs);
                resultArea.setText(result);
            } catch (NumberFormatException e) {
                resultArea.setText("Error: Mohon masukkan angka yang valid");
            } catch (Exception e) {
                resultArea.setText("Error: " + e.getMessage());
            }
        }
    }
}

class PhysicsTopic {
    private String name;
    private String description;
    private String[] inputLabels;
    private PhysicsCalculator calculator;

    public PhysicsTopic(String name, String description, String[] inputLabels, PhysicsCalculator calculator) {
        this.name = name;
        this.description = description;
        this.inputLabels = inputLabels;
        this.calculator = calculator;
    }

    public String getName() { return name; }
    public String getDescription() { return description; }
    public String[] getInputLabels() { return inputLabels; }
    public String calculate(String[] inputs) { return calculator.calculate(inputs); }
}

interface PhysicsCalculator {
    String calculate(String[] inputs);
} 