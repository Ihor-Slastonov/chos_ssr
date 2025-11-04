import os
import json
import glob
import sys
import zipfile
import time
import subprocess

CONFIG_FILE = "config.json"
archive_name = "my_save_files.zip"
extension_pattern = '*.sav'


def check_config():
    """Проверяет наличие config.json и возвращает сохраненный путь."""
    default_values = {
        "user_saves_folder": "",
        "user_extension": ""
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Возвращаем сохраненный путь или пустую строку, если его нет
                return {
                    "user_saves_folder": config.get("user_saves_folder", ""),
                    "user_extension": config.get("user_extension", "")
                }
        except json.JSONDecodeError:
            # На случай, если файл поврежден или отсутсвует
            pass
    else:
        # Создаем конфиг с пустым путем, если его нет

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_values, f, indent=4)
        return default_values


def save_config(folder_path,extension, log_func):
    """Сохраняет переданный путь к папке в config.json."""
    config = {
        "user_saves_folder": folder_path,
        "user_extension": extension
    }
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    log_func(f"Новый путь и расширения сохранены Битчес:")
    log_func(f"Папка: {folder_path}")
    log_func(f"Расширение: {extension if extension != "" else 'БЛЯ НАПЕЧАТАЙ РАСШИРЕНИЕ ФАЙЛОВ'}")


def zip_user_saves(folder_path, extension, log_func):
    if not extension or not extension.startswith("."):
        log_func("Не найдено файлы с расширением .Н И Х У Я")
        return
    search_pattern = os.path.join(folder_path, f'*{extension}')

    sav_files = glob.glob(search_pattern)

    if sav_files:
        try:
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                log_func(f"Создание архива: {archive_name}")
                file_count = len(sav_files)
                for file_path in sav_files:
                    time.sleep(0.1)
                    # zipf.write(путь_к_файлу, имя_файла_внутри_архива)
                    file_name = os.path.basename(file_path)
                    zipf.write(file_path, file_name)
                    log_func(f"  Добавлен: {file_name}")

            log_func(f'Успешно отпитонил в зипуху, вот столько: {file_count}')
        except Exception as e:
            log_func(f"Ошибка при создании архива: {e}", is_error=True)
    else:
        log_func(f"Файлы с расширением {extension} в папке {folder_path} не найдены.", is_error=True)


def unzip_user_saves(folder_path, log_func):
    if not folder_path or not os.path.isdir(folder_path):
        log_func("Не допустим путь к папке, выбери бля нормально")
        return
    if os.path.exists(archive_name):
        try:
            with zipfile.ZipFile(archive_name, 'r') as zipf:
                zipf.extractall(folder_path)
                log_func(f"Распаковка завершена! Файлы извлечены в: {folder_path}")
        except Exception as e:
            log_func(f"Ошибка при распаковке: {e}", is_error=True)
    else:
        log_func(f"Ошибка: Архив {archive_name} не найден. Убедитесь, что он находится рядом с программой.",
                 is_error=True)


def open_user_saves(folder_path, log_func):
    if not folder_path or not os.path.isdir(folder_path):
        log_func("Ты бля на приколе? Бро", is_error=True)
        return

    try:
        if os.name == "nt": #Windows
            os.startfile(folder_path)
        else:
            log_func('Не понимаю шо за ОП', is_error=True)
            return
    except Exception as e:
        log_func(f"Ошибка при открытии папки: {e}", is_error=True)