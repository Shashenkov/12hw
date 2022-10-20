from flask import Blueprint, render_template, request
import logging

from main.utils import *
from exeptions import *

""" Создаём main_blueprint для показывания фото."""
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


@main_blueprint.route("/")
def main_page():
    """ Вывод формы на главной странице при обращении к / + логгинг. """
    logging.info("Открытие главной страницы.")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    """ Поиск и вывод постов при обращении на /search/?s=<ключ поиска> """
    s = request.args.get("s", "")
    logging.info("поиск...")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Файл не открывается"
    filtered_posts = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)
