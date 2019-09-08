from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

if __name__ == '__main__':
    app.run()
