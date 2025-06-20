# Concurrency-Project-CLI-Concurrent-Downloader
Hi! This is a big project from the topic Concurrency from my Software Architect and DevSecOps Engineer road map.

For the concurrency project, I'm creating a CLI (Command-line Interface) Concurrent Downloader to download data from such websites concurrently!

Follow instructions below the high level diagram or check how_to_use.txt in the repo.

Check out my benchmark and analysis comparing downloading using threading, asyncio, and multiprocessing of 10 URLS and 100 URLS in my Road Map Repo:

https://github.com/WillyPhan06/Software-Architect-and-DevSecOps-Engineer-Road-Map/tree/main/Concurrency/FinalProject.

Below is high level design of my CLI Concurrent Downloader!

![High Level Design of CLI Concurrent Downloader](high_level_CLI_concurrent_downloader_diagram.png)

**📘 HOW TO USE - Concurrent Downloader CLI Tool**
This project allows you to download multiple files concurrently using threading, asyncio, or multiprocessing in Python.

**✅ Requirements**
Python 3.10+

**Visual Studio Code (VS Code) is recommended**

**🧠 Step-by-Step Instructions**

**🔧 Step 0: Clone the Repository**
_Open VS Code_
_Press Ctrl + ~ to open the terminal_

_Navigate to a folder where you want to store the project:_
cd path/to/your/folder

_Clone the repo:_
git clone https://github.com/WillyPhan06/Concurrency-Project-CLI-Concurrent-Downloader.git

_Navigate into the project folder:_
cd Concurrency-Project-CLI-Concurrent-Downloader

**🐍 Step 1: Set Up Virtual Environment**
_Run the following command to create a virtual environment:_
python -m venv venv

_Activate the virtual environment:_

_On Windows (CMD):_
venv\Scripts\activate

_On Windows PowerShell (recommended if you are using terminal of VSCode in Window):_
.\venv\Scripts\Activate.ps1

_On Mac/Linux:_
source venv/bin/activate

_Install dependencies (if any are added in future):_
pip install -r requirements.txt

**🌐 Step 2: Edit urls.txt**
_Open urls.txt in VS Code._
_Add one URL per line that you want to download content from._

_Example:_
https://example.com/file1.jpg
https://example.com/file2.jpg

**📥 Step 3: Run the Downloader**
_Make sure you're in the main project folder (Concurrency-Project-CLI-Concurrent-Downloader)._

_Choose one of the following methods:_

_▶️ Download using Threading:_
python concurrent_downloader/main.py --method threading --url-file urls.txt --output-dir downloads

_▶️ Download using Asyncio:_
python concurrent_downloader/main.py --method asyncio --url-file urls.txt --output-dir downloads

_▶️ Download using Multiprocessing:_
python concurrent_downloader/main.py --method multiprocessing --url-file urls.txt --output-dir downloads

**⏳ Step 4: Wait for Completion**
_The terminal will show a "Done" message along with the total time taken._
_Progress and status will be printed while downloading._

**📁 Step 5: Check Your Downloads**
_All downloaded files will be saved inside the downloads/ folder._
_If you used threading or asyncio, a log.txt file will also be generated inside downloads/, containing detailed logs of the download process._

**💡 Tips**
_Make sure the URLs in urls.txt are valid and accessible._
_To restart, just clear downloads/ and re-run a method._




