import os
from pathlib import Path
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_dir):
    
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError("El archivo PDF seleccionado no existe")
    
    images = convert_from_path(str(pdf_path))
    output_dir = Path(output_dir) / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    saved_files = []
    
    for i, image in enumerate(images, start=1):
        img_path = output_dir / f"page_{i}.png"
        image.save(img_path, "PNG")
        saved_files.append(img_path)
    
    return saved_files