from pytube import YouTube
from flask import Flask, render_template, request, send_file, flash
import os

path = "/storage/emulated/0/flask_web_app"

def downloader(request):
  url = request.form['url']
  choice = request.form['choice']
  
  yt = YouTube(url)
  title = yt.title
  print(title)
  thumbnail = yt.thumbnail_url
  stream = yt.streams.get_by_resolution("360p")
  stream.download()
  print("downloaded")
  return thumbnail
    
def download_audio():
  pass

def download_video():
  pass
'''
get_by_resolution("360p")
#resolution (str) – Video resolution i.e. “720p”, “480p”, “360p”, “240p”, “144p”
'''