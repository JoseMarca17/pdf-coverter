from pathlib import Path

VALID_FORMATS = ["word", "excel", "imagenes"]

def validate_pdf(path: Path):
    if path is None: 
        raise ValueError("No se selecciono ningun archivo")
    
    if not path.exists():
        raise FileNotFoundError("El archivo no existe")
    
    if path.suffix.lower() != ".pdf":
        raise ValueError("El archivo no es PDF")

def validate_output_format(format_name):
    if format_name not in VALID_FORMATS: 
        raise ValueError(f"El formato no esta permitido: {format_name}")