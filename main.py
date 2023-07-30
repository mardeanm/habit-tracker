import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# neccessites for accessing pixela to graph progess

username = os.environ["USERNAME"]
token = os.environ["TOKEN"]
user_url = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# User creation on Pixela
# https://pixe.la/@mardean
# response=requests.post(url=user_url,json=user_params)
# print(response.text)

# create a new graph on Pixela
graph_url = "https://pixe.la/v1/users/a-know/graphs"
graph_id = "graph2"
graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "sora"

}

headers = {
    "X-USER-TOKEN": token
}
# reponse=requests.post(url=graph_url, )
graph_endpoint = f"{user_url}/{username}/graphs"

# create the graph
# response = requests.post(url=graph_endpoint, json= graph_config, headers=headers)
# print(response.text)

# add a pixel to the graph in today's date
pixel_endpoint = f"{user_url}/{username}/graphs/{graph_id}"
today = datetime.date.today()
today = today.strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": input("How many hours of coding did you do today?")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
