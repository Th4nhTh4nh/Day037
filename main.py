import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "afasdqwrngdaf4n8asjf",
    "username": "thanhthanh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/graph1"

graph_config = {
    "id": "graph1",
    "name": "My Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

header = {"X-USER-TOKEN": user_params["token"]}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


graph_post_pixel = {
    "date": "20230820",
    "quantity": "10",
}

response = requests.post(url=graph_endpoint, json=graph_post_pixel, headers=header)
print(response.text)
