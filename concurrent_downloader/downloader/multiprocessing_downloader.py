# downloader/multiprocessing_downloader.py
import time
import os
import requests
from tqdm import tqdm
from multiprocessing import Pool
from .base import BaseDownloader


def download_file_multiprocess(args):
    url, output_dir = args
    filename = os.path.join(output_dir, url.split("/")[-1])

    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total = int(response.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=filename,
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            leave=False
        ) as bar:
            for chunk in response.iter_content(1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
        return f"SUCCESS - {url}"
    except Exception as e:
        return f"FAIL - {url} ({e})"


class MultiprocessingDownloader(BaseDownloader):
    def __init__(self, urls, output_dir):
        super().__init__(urls, output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def download(self):
        start = time.time()
        print("🚀 Starting multiprocessing downloads...\n")
        with Pool(processes=4) as pool:  # Adjust based on your CPU
            results = pool.map(download_file_multiprocess, [(url, self.output_dir) for url in self.urls])

        for result in results:
            print(result)
        print("✅ All multiprocessing downloads completed.\n")
        print(f"✅ All took total of {time.time() - start:.2f} seconds")
