import requests
import data
from bs4 import BeautifulSoup
url = "http://localhost:8000/create"


def generateCsrfToken():
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    inputs = soup.find_all('input')
    for input in inputs:
        if input.get("name") == "csrfmiddlewaretoken":
            return input.get("value")
        


def generateData():
    nameData = data.generateNames()
    return {
    "csrfmiddlewaretoken":"H6RWXvsuOt5zttJa334Wauq9QQ5hyHXjRFRctUwVkRPcga6Iz2CF1GOf3jsfqo6w",
    "firstname":nameData['firstname'],
    "lastname":nameData['lastname'],
    "username":nameData['username'],
    "age":data.generateAge(),
    "gender":data.generateGender(),
    "permissionLevel":data.generatePermissionLevel(),
    "email":data.generateEmail(),
    "height":data.generateHeight(),
    "weight":data.generateWeight(),
    "nickname":nameData['nickname'],
    "bio":data.generateBio(),
    "bloodGroup":data.generateBloodGroup()
}
headers = {
  'Cookie': 'csrftoken=kJaqGzeBGyUNXRxIG9IT1mygnDx82Rjn'
}
for i in range(200):
    response = requests.post(url,data=generateData(),headers=headers)
    print(f"[+] {response.status_code}",end="  ")
    print(response.text)