#!/usr/bin/env python

from image_dl import download_file, download_album
import os
import sys

"""
Run commands:
    python grab.py <url> <name>
"""

def grab(url, name):
    
    if not url.startswith("http://"):
        url = "http://www.imagebam.com/gallery/" + url

    if "imgbox.com" in url:
        host = "imgbox"
    elif "imagebam.com" in url:
        host = "imagebam"
    elif "imagevenue.com" in url:
        host = "imagevenue"
    else:
        print("unknonw host:" + url)
        sys.exit(1)

    dest = os.path.join("/Users/francois/Downloads/images-hosts", name)
    download_album(host, url, name, dest, delim="_")


if __name__ == "__main__":
    if (len(sys.argv) > 2) :
        grab(sys.argv[1], sys.argv[2])
    else:
        grab(sys.argv[1], sys.argv[1])
