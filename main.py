from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "This is all there is ... for now."

if __name__ == '__main__':
    app.run()