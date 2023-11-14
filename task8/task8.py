import urllib.request
import json

FOLDER_ID = "b1gh9vponl12f9in278r" # Идентификатор каталога
IAM_TOKEN = "t1.9euelZrOy8eRlpqLicjJyJGMkp7Mi-3rnpWajJLJj83Pzo-SlMvKyZuVzZ7l8_cveA9W-e9eFFwX_d3z928mDVb5714UXBf9zef1656Vms2Zzcidj5KWlZnNx43Oz83N7_zF656Vms2Zzcidj5KWlZnNx43Oz83N.5hukB6eIJmyHIvPCrqestEaecNO3134fc9RKPKp-TPmG4LGFgn1WlZiz7fFqEQsVTRMz0s_z0bIBTgP9FjomAw" # IAM-токен

with open("speech.ogg", "rb") as f:
    data = f.read()

params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])

url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
# Аутентификация через IAM-токен.
url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

responseData = urllib.request.urlopen(url).read().decode('UTF-8')
decodedData = json.loads(responseData)

if decodedData.get("error_code") is None:
    print(decodedData.get("result"))
