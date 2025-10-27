flickr-uploader
===============

Upload a directory of media to Flickr to use as a backup to your local storage.

**Python 3 Compatible** - This fork has been updated to work with Python 3 and uses OAuth 1.0a authentication.

Interested in helping manage pull requests and issues? I need one or more collaborators since I no longer actively use this script.
* trickortweak was kind enough to add me as a contributor to this repository.
* I will be maintaining it mostly to answer queries and to incorporate pull requests/changes from other contributors.
* I do more actively maintain this fork [flickr-uploader](https://github.com/oPromessa/flickr-uploader) also available [on pypi.org also](https://pypi.org/project/flickr-uploader/).


## Features:
* Uploads images in full resolution to Flickr account (JPG, PNG...)
* Reuploads modified images
* Removes images from Flickr when they are removed from your local hard drive
* Uploads videos (AVI, MOV, MPG, MP4, 3GP...)
* Stores image information locally using a simple SQLite database
* Creates "Albums" (Sets) based on the folder name the media is in (getting existing sets from Flickr is managed also)
* Ignores unwanted directories (like ".picasabackup" for Picasa users)
* Allows specific files to be ignored (via regular expressions)
* Convert RAW files (with an external tool)

THIS SCRIPT IS PROVIDED WITH NO WARRANTY WHATSOEVER. PLEASE REVIEW THE SOURCE CODE TO MAKE SURE IT WILL WORK FOR YOUR NEEDS. IF YOU FIND A BUG, PLEASE REPORT IT.

## Requirements:

* Python 3.7+ (Python 2 is no longer supported)
* `flickrapi` library (automatically installed with setup)
* File write access (for the token and local database)
* Flickr API key (free)

## Setup:

### 1. Install Dependencies

**Using uv (recommended):**
```bash
# Install dependencies from pyproject.toml
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

**Using pip (alternative):**
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install from requirements.txt
pip install -r requirements.txt

# Or install just the main library
pip install flickrapi
```

### 2. Get Flickr API Key
Go to http://www.flickr.com/services/apps/create/apply and apply for an API key

### 3. Configure uploadr.ini
Edit the following variables in the uploadr.ini:

* FILES_DIR = "/path/to/your/photos"
* FLICKR = {
        "title"                 : "",
        "description"           : "",
        "tags"                  : "auto-upload",
        "is_public"             : "0",
        "is_friend"             : "0",
        "is_family"             : "0",
        "api_key"               : "YourAPIKey",
        "secret"                : "YourSecret"
        }

Refer to https://www.flickr.com/services/api/upload.api.html for what each of the
upload arguments above correspond to for Flickr's API.

### 4. Authenticate with Flickr
**First time only:** Run the authentication script to get your OAuth token:
```bash
source .venv/bin/activate
python authenticate_flickr.py
```
This will open your browser to authorize the application. After authorization, the token will be saved automatically.

## Usage

### Basic Upload
```bash
source .venv/bin/activate
python uploadr.py
```

It will crawl through all the files from the FILES_DIR directory and begin the upload process.

**Note:** You can press **Ctrl+C** at any time to stop the upload gracefully. The script will exit immediately without processing remaining files.

**Album Organization:** Photos are automatically organized into Flickr albums based on their folder structure. For example:
```
/path/to/your/photos/
  ├── Vacation2024/    → Creates "Vacation2024" album
  ├── Family/          → Creates "Family" album
  └── Portfolio/       → Creates "Portfolio" album
```

### Dry Run
To check what files would be uploaded and deleted without actually doing it:
```bash
python uploadr.py --dry-run
```

### Remove Ignored Files
If you've changed the EXCLUDED_FOLDERS setting in your INI file and want to remove any previously uploaded files that are now ignored:
```bash
python uploadr.py --remove-ignored
```

## Changes in This Fork

* **Python 3 Support:** Fully migrated from Python 2 to Python 3
* **OAuth 1.0a Authentication:** Uses modern Flickr OAuth instead of deprecated auth methods
* **Simplified Authentication:** New `authenticate_flickr.py` script handles OAuth flow automatically
* **Album Organization:** Maintains folder-based album structure on Flickr
* **Bug Fixes:** Fixed various Python 3 compatibility issues (string/bytes handling, dictionary operations, etc.)

## Q&A
* Q: Who is this script designed for?
* A: Those people comfortable with the command line that want to backup their media on Flickr in full resolution.

* Q: Does this work with Python 2?
* A: No, this fork requires Python 3.7+. For Python 2 support, use the original repository.

* Q: Why OAuth?
* A: Flickr deprecated the old authentication method. OAuth 1.0a is now required for new API keys.

* Q: Is this script feature complete and fully tested?
* A: It's a work in progress. Core functionality (upload, album creation, file management) is tested and working.

* Q: How to automate it with a Synology NAS?
* A: First authenticate once via SSH to get the token file. Then create a scheduled task in DSM that runs: `"/path/to/python3 /path/to/uploadr.py"`. Make sure Python 3 is installed via the Package Center or SynoCommunity.
