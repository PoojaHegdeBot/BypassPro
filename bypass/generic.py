import requests
from bs4 import BeautifulSoup
import re

def generic_bypass(url):
    try:
        session = requests.Session()
        res = session.get(url, timeout=10, allow_redirects=True)
        soup = BeautifulSoup(res.text, "html.parser")
        meta = soup.find("meta", attrs={"http-equiv": "refresh"})
        if meta and "url=" in meta.get("content", ""):
            return meta["content"].split("url=")[1]
        if res.url != url:
            return res.url
        matches = re.findall(r'https?://[^\s"\']+', res.text)
        for m in matches:
            if get_domain(m) not in url:
                return m
    except Exception as e:
        return f"Error: {str(e)}"
    return "Bypass failed."
