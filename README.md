# Flask Blog

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3\&logoColor=white)

A simple blog application built with Flask and JSON storage. The project supports creating, viewing, updating, and deleting blog posts.

## Features

* View all blog posts
* Add new posts
* Update existing posts
* Delete posts
* JSON-based data storage

## Running Locally

```bash
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Project Structure

```text
flask-blog/
├── app.py
├── blog.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
└── static/
    └── style.css
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
