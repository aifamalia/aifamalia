from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('wkyBePuiuu/Mjjv2EbS5TYG3HTZ9QUQScVnTHQh+8kbOX8kUcqqfeA0gvOWV7wwdmSSbdk5zY/5Qt7/EGi9qQXwY9jfcyPaKUQHAlMx6ZCmfTgq+3fNO7W1a1lAWCfIQtPqCKvZ5yAX6Ffo1HWR1UgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8fe23e19ac1155932d9175a98cbfe86b')


@app.route("/callback", methods=['POST'])
def callback():
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
