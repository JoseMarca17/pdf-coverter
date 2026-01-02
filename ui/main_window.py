from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QComboBox, QVBoxLayout, QWidget
from core.converter_manager import convert
from services.file_manager import is_pdf, ensure_directory
from pathlib import Path
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Converter")
        self.setMinimumSize(600,400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)
        
        self.label_file = QLabel("Seleccione un pdf")
        self.button_select_file = QPushButton("Abrir PDF")
        self.combo_format = QComboBox()
        self.combo_format.addItems(["Word", "Excel", "Imagenes"])
        self.button_convert = QPushButton("Convertir")
        self.label_status = QLabel("Esperando accion...")
        
        self.layout.addWidget(self.label_file)
        self.layout.addWidget(self.button_select_file)
        self.layout.addWidget(self.combo_format)
        self.layout.addWidget(self.button_convert)
        self.layout.addWidget(self.label_status)
        
        self.button_select_file.clicked.connect(self.select_file)
        self.button_convert.clicked.connect(self.start_conversion)
        
        self.pdf_path = None 
        
    def select_file(self):
        result = QFileDialog.getOpenFileName(self, "Seleccionar PDF", "", "PDF files (*.pdf)")
        file_path = result[0]
            
        if file_path:
            self.pdf_path = Path(file_path)
            self.label_file.setText(f"Archivo: {self.pdf_path.name}")

    def start_conversion(self):
        if not self.pdf_path or not is_pdf(self.pdf_path):
            self.label_status.setText("Seleccione un PDF valido...")
            return 
        
        output_dir = ensure_directory("output_gui")
        output_format = self.combo_format.currentText().lower()
        try:
            result = convert(self.pdf_path, output_dir, output_format)
            self.label_status.setText(f"Convertido: {result}")
        except Exception as e:
            self.label_status.setText(f"Error: {e}")
