import json

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    """Display all blog posts on the home page."""
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display the add-post form and create a new blog post."""
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        with open('blog.json', 'r') as file:
            blog_posts = json.load(file)

        new_id = max([post['id'] for post in blog_posts], default=0) + 1

        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        blog_posts.append(new_post)

        with open('blog.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')


def fetch_post_by_id(post_id):
    """Return a blog post with the given ID, or None if not found."""
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    for post in blog_posts:
        if post['id'] == post_id:
            return post

    return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Display the update form and update an existing blog post."""
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')

        with open('blog.json', 'r') as file:
            blog_posts = json.load(file)

        for index, blog_post in enumerate(blog_posts):
            if blog_post['id'] == post_id:
                blog_posts[index] = post
                break

        with open('blog.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Delete the blog post with the given ID."""
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    blog_posts = [post for post in blog_posts if post['id'] != post_id]

    with open('blog.json', 'w') as file:
        json.dump(blog_posts, file, indent=4)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)