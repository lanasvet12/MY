from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
@app.route("/about)
def about():
    return render_template("about.html")
