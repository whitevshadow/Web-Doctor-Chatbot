from bardapi import BardCookies


def chatbot_res(msg):
    cookie_dict = {
        "__Secure-1PSID": "bAjBzMPa1LnBnghntZ4HXKI4gDbZ2m1jyusTXnRaeVtyvvQxyf2XjjJpCZYmsa7ipB4dEQ.",
        "__Secure-1PSIDTS": "sidts-CjIB3e41hRvSzb_xguKKZ_maIcJma_eT93ynqtjC58vPwe_LJ3U3PWE--VZQ897JP1aH9hAA",
        # Any cookie values you want to pass session object.
    }

    bard1 = BardCookies(cookie_dict=cookie_dict)
    addon = "few lines Answer"

    input_text = msg + addon
    response = (bard1.get_answer(input_text)['content'])

    return response


print(chatbot_res("My name is Anish"))