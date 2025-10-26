#!/usr/bin/env python
"""
Flickr OAuth Authentication Script

This script uses the flickrapi library to properly authenticate with Flickr
using OAuth 1.0a and saves the token for use with uploadr.py
"""

import flickrapi
import configparser
import os
import sys

# Read config from uploadr.ini
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(sys.argv[0]), "uploadr.ini"))
FLICKR = eval(config.get('Config', 'FLICKR'))
TOKEN_PATH = eval(config.get('Config', 'TOKEN_PATH'))

api_key = FLICKR["api_key"]
api_secret = FLICKR["secret"]

print("=" * 70)
print("Flickr OAuth Authentication")
print("=" * 70)
print()
print(f"API Key: {api_key}")
print(f"Token will be saved to: {TOKEN_PATH}")
print()
print("A browser window will open for you to authorize this application.")
print("After authorizing, the token will be automatically saved.")
print()
print("Starting authentication...")
print()

try:
    # Create FlickrAPI instance
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

    # Authenticate - this will open a browser window
    print("Authenticating...")
    flickr.authenticate_via_browser(perms='delete')

    # Get the token
    token = flickr.token_cache.token

    if token:
        # Extract just the token string (not the full object representation)
        if hasattr(token, 'token'):
            token_string = token.token
        else:
            token_string = str(token)

        # Ensure it's a string, not bytes
        if isinstance(token_string, bytes):
            token_string = token_string.decode('utf-8')

        # Save token to the same location uploadr.py expects
        with open(TOKEN_PATH, 'w') as f:
            f.write(token_string)

        print()
        print("=" * 70)
        print("SUCCESS! Authentication complete!")
        print("=" * 70)
        print(f"Token saved to: {TOKEN_PATH}")
        print()
        print("You can now run uploadr.py to upload your photos.")
        print()
    else:
        print("ERROR: Could not obtain token")
        sys.exit(1)

except Exception as e:
    print(f"ERROR: {str(e)}")
    print()
    print("If authentication failed, please check:")
    print("1. Your API key and secret in uploadr.ini")
    print("2. Your internet connection")
    print("3. That you authorized the app in the browser")
    sys.exit(1)
