from abc import ABC, abstractmethod
from typing import List


class BaseDownloader(ABC):
    def __init__(self, urls: List[str], output_dir: str):
        self.urls = urls
        self.output_dir = output_dir

    @abstractmethod
    def download(self):
        """Start the download process."""
        pass
