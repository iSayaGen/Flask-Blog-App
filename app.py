from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Read the existing posts
        with open('blog.json', 'r') as file:
            blog_posts = json.load(file)

        # Generate a new unique ID
        new_id = max([post['id'] for post in blog_posts], default=0) + 1

        # Create the new blog post
        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        # Add the new post to the list
        blog_posts.append(new_post)

        # Save the updated list back to blog.json
        with open('blog.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')


def fetch_post_by_id(post_id):
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    for post in blog_posts:
        if post['id'] == post_id:
            return post

    return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        post['author'] = author
        post['title'] = title
        post['content'] = content

        with open('blog.json', 'r') as file:
            blog_posts = json.load(file)

        for i, blog_post in enumerate(blog_posts):
            if blog_post['id'] == post_id:
                blog_posts[i] = post
                break

        with open('blog.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    with open('blog.json', 'r') as file:
        blog_posts = json.load(file)

    blog_posts = [post for post in blog_posts if post['id'] != post_id]

    with open('blog.json', 'w') as file:
        json.dump(blog_posts, file, indent=4)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)