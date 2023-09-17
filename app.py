from bardapi import BardCookies


def chatbot_response(msg):
    try:
        cookie_dict = {
            "__Secure-1PSID": "bAjBzMPa1LnBnghntZ4HXKI4gDbZ2m1jyusTXnRaeVtyvvQxyf2XjjJpCZYmsa7ipB4dEQ.",
            "__Secure-1PSIDTS": "sidts-CjIB3e41hRvSzb_xguKKZ_maIcJma_eT93ynqtjC58vPwe_LJ3U3PWE--VZQ897JP1aH9hAA",
            # Any cookie values you want to pass session object.
        }

        bard = BardCookies(cookie_dict=cookie_dict)

        input_text = msg + "in 10 lines"
        res = (bard.get_answer(input_text)['content'])
        return res

    except:
        res_err = "Sorry the Server has been Disconnected" + "\n We will soon be Connected"
        return res_err


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()
