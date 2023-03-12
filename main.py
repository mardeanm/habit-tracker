import requests
username="mardean"
token="asldkjasd213"
user_url="https://pixe.la/v1/users"
user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#User creation on Pixela
# https://pixe.la/@mardean
# response=requests.post(url=user_url,json=user_params)
# print(response.text)

#create a new graph on Pixela
graph_url="https://pixe.la/v1/users/a-know/graphs"
graph_config={
    "token":token,
    "username":username,
    "id":"graph1",
    "name": "Coding Graph",
    "unit":"hours",

}
reponse=requests.post(url=graph_url, )