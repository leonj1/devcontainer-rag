import httpx
import asyncio
from bs4 import BeautifulSoup

async def fetch_content(client, url):
    response = await client.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

async def fetch_all_contents(urls):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_content(client, url) for url in urls]
        return await asyncio.gather(*tasks)
