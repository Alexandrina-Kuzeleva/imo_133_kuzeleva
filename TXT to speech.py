import requests

def tts():
    iam_token = 't1.9euelZqXzoqax86anIubyJyTzY-Rz-3rnpWaypiTi83GyI2dj4uXzMeRxpjl9Pd_GDFV-e9VKWeI3fT3P0cuVfnvVSlniM3n9euelZqVnZXImo6czJiSmpOQz4mPzO_8xeuelZqVnZXImo6czJiSmpOQz4mPzA.7SdhmDwtuNEr1Nwvf5BDOmHl24MI4v1visU-Lw-1oIIFfQBKC7upcjCw8E0Dg8ivWQ_JTYCDY1vmSY_OancQAg'
    folder_id = 'b1gqevh6bpdtkql6e188'
    headers = {
        "Authorization": "Bearer " + iam_token
    }
    data = {
        "text": "Полный бак (Полный бак) Я заправил в свою тачку полный бак (Полный бак) Я заправил в твою сучку полный бак (Шлёп-шлёп) Хочешь чё-то мне сказать? Мне поебать Мне поебать (Как же мне похуй) Полный бак (Полный бак) Я заправил в свою тачку полный бак (Полный бак) Я заправил в твою сучку полный бак (Полный, воу) Хочешь чё-то мне сказать? Мне поебать (Пошёл нахуй) Мне поебать (Ты абобус) Как лицо не прячу, всё равно все узнают Вроде бы обычный парень, но в штанах несёт змею Я как Доминик Торетто, люблю тачки и семью Мои птички на кармане, мы уже летим на юг Хапнул за сутки полсотни мультов — называй меня Telegram Сунул твоей тати в рот, теперь она выглядит будто бы пеликан Со мной всегда мой кореш-циклоп, он одноглазый и великан (Ага) Ты хотел залить полный бак, но не нашёл бензобака у велика (Трр-ч) Тапку в пол, прыгаю в этот салон, как ковбой (Е) Год назад — уклон (Где?), а ты, сука, только палишь, как куколд (Ага) (Вау) Up'нул gold, я горю, как огонь (Шараут, skrrt) Сегодня они все глотают пыль за мной Заливаю полный бак, бак, бак, ба-ак Наливаю полный cup, cup, cup, cu-up Все не понимают: Как так? Как та-ак? Мечты за спиною: Плак-плак-плак Полный бак (Полный бак) Я заправил в свою тачку полный бак (Полный бак) Я заправил в твою сучку полный бак (Шлёп-шлёп) Хочешь чё-то мне сказать? Мне поебать Мне поебать (Как же мне похуй) Полный бак (Полный бак) Я заправил в свою тачку полный бак (Полный бак) Я заправил в твою сучку полный бак (Полный, воу) Хочешь чё-то мне сказать? Мне поебать (Пошёл нахуй) Мне поебать (Ты абобус)",
        "lang": "ru-RU",
        "voice": "filipp",
        "folderId": folder_id
    }
    response = requests.post("https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize", headers=headers, data=data)
    response_bytes = response.content
    with open("speech.ogg", "wb") as file:
        file.write(response_bytes)

if __name__ == "__main__":
    tts()
