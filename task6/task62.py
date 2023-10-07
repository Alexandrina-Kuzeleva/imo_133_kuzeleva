import requests

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)
data = response.json()
with open("titles.txt", "w", encoding="utf-8") as file:
    for post in data:
        title = post["title"]
        file.write(title + "\n")
