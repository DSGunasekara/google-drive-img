import json
import requests
headers = {"Authorization": "Bearer "}
para = {
    "name": "1.jpg",
    "parents": ["18u1tQm2tyqZTd8lqDuwY2X0pY5p6jitS"]
}
files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("/Users/dilain/Downloads/images/1.jpg", "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

para = {
    "name": "2.jpg",
    "parents": ["18u1tQm2tyqZTd8lqDuwY2X0pY5p6jitS"]
}
files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("/Users/dilain/Downloads/images/2.jpg", "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

para = {
    "name": "3.jpg",
    "parents": ["18u1tQm2tyqZTd8lqDuwY2X0pY5p6jitS"]
}
files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("/Users/dilain/Downloads/images/3.jpg", "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

para = {
    "name": "4.jpg",
    "parents": ["18u1tQm2tyqZTd8lqDuwY2X0pY5p6jitS"]
}
files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("/Users/dilain/Downloads/images/4.jpg", "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r)