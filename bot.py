from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('4amhqNoNxD6PIejZgRDjA0RokbkkOss9A6KRiyeuQOTSBbGOYaNrLotpaPmQ9KKAIqTT3GyvWNypRQ0dZR0Rxd3ehn/vEu3uDIKU5W2V6WiWoxdrDw04HcRh0y7LU2fOdjmXJoC4Z9atZFo2i6D/xgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e74028b8fa4f4920f6c20f899359b4c9')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
if request.method == 'POST':

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
