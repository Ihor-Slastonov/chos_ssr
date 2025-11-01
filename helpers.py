import os
import json
import glob
import zipfile

CONFIG_FILE = "config.json"

def check_config():
    """Проверяет наличие config.json и возвращает сохраненный путь."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Возвращаем сохраненный путь или пустую строку, если его нет
                return config.get("user_saves_folder", "")
        except json.JSONDecodeError:
            # На случай, если файл поврежден
            return ""
    else:
        # Создаем конфиг с пустым путем, если его нет
        default_config = {
            "user_saves_folder": ""
        }
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4)
        return ""

def save_config(folder_path):
    """Сохраняет переданный путь к папке в config.json."""
    config = {
        "user_saves_folder": folder_path
    }
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

def zip_user_saves(folder_path):
    archive_name = "my_save_files.zip"
    extension_pattern = '*.sav'

    search_pattern = os.path.join(folder_path, extension_pattern)

    sav_files = glob.glob(search_pattern)

    if sav_files:
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            print(f"Создание архива: {archive_name}")
            for file_path in sav_files:
                # zipf.write(путь_к_файлу, имя_файла_внутри_архива)
                file_name = os.path.basename(file_path)
                zipf.write(file_path, file_name)
                print(f"  Добавлен: {file_name}")

        print('complete')
    else:
        print(f"Файлы с расширением {extension_pattern} в папке {folder_path} не найдены.")






