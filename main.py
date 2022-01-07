import pafy

z = input("url : ")
url = z


video = pafy.new(url)
streams = video.streams

for i in streams:
    print(i)
    
best=video.getbest()
best.download()