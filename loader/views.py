from flask import Blueprint, render_template, request, abort
import logging
from main.utils import load_json_data
from loader.utils import *


"""Блюпринт для загрузки фото."""
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def create_new_post_page():
    """Страничка "добавить пост" при обращении к GET /post"""
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    """Принимаем данные, проверяем, записываем, выводим."""
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.error("Отсутствует часть данных")
        return "Ошибка загрузки. Отсутствует часть данных"
    posts = load_json_data(POST_PATH)

    try:
        new_post = {"pic": pic_save(picture), "content": content}
    except WrongImgFile:
        abort(400)

    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)


