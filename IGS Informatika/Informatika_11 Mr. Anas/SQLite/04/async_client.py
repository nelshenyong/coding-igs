import aiohttp
import asyncio

BASE_URL = "http://127.0.0.1:5000/players"

async def get_all_players():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as resp:
            print("Status:", resp.status)
            data = await resp.json()
            print("All Players:", data)

async def get_player_by_id(player_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/{player_id}") as resp:
            print(f"Status (GET ID {player_id}):", resp.status)
            data = await resp.json()
            print("Player Data:", data)

async def create_player():
    payload = {
        "name": "Prince",
        "age": 1000,
        "games_played": 100,
        "highest_score": 10000,
        "current_score": 5000
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(BASE_URL, json=payload) as resp:
            print("Status (POST):", resp.status)
            data = await resp.json()
            print("Created Player:", data)

async def update_player(player_id):
    payload = {
        "current_score": 450
    }
    async with aiohttp.ClientSession() as session:
        async with session.patch(f"{BASE_URL}/{player_id}", json=payload) as resp:
            print(f"Status (PATCH ID {player_id}):", resp.status)
            data = await resp.json()
            print("Updated Player:", data)

async def delete_player(player_id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{BASE_URL}/{player_id}") as resp:
            print(f"Status (DELETE ID {player_id}):", resp.status)
            data = await resp.json()
            print("Deleted Player:", data)

async def main():
    #await create_player()
    await get_all_players()
    await get_player_by_id(2)
    #await update_player(1)
    #await delete_player(1)
    #await get_all_players()

if __name__ == "__main__":
    asyncio.run(main())
