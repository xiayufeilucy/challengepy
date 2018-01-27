from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to PennClubReview!"

@app.route('/api')
def api():
    return "Welcome to the PennClubReview API!."

if __name__ == '__main__':
    app.run()