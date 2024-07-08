import instaloader
import yt_dlp

def downloader(link):
    
    if  link.find("instagram") == 12:

        # To create an instance of the IG API.
        ig_api = instaloader.Instaloader()

        # This gets the video's unique identifier.
        shortcode = link.split("/")[-2]

        # This is for downloading the reel.
        post = instaloader.Post.from_shortcode(ig_api.context, shortcode)
        ig_api.download_post(post, target="Reels")
    
    elif link.find("tiktok") == 12:

        # Set the options for downloading the best quality video.
        ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': r'C:\Users\johan\TG_BOT\TikToks\%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
        }

        # To download the video.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    
    elif link.find("youtube") == 12:
        
        # Set the options for downloading the best quality video.
        ydl_opts = {

            'format': 'bestvideo[height<=1980]+bestaudio/best[height<=1080]',
            'outtmpl': r'C:\Users\johan\tg_bot\Youtube Videos\%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        # To download the video.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    else:
        # Set the options for downloading the best quality video.
        ydl_opts = {

            'format': 'bestvideo[height<=1980]+bestaudio/best[height<=1080]',
            'outtmpl': r'C:\Users\johan\tg_bot\General Videos\%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        # To download the video.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

# Menu to enter a link.
link = str(input("Introduzca el link del video que desea descargar: "))
downloader(link)