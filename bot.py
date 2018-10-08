from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
import xlrd 

app = Flask(__name__)

line_bot_api = LineBotApi('4amhqNoNxD6PIejZgRDjA0RokbkkOss9A6KRiyeuQOTSBbGOYaNrLotpaPmQ9KKAIqTT3GyvWNypRQ0dZR0Rxd3ehn/vEu3uDIKU5W2V6WiWoxdrDw04HcRh0y7LU2fOdjmXJoC4Z9atZFo2i6D/xgdB04t89/1O/w1cDnyilFU=')
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

def find_inExcel(Value, col, path):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        if str(row_value[col]).startswith(Value):
            return row_value

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    soruser = eval(str(event.source))
    for key, value in soruser.items():
        if key == 'userId':
            iduser = value
    if event.message.text.upper() == 'GETID':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=iduser))
    if find_inExcel(iduser, 0,"user.xlsx") != None:
        if find_inExcel(event.message.text, 1,"testdatabase.xlsx") != None:
            row_value = find_inExcel(event.message.text, 1,"testdatabase.xlsx")
            backtext = str(row_value[2]) + ' ราคา = ' + str(row_value[4]) + ' บาท'
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=backtext))


if __name__ == "__main__":
    app.run()
