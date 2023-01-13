import json


def get_posts_all():
    with open('data/posts.json', 'r+', encoding='utf-8') as posts:
        posts = json.load(posts)
    for post in posts:
        content = post['content'].split()
        for i in content:
            if '#' in i:
                index = content.index(i)
                content[index] = f'<a href="/tag/{i[1:]}">{i}</a>'
        post['content'] = ' '.join(content)
    return posts

def get_comments_all():
    with open('data/comments.json', 'r', encoding='utf-8') as comments:
        return json.load(comments)


def get_posts_by_user(user_name):
    list_post = []
    for post in get_posts_all():
        if user_name in post['poster_name']:
            list_post.append(post)
    if len(list_post) == 0:
        raise ValueError
    elif not 'content' in set(list_post[0].keys()):
        return []
    return list_post


def get_comments_by_post_id(post_id):
    list_comment = []
    cnt = False
    for comment in get_comments_all():
        if post_id == comment['post_id']:
            list_comment.append(comment)
    for i in get_posts_all():
        if post_id == i['pk']:
            cnt = True
    if not cnt:
        raise ValueError
    elif len(list_comment) == 0:
        return []
    return list_comment


def search_for_posts(query):
    list_post = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            list_post.append(post)
    return list_post


def get_post_by_pk(pk):
    return [i for i in get_posts_all() if pk == i['pk']][0]

def get_bookmarks():
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_tag(tag_name):
    return f'<a href="/tag/{tag_name}">#{tag_name}</a>'

print(get_posts_all())