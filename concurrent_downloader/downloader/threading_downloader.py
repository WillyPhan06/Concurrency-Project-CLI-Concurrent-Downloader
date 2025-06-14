import os
import threading
import requests
from tqdm import tqdm
from .base import BaseDownloader

class ThreadingDownloader(BaseDownloader):
    def __init__(self, urls, output_dir):
        super().__init__(urls, output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def download_file(self, url):
        try:
            local_filename = os.path.join(self.output_dir, url.split("/")[-1])
            response = requests.get(url, stream=True)
            total = int(response.headers.get('content-length', 0))
            with open(local_filename, 'wb') as f, tqdm(
                desc=local_filename,
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024
            ) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")

    def download(self):
        threads = []
        for url in self.urls:
            thread = threading.Thread(target=self.download_file, args=(url,))
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()
        print("✅ All downloads completed.\n")
