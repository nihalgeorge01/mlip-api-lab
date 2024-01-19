import requests

URL = "http://localhost:3000/api/v1/analysis/"
PARAMS = {"uri":"http://jeroen.github.io/images/testocr.png"}
r = requests.get(url = URL, json=PARAMS)
print(r.json())
