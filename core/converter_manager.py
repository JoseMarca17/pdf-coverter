from core.pdf_to_word import convert_pdf_to_word
from core.pdf_to_excel import convert_pdf_to_excel
from core.pdf_to_image import convert_pdf_to_images

def convert(input_path, output_dir, output_format):
    output_format = output_format.lower()
    
    if output_format == "word":
        return convert_pdf_to_word(input_path, output_dir)
    
    if output_format == "excel":
        return convert_pdf_to_excel(input_path, output_dir)
    
    if output_format == "imagenes":
        return convert_pdf_to_images(input_path, output_dir)
    
    else: 
        raise ValueError("Formato no admitido")