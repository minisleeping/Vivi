from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
if request.method == 'POST':
    return 'OK'
    
if __name__ == "__main__":
    app.run()
