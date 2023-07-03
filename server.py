from flask import Flask, request, jsonify
from translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french():
    data = request.get_json()
    text = data.get('text')
    translation = english_to_french(text)
    return jsonify({'translation': translation})

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english():
    data = request.get_json()
    text = data.get('text')
    translation = french_to_english(text)
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run()