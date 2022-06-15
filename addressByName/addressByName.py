from config import *
import requests as r

def geckoIdByName(name:str):
    response = r.get(API_URL + f"/search?query={name}")
    if response:
        data = response.json()
        if len(data['coins']) == 0:
            ValueError("Could not find coin \"{name}\"")
        else:
            return data['coins'][0]['id']
    else:
        ValueError(f"Something wrong with response\n{response.status_code}\n{response.text}")

def platformsById(id:str):
    response = r.get(API_URL + f"/coins/{id}")
    if response:
        data = response.json()
        try:
            return data["platforms"]
        except:
            ValueError(f"Could not find coin with the given id: {id}")
    else:
        ValueError(f"Something wrong with response\n{response.status_code}\n{response.text}")

if __name__ == '__main__':
    print(geckoIdByName("ethereum"))
    print(platformsById("pancakeswap-token"))