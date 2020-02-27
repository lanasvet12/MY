from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
