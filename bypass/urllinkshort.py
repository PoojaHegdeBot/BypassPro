import requests
from bs4 import BeautifulSoup
import time

def bypass_urllinkshort(url):
    try:
        session = requests.Session()
        headers = {"User-Agent": "Mozilla/5.0"}
        res = session.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        final_btn = soup.find("a", attrs={"id": "redirect"})
        if final_btn:
            return final_btn.get("href")
        time.sleep(3)
        if res.url != url:
            return res.url
    except Exception as e:
        return f"Error: {str(e)}"
    return "Bypass failed."
