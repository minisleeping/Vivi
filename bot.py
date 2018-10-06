from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('zBSXkKQNXKTM8jbLTLO2KxyeYJKO8J8KG5ONungzu1IDzv5GA3bT0DznUYbgEvwPIqTT3GyvWNypRQ0dZR0Rxd3ehn/vEu3uDIKU5W2V6WioPpcJYYHmjIthKyyIQb5t3LbPXeNVWqlFh1CihpHw/AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e74028b8fa4f4920f6c20f899359b4c9')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
