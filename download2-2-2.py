import urllib.request as dw


imgUrl = "http://post.phinf.naver.net/20161017_243/1476630494401TkViK_PNG/IsL_L4lKWmaBl-EcXKVi948VReuk.jpg"
htmlURL = "http://google.com"

savePath1 = "/Users/trexx/Documents/4_developing/python/lecture/niceman/section2/text.jpg"
savePath2 = "/Users/trexx/Documents/4_developing/python/lecture/niceman/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a: add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
