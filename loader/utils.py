import json

from main.views import UPLOAD_FOLDER, POST_PATH
from exeptions import *


def pic_save(picture):
    """Функция сохранения картинки с проверкой формата."""
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.lower().split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgFile(f"Неверный формат файла! Допустимы {', '.join(allowed_type)}")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    """Запись поста в json-файл всех постов."""
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)
