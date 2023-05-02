from Heema import *
from pytube import YouTube
import requests


root=create_window(text="BumBum Downloader")


paste_url_text=label(root,text="Paste the url here")
paste_url_text.config(font=("Segoe UI",16))
paste_url_text.pack(pady=10)
url_box=Entry(root,font=("Segoe UI",16),width=60)
url_box.pack(pady=30)


def download_video():
    global url_box
    url =  url_box.get()
    my_video= YouTube(url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    

def genereate_download_link():
    global url_box
    download_page=menu_page("Your video")
    url =  url_box.get() 
    my_video= YouTube(url)
    image_url = my_video.thumbnail_url
    r = requests.get(image_url) # create HTTP response object
    thumbnail_image_name="thumnail"
    thumbnail_image_name=thumbnail_image_name+".png"
    with open(thumbnail_image_name,'wb') as f:
        f.write(r.content)
    thumbnail_image=create_image(download_page,path=thumbnail_image_name,size=(450,300))
    thumbnail_image.pack(pady=10)
    title_label=label(download_page,text="Your Video")
    title_label.config(font=("Segoe UI",13))
    title_label.pack(pady=10)
    download_now=button4(download_page, text="Download now", command=download_video)
    download_now.pack(pady=10,ipadx=50)

get_video_btn=button5(frame_name=root, text="Generate download link", command=genereate_download_link)
get_video_btn.config(font=("Segoe UI",10))
get_video_btn.pack(pady=30)

root.mainloop()
