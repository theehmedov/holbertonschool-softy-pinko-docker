from flask import Flask
from flask_cors import CORS # CORS dəstəyini əlavə edin

app = Flask(__name__)
CORS(app) # CORS-u tətbiqdə aktivləşdirin

@app.route('/api/hello') # Marşrutu /api/hello olaraq dəyişin
def hello_world():
    # Sadə string cavabı
    return 'Hello, World!'

if __name__ == '__main__':
    # Portu 5252 olaraq dəyişin
    app.run(host='0.0.0.0', port=5252)
