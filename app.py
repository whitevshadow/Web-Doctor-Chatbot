from bardapi import BardCookies


def Worq_Hat(msg):
    # This is a sample code to get you started
    # You can access the advanced code and other parameters at https://docs.worqhat.com
    import requests

    url = "https://api.worqhat.com/api/ai/content/v2"

    API_KEY = "sk-ad7ebf9190d44e948133e8880bd985b4"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "question": msg,
        "randomness": 0.4
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        resp_bot = (response.json())
        content = resp_bot["content"]
        return content
    else:
        error = ("Error:", response.text)
        return error


def Bard(msg):
    try:
        cookie_dict = {
            "__Secure-1PSID": "bAjBzMPa1LnBnghntZ4HXKI4gDbZ2m1jyusTXnRaeVtyvvQxyf2XjjJpCZYmsa7ipB4dEQ.",
            "__Secure-1PSIDTS": "sidts-CjIB3e41hRvSzb_xguKKZ_maIcJma_eT93ynqtjC58vPwe_LJ3U3PWE--VZQ897JP1aH9hAA",
        }

        bard = BardCookies(cookie_dict=cookie_dict)

        input_text = msg + "in 10 lines"
        res = (bard.get_answer(input_text)['content'])
        return res

    except:
        res_err = "Sorry the Server has been Disconnected" + "\n We will soon be Connected"
        return res_err


def chatbot_response(msg):
    try:
        print("Response from Worq Hat")
        worq = Worq_Hat(msg)
        return worq

    except:
        print("Response from Bard")
        # Bard(msg)
        bard = Bard(msg)
        return bard


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
