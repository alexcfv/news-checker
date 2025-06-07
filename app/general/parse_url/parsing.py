import app
import aiohttp
import ssl
import certifi
from bs4 import BeautifulSoup

class_names = ['article-body', 'article-text', 'article__body', 'article__text']

async def fetch_content(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            if response.status != 200:
                return app.error_message

            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            title = soup.find('h1')
            if title:
                title = title.text.strip()
        
            article_tag = soup.find('article')
            
            if article_tag:
                paragraphs = article_tag.find_all('p')
            else:
                for i in class_names:
                    container = soup.find('div', class_=i)
                    paragraphs = container.find_all('p') if container else []
                    
                    if paragraphs:
                        break

            content = '\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            
            if content != True and title:
                return title
            
            elif content:
                return content
            
            else:
                return app.error_message