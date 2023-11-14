import requests
import json
import time

# https://cloud.yandex.ru/docs/iam/operations/api-key/create
apikey="AQVN2-87h-0OcAonnj5ux8A9PPVdGgKvRr6mbZFg" 

headersm = {    
    "Authorization": f"Api-Key {apikey}"
}


url = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"
oggcloud = "https://storage.yandexcloud.net/task/speech.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=YCAJE2soELmMxED0LswuxqgFl%2F20231114%2Fru-central1%2Fs3%2Faws4_request&X-Amz-Date=20231114T182354Z&X-Amz-Expires=3600&X-Amz-Signature=2A21307A5AE7FA304757D64ADC90FF3C2767E1D416A41C302523976592F98435&X-Amz-SignedHeaders=host"

request_body = {
            "config": {
                "specification": {
                    "audioEncoding": "MP3",
                    "languageCode": "ru-RU"
                }
            },
            "audio": {
                "uri": oggcloud
            }
        }

response = requests.post(url, headers=headersm, json=request_body)
print(response.content)
dataj = response.json()
opid=dataj['id']
print(opid)
time.sleep(20)
with open("outputya2.json", "wb") as file:
    file.write(response.content)

#get
urlres="https://operation.api.cloud.yandex.net/operations/"+opid
response = requests.get(urlres, headers=headersm)
res = response.json()
with open("output-ya4.json", "w", encoding="utf-8") as file:
    json.dump(res,file)

print("ok")    
