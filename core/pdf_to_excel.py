import os
from pathlib import Path
import tabula

def convert_pdf_to_excel(input_path, output_dir):
    
    pdf_path = Path(input_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError("El archivo pdf seleccionado no existe")
    
    output_path = Path(output_dir) / (pdf_path.stem + ".xlsx")

    tabula.convert_into(
        str(pdf_path),
        str(output_path),
        output_format="xlsx",
        pages="all"
    )

    return output_path