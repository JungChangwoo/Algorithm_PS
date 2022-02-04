# [파이썬 웹 요청 예제: GET 방식]
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)

# [JSON 객체 사용 예제]
import json
user = {
  "id": "just",
  "password": "12345",
  "age": 30,
  "hobby": ["book", "programming"]
}
json_data = json.dumps(user, indent=4)
print(json_data)

# [JSON 객체 파일 저장]
import json
user = {
  "id": "just",
  "password": "12345",
  "age": 30,
  "hobby": ["book", "programming"]
}
# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
  json_data = json.dump(user, file, indent=4)

# [REST API를 호출하여 회원정보를 처리하는 예제]
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)
# 응답 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()
# 모든 사용자(user) 정보를 확인하여 이름 정보만 삽입
name_list = []
for user in data:
  name_list.append(user['name'])

print(name_list)

  