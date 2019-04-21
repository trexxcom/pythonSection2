import urllib.request as dw


imgUrl = "http://post.phinf.naver.net/20161017_243/1476630494401TkViK_PNG/IsL_L4lKWmaBl-EcXKVi948VReuk.jpg"
htmlURL = "http://google.com"
savePath1 = "/Users/trexx/Documents/4_developing/python/lecture/niceman/section2/text.jpg"
savePath2 = "/Users/trexx/Documents/4_developing/python/lecture/niceman/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
