from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    data = Post()
    data = data.get_data()
    return render_template("index.html", data=data)


@app.route('/post/<int:post_id>')
def post(post_id):
    data = Post()
    data = data.get_data()
    return render_template('post.html', post_id=post_id, data=data)


if __name__ == "__main__":
    app.run(debug=True)
