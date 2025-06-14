import argparse
import os

from downloader.threading_downloader import ThreadingDownloader
# from downloader.asyncio_downloader import AsyncioDownloader (for later)
# from downloader.multiprocessing_downloader import MultiprocessingDownloader (for later)


def load_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def main():
    parser = argparse.ArgumentParser(description="Concurrent Downloader CLI")
    parser.add_argument('--method', choices=['threading'], required=True, help='Concurrency method')
    parser.add_argument('--url-file', required=True, help='Path to file containing URLs (1 per line)')
    parser.add_argument('--output-dir', required=True, help='Directory to save downloaded files')

    args = parser.parse_args()

    urls = load_urls_from_file(args.url_file)

    if args.method == 'threading':
        downloader = ThreadingDownloader(urls, args.output_dir)
    else:
        raise ValueError("Unsupported method (yet)")

    downloader.download()


if __name__ == '__main__':
    main()
