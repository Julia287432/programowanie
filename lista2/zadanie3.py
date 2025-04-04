import os
import zipfile
from datetime import datetime

def create_backup(directory):
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    archive_name = f"{current_date}_backup.zip"
    
    with zipfile.ZipFile(archive_name, 'w') as zip_file:
        for root, directories, files in os.walk(directory):
            if root.startswith("."):
                continue
            
            for file in files:
                file_path = os.path.join(root, file)
                
                zip_file.write(file_path, os.path.relpath(file_path, directory))
        
        print(f"Stworzono archiwum: {archive_name}")
        print("Zawartość archiwum:", zip_file.namelist())

create_backup("C:/Users/julia/OneDrive/Pulpit/folder")  # Możesz zmienić ścieżkę na dowolny katalog

