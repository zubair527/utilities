import urllib
from bs4 import BeautifulSoup
import requests


r  = requests.get("https://web.stanford.edu/class/cs357/")
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    file_link = link.get('href')
    try:
        if file_link.endswith('pdf') or \
                file_link.endswith('ppt') or \
                file_link.endswith('zip') or file_link.endswith('doc'):
            file_name = file_link.replace('/','-')
            if ("http" or "https") not in file_link:
                print('https://web.stanford.edu/class/cs357/'+file_link)
                urllib.request.urlretrieve('https://web.stanford.edu/class/cs357/'+file_link, file_name)
            else:
                print(file_link)
                urllib.request.urlretrieve(file_link, file_name)
    except Exception as e:
        print(e)



