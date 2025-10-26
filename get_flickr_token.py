#!/usr/bin/env python
"""
Manual Flickr OAuth 1.0a Token Generator

This script helps you obtain a Flickr OAuth token manually.
Follow the instructions printed by this script.
"""

import hashlib
import webbrowser
import configparser
import os
import sys

# Read config
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(sys.argv[0]), "uploadr.ini"))
FLICKR = eval(config.get('Config', 'FLICKR'))
TOKEN_PATH = eval(config.get('Config', 'TOKEN_PATH'))

api_key = FLICKR["api_key"]
secret = FLICKR["secret"]

print("=" * 70)
print("Flickr OAuth 1.0a Token Generator")
print("=" * 70)
print()
print("Since Flickr has deprecated the old auth API web interface,")
print("you need to use the new OAuth flow to get your token.")
print()
print("Follow these steps:")
print()
print("1. Go to this URL in your browser:")
print()
oauth_url = f"https://www.flickr.com/services/oauth/authorize?oauth_token=REQUEST_TOKEN&perms=delete"
print(f"   https://www.flickr.com/services/oauth/request_token")
print()
print("2. Since the old frob-based auth no longer works via web browser,")
print("   you have TWO options:")
print()
print("   OPTION A: Use flickrapi Python library (RECOMMENDED)")
print("   ---------------------------------------------------------")
print("   Install the library:")
print("       source .venv/bin/activate")
print("       uv pip install flickrapi")
print()
print("   Then run this authentication script:")
print("       python -c \"")
print("import flickrapi")
print(f"api_key = '{api_key}'")
print(f"api_secret = '{secret}'")
print("flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')")
print("flickr.authenticate_via_browser(perms='delete')")
print("print('Token:', flickr.token_cache.token)")
print("       \"")
print()
print("   OPTION B: Use Flickr App Garden (Manual)")
print("   ---------------------------------------------------------")
print("   1. Go to https://www.flickr.com/services/apps/by/me")
print("   2. Click on your app (or create a new one)")
print("   3. Click 'Authenticate' link")
print("   4. Follow the OAuth flow in browser")
print("   5. Copy the token from the success page")
print()
print(f"   Then save it to: {TOKEN_PATH}")
print()
print("=" * 70)
