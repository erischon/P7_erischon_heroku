from flask import Flask, render_template, request, jsonify

from .main import GrandPy
from .config import Config

app = Flask(__name__)

config = Config()
app.config['SECRET_KEY'] = config.SECRET_KEY


@app.route('/')
def index():
    config = Config()
    GKEY_F = config.GKEY_F
    return render_template('index.html', gkey=GKEY_F)


@app.route('/livesearch', methods=['GET', 'POST'])
def livesearch():
    searchbox = request.form.get("text")
    grandpy = GrandPy()
    result = grandpy.main(searchbox)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
