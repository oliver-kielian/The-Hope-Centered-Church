from flask import Flask, render_template, request, redirect, send_from_directory, url_for, jsonify


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'mycoolawesomekey'

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

if __name__ == '__main__':
     app.run(debug=True)