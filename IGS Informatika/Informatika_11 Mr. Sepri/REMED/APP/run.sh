#!/bin/bash

# Check if JavaFX is installed
if [ ! -d "/usr/share/openjfx/lib" ]; then
    echo "JavaFX not found. Installing JavaFX..."
    sudo apt-get update
    sudo apt-get install -y openjfx
fi

# Go to src directory
cd src

# Compile the Java files
echo "Compiling Java files..."
javac --module-path /usr/share/openjfx/lib --add-modules javafx.controls,javafx.fxml App.java Controller.java

# Run the application
echo "Running the application..."
java --module-path /usr/share/openjfx/lib --add-modules javafx.controls,javafx.fxml App 