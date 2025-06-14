# downloader/asyncio_downloader.py

import os
import asyncio
import aiohttp
from tqdm.asyncio import tqdm
from .base import BaseDownloader
from .logger import Logger

class AsyncioDownloader(BaseDownloader):
    def __init__(self, urls, output_dir):
        super().__init__(urls, output_dir)
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = Logger(os.path.join(output_dir,"log.txt"))

    async def download_file(self, session, url):
        try:
            local_filename = os.path.join(self.output_dir, url.split("/")[-1])
            async with session.get(url) as response:
                response.raise_for_status()
                total = int(response.headers.get('content-length', 0))

                with open(local_filename, 'wb') as f, tqdm(
                    desc=local_filename,
                    total=total,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024
                ) as bar:
                    async for chunk in response.content.iter_chunked(1024):
                        f.write(chunk)
                        bar.update(len(chunk))
            self.logger.log(url, "success")
        except Exception as e:
            self.logger.log(url, "fail", f"({str(e)})")
            print(f"❌ Error downloading {url}: {e}")


    async def run(self):
        connector = aiohttp.TCPConnector(limit=10)
        timeout = aiohttp.ClientTimeout(total=60)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        async with aiohttp.ClientSession(connector=connector, timeout=timeout, headers=headers) as session:
            await asyncio.gather(*(self.download_file(session, url) for url in self.urls))


    def download(self):
        asyncio.run(self.run())
        print("✅ All async downloads completed.\n")
