
import os
import shutil
from datetime import datetime, timedelta

# Parametry
extensions = ['.txt', '.py'] 
search_dirs = ['./']  # Można dodać inne katalogi
backup_dir = 'Backup'

# Data sprzed 3 dni
three_days_ago = datetime.now() - timedelta(days=3)
today_str = datetime.now().strftime('%Y-%m-%d')
dest_dir = os.path.join(backup_dir, f'copy-{today_str}')


# Przeszukiwanie katalogów
for search_dir in search_dirs:
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
                if mtime > three_days_ago:
                    # Tworzenie struktury katalogów w kopii
                    relative_path = os.path.relpath(root, start=search_dir)
                    backup_path = os.path.join(dest_dir, relative_path)
                    os.makedirs(backup_path, exist_ok=True)
                    shutil.copy2(filepath, os.path.join(backup_path, file))

print(f'Pliki zostały skopiowane do {dest_dir}')

