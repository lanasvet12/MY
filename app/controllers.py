from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
@app.route("/home")
def home():
    return render_template("home.html")
