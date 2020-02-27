from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
@app.route("/home)
def home():
    return render_template("home.html")
@app.route("/about)
def about():
    return render_template("about.html")
