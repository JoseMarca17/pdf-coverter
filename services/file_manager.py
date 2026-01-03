from pathlib import Path

def ensure_directory(folder_path):
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def build_output_path(input_pdf: Path, output_dir: Path, new_extension: str)-> Path:
    return output_dir / f"{input_pdf.stem}.{new_extension}"