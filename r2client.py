import boto3

R2_ACCESS_KEY_ID = 'ddf182dbcfe6e26f95506e1d3b2260db'
R2_SECRET_ACCESS_KEY = '5853a0ea58130715145e830301c3f467708a3a5e11c4517656b06cdd579a9aa4'
R2_ENDPOINT_URL = 'https://9f6ea06c6fb4f78c8a3fbe9bc3bef9ef.r2.cloudflarestorage.com'

BUCKET_NAME = 'savegames'

s3_client = boto3.client(
    service_name='s3',
    endpoint_url=R2_ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY
)





def r2_upload(file_path, archive_name, log_func, ):
    log_func(file_path, archive_name)
    try:
        log_func("start uploading")
        s3_client.upload_file(
            Filename=archive_name,
            Bucket=BUCKET_NAME,
            Key=archive_name
        )
    except Exception as e:
        print(e)
    finally:
        log_func("Ура бля я загрузил обновления")


def r2_download(full_local_path, archive_name, log_func):
    log_func(f"Попытка скачать файл '{archive_name}' в '{full_local_path}'")

    try:
        log_func("Начало скачивания...")

        # --- Ключевое изменение: используем download_file ---
        s3_client.download_file(
            Bucket=BUCKET_NAME,  # Имя корзины (Bucket)
            Key=archive_name,  # Имя файла в хранилище (Key)
            Filename=full_local_path  # Локальный путь, куда сохранить файл (Filename)
        )
        # ----------------------------------------------------

    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")
        # Вы можете добавить здесь log_func для более подробного логирования ошибки

    finally:
        # Ваше фирменное сообщение! 😉
        log_func("Ура! Я скачал обновления.")
