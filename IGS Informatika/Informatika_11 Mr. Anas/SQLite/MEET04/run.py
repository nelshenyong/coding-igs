# import requests
import aiohttp
import asyncio
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

BASE_URL = "http://localhost:5000/players"

# def get_all_players():
#     response = requests.get(BASE_URL)
#     print("Status:", response.status_code)
#     print("Data", response.json())
    
# def get_player_by_id(player_id):
#     response = requests.get(f"{BASE_URL}/{player_id}")
#     print("Status:", response.status_code)
#     print("Data", response.json())

# def create_player(player):
#     payload = {
#         "name": "John Doe",
#         "age": 25,
#         "games_played": 10,
#         "highest_score": 1200,
#         "current_score": 300
#     }
#     response = requests.post(BASE_URL, json=payload)
#     print("Status:", response.status_code)
#     print("Data", response.json())
    
# def update_player(player_id):
#     payload = {
#         "current_score": 450
#     }
#     response = requests.patch(f"{BASE_URL}/{player_id}", json=payload)
#     print("Status:", response.status_code)
#     print("Data", response.json())
    
# def delete_player(player_id):
#     response = requests.delete(f"{BASE_URL}/{player_id}")
#     print("Status:", response.status_code)
#     print("Data", response.json())

async def get_all_players():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("Data", data)

async def get_player_by_id(player_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/{player_id}") as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("Data", data)

async def create_player():
    async with aiohttp.ClientSession() as session:
        payload = {
            "name": "John Doe",
            "age": 25,
            "games_played": 10,
            "highest_score": 1200,
            "current_score": 300
        }
        async with session.post(BASE_URL, json=payload) as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("Data", data)

async def update_player(player_id):
    async with aiohttp.ClientSession() as session:
        payload = {
            "current_score": 450
        }
        async with session.patch(f"{BASE_URL}/{player_id}", json=payload) as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("Data", data)

async def delete_player(player_id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{BASE_URL}/{player_id}") as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("Data", data)

async def main():
    await get_all_players()
    await get_player_by_id(1)
    # await create_player()
    # await update_player(1)
    # await delete_player(1)

if __name__ == "__main__":
    asyncio.run(main())
    # get_all_players()
    # get_player_by_id(1)
    # create_player()
    # update_player(1)
    # delete_player(1)
