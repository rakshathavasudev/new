from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.gsmarena.com/nokia_8_sirocco-review-1772.php")

soup=BeautifulSoup(r.text,"html.parser")

release=soup.find("img", {"alt":"Nokia 8 Sirocco review"})

print(release.text)