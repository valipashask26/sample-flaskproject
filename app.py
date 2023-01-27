from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the main page <h1>WELCOME</h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)





# python app.py
#python -m flask --app .\app.py run
