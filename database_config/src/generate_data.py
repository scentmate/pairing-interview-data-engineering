import math
import random
import asyncio
import aiohttp
import aiofiles
from tenacity import retry

MAX = 1000
MIN = 0

@retry
async def get_entry(id):
    async with aiohttp.ClientSession() as session:
            async with session.get('https://san-random-words.vercel.app/') as response:
                
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                data = await response.json()
    
    data = data.pop()
    definition = data.get('definition').replace("'"," ")
    insert_data = (
        "INSERT INTO fragrances(fragrance_id, name, description, cost, forbidden) "
        f"VALUES({id},'{data.get('word')}','{definition}', {random.randint(0,100)}, 'f');\n"
    )

    print(insert_data)

    async with aiofiles.open('data.sql', mode='a') as f:
        await f.write(insert_data)
        

async def gen_data(entries=10000):

    tasks = []
    for i in range(entries):
        tasks.append(
            get_entry(i)
        )

    await asyncio.gather(*tasks)

if __name__ == "__main__":

    entries = input("How many entries do you want to create?")
    try:
        entries = int(entries)
    except Exception as e: 
        print(f"WARNING: Ensure you entered a valid number!!!!")
        raise e

    
    if entries < MIN and entries > MAX:
        print(f"Entries should be larger than {MIN} and smaller than {MAX}")
    else:
        asyncio.run(
            gen_data(entries)
        )
    