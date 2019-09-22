import requests
from os import getenv
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from flask import Flask, escape, request

load_dotenv()

app = Flask(__name__, static_url_path='/', static_folder="static", template_folder="templates")

import routes

app.run(host="127.0.0.1", port=5000, threaded=True)
