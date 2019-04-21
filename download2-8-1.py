from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
from os.path import expanduser
import os

# 네이버 보안 설정
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

user = expanduser('~')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아이유")
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

imgList = soup.select("div.img_area > a.thumb._thumb > img")

for i, imgList in enumerate(imgList,1):
    # print(imgList['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(imgList['data-source'], fullFileName)


print("다운로드 완료")
