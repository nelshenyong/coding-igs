import asyncio
import aiohttp


async def get_100_pokemon_names(session):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100'
    async with session.get(url) as response:
        data = await response.json()
        return [pokemon['name'] for pokemon in data['results']]


async def get_pokemon_details(session, name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {'name': name, 'error': f'Status code {response.status}'}


async def main():
    async with aiohttp.ClientSession() as session:
        names = await get_100_pokemon_names(session)

      
        tasks = [get_pokemon_details(session, name) for name in names]
        all_details = await asyncio.gather(*tasks)


        for i, p in enumerate(all_details[:5], 1):
            print(f"{i}. {p['name'].title()} - Height: {p.get('height')} - Weight: {p.get('weight')}")


if __name__ == '__main__':
    asyncio.run(main())
