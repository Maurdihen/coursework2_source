from flask import Flask, render_template, request, jsonify
from utils import *
import logging

app = Flask(__name__, template_folder='templates')

logging.basicConfig(level=logging.INFO, filename='api.log', format='%(asctime)s [%(levelname)s] %(message)s')
# logger = logging.getLogger("one")
# handler = logging.FileHandler('api.log')
# formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# handler.setFormatter(formatter_one)
# logger.addHandler(handler)

@app.route('/')
def main_page():
    posts = get_posts_all()
    bookmarks = get_bookmarks()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<int:postid>')
def page_post(postid):
    posts = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', comments=comments, posts=posts)

@app.route('/search')
def search_page():
    s = request.args.get('s')
    posts = search_for_posts(s)
    return render_template('search.html', posts=posts)

@app.route('/users/<username>')
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.route('/api/posts')
def json_page():
    logging.info('Запрос /api/posts')
    return jsonify(get_posts_all())


@app.route('/api/posts/<int:post_id>')
def json_page_by_id(post_id):
    logging.info(f'Запрос /api/posts/{post_id}')
    return jsonify(get_post_by_pk(post_id))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Статус-код 404</h1><p>Такой странички не существует сори 😪</p>", 404

@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Статус-код 500</h1><p>Видимо ты где то в коде допустил ошибку, проверь ещё раз 😪</p>", 404

# @app.route('/tag/<tagname>')
# def user_page(tagname):
#     return render_template('tag.html', tagname=tagname)

# @app.route('/bookmarks')
# def user_page():
#     return render_template('bookmarks.html')
#
# @app.route('bookmarks/remove/postid')
# def user_page():
#     return render_template('bookmarks.html')
#
# @app.route('bookmarks/add/postid')
# def user_page():
#     return render_template('bookmarks.html')





if __name__ == "__main__":
    app.run()