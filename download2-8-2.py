from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

user = os.path.expanduser('~')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote

res = req.urlopen(url)
savePath = user + '/Documents/4_developing/python/lecture/niceman/downloads/imageDown/'

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.error != errono.EEXIST:
        print("폴더만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

imgList = soup.select("ul.slides")[0]

for i, e in enumerate(imgList,1):
    with open(savePath+"text_"+str(i)+".txt", "wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'], fullFileName)


print("다운로드 완료")
