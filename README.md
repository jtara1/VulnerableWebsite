# VulnerableWebsite
A simple website built with security flaws that will allow a client to run
arbitrary Python code on the server.

The intended purpose is to prettify (format) JSON so it's more readable.

Included in the scripts folder are some scripts to convert a file->bytes (text file)
and bytes (text file)->image.

Python 2 or 3 should work fine; there's only two required modules.

[Here's a video example of what a hacker can do with a website like this one.](https://www.youtube.com/watch?v=doCy8GAyhEQ&feature=youtu.be)

## Install

1. `git clone` or download this repo & `cd VulnerableWebsite`
2. `pip install -r requirements.txt`

## Run

`python run.py`
