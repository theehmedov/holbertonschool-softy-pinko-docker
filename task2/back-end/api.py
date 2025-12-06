# task2/back-end/api.py

from flask import Flask, jsonify

app = Flask(__name__)

# Sadə bir API marşrutu
@app.route('/', methods=['GET'])
def hello_world():
    # JSON formatında cavab qaytarın
    return jsonify({"message": "Hello, World!"})

# Tətbiqi işə salmaq üçün
if __name__ == '__main__':
    # Flask tətbiqini bütün interfeyslərdə (0.0.0.0) və standart portda (5000) işə salın
    app.run(host='0.0.0.0', port=5000)
