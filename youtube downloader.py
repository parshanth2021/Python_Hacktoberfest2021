
from pytube import YouTube


YouTube("https://www.youtube.com/watch?v=aOlQhmyog7k").streams.first().download()
yt=YouTube("https://www.youtube.com/watch?v=aOlQhmyog7k")
yt.streams
save.filter(progressive=True, file_extension='mp4')
order_by('resolution')
desc()
first()
yt.download("C:/Users/hp/PycharmProjects/pythonProject2")

