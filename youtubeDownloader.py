import pytube
import os
import subprocess

# 다운 받을 동영상 URL
# input으로 입력? 클립보드에서 가져오기
yt = pytube.YouTube("https://www.youtube.com/watch?v=jv2WJMVPQi8")
videos = yt.streams.all()

# print('videos',videos)

for i in range(len(videos)):
    print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력) "))

downDir = "/Users/trexx/Documents/4_developing/python/lecture/niceman/downloads"

videos[cNum].download(downDir)

newFileName = input("변환할 mp3 파일명은? ")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(downDir,oriFileName),
    os.path.join(downDir,newFileName)
])


print("동영상 다운루드 및 mp3 변환 완료!")
