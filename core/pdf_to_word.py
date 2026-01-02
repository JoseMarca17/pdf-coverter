import os
from pathlib import Path
from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, output_dir):
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError("El archivo PDF que seleccionaste no existe")
    
    if pdf_path.stat().st_size == 0:
        raise ValueError("El archivo PDF esta vacio")
    
    output_path = Path(output_dir)/(pdf_path.stem + ".docx")
    
    
    
    try:
        cv = Converter(str(pdf_path))
        cv.convert(str(output_path))
        
    finally:
        if 'cv' in locals():
            cv.close()
    
    return output_path