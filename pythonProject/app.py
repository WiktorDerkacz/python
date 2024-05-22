from flask import Flask, render_template, url_for
from pip._internal.vcs import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./python')
    origin = repo.remotes.origin
    repo.create_head('main',
    origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '',200

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return app.send_static_file('about.html')
@app.route('/gallery')
def gallery():
    return app.send_static_file('gallery.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')