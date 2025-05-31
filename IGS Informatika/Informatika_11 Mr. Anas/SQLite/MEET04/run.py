import aiohttp
import asyncio

BASE_URL = "https://pokeapi.co/api/v2"

async def get_pokemon_list(limit=100):
    """Fetch a list of first 100 Pokemon"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/pokemon?limit={limit}") as resp:
            print(f"Status: {resp.status}")
            if resp.status == 200:
                data = await resp.json()
                print(f"Total Pokemon loaded: {len(data['results'])}")
                print("\nComplete Pokemon List:")
                for i, pokemon in enumerate(data['results'], 1):
                    print(f"{i}. {pokemon['name']}")
            else:
                print(f"Error fetching Pokemon list: {resp.status}")

async def get_pokemon_by_id(pokemon_id):
    """Fetch details of a specific Pokemon by ID"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/pokemon/{pokemon_id}") as resp:
            print(f"Status: {resp.status}")
            if resp.status == 200:
                data = await resp.json()
                print(f"Pokemon Details:")
                print(f"Name: {data['name']}")
                print(f"ID: {data['id']}")
                print(f"Height: {data['height']}")
                print(f"Weight: {data['weight']}")
                print(f"Types: {', '.join([t['type']['name'] for t in data['types']])}")
                print(f"Abilities: {', '.join([a['ability']['name'] for a in data['abilities']])}")
            else:
                print(f"Error fetching Pokemon #{pokemon_id}: {resp.status}")

async def main():
    print("--- Fetching Pokemon List ---")
    await get_pokemon_list(100)
    
    print("\n--- Fetching Pokemon Details ---")
    # Get Pikachu (ID: 25)
    await get_pokemon_by_id(25)

if __name__ == "__main__":
    asyncio.run(main())