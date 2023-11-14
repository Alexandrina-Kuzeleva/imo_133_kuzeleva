import requests

def tts():
    iam_token = 't1.9euelZqOyMzMmo2clMvHzMbLzpicmO3rnpWajJLJj83Pzo-SlMvKyZuVzZ7l8_dPfDBV-e8BMl5G_t3z9w8rLlX57wEyXkb-zef1656VmsvOiZfPm8mWnZqVj4-XlZiN7_zF656VmsvOiZfPm8mWnZqVj4-XlZiN.94-7e8sbq0GVkjHHtxZWL5txGd3UC4fIqPDWHnypbF6zIDPlaiJs_xgVfonaUWBl5qAglP2Slnfes33rVdL3BQ'
    folder_id = 'b1gh9vponl12f9in278r'
    headers = {
        "Authorization": "Bearer " + iam_token
    }
    data = {
        "text": "Вино и сигареты - это все, что нам осталось. Душить друг друга в ванной и снимать свою усталость. Мой сон - твои объятия, а мой космос - гематома. Впечатай меня в стену, чтобы я осталась дома. Я осталась дома, я осталась дома",
        "lang": "ru-RU",
        "voice": "filipp",
        "folderId": folder_id
    }
    response = requests.post("https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize", headers=headers, data=data)
    response_bytes = response.content
    with open("speech1.ogg", "wb") as file:
        file.write(response_bytes)

if __name__ == "__main__":
    tts()

