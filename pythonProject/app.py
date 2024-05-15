from flask import Flask, render_template, url_for
app = Flask(__name__)
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