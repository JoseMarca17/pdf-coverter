from pathlib import Path

def file_exists(file_path):
    return Path(file_exists).exists()

def is_pdf(file_path):
    return Path(file_path).suffix.lower() == ".pdf"

def ensure_directory(folder_path):
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def normalize_path(dir):
    return Path(dir).resolve()