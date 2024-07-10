import instaloader
import yt_dlp

def downloader(link):
    
    # Downloads Instagram Reels.
    if  link.find("instagram") == 12:

        # To create an instance of the IG API.
        ig_api = instaloader.Instaloader()

        # This gets the video's unique identifier.
        shortcode = link.split("/")[-2]

        # This is for downloading the reel.
        post = instaloader.Post.from_shortcode(ig_api.context, shortcode)
        ig_api.download_post(post, target="Reels")
    
    # Downloads TikToks from TikTok.
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
    
    # Download YouTube videos and audios.
    elif link.find("youtube") == 12:

        option = int(input("Video (1) or Audio (2): "))

        if option == 1:

            # Set the options for downloading the best quality video.
            ydl_opts = {

                'format': 'bestvideo[height<=1980]+bestaudio/best[height<=1080]',
                'outtmpl': r'C:\Users\johan\TG_BOT\Youtube\Videos\%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
            }
        elif option == 2:
            # Set the options for downloading the best quality audio.
             ydl_opts = {

                'format': 'bestaudio/best',
                'outtmpl': r'C:\Users\johan\TG_BOT\Youtube\Audio\%(title)s.%(ext)s',
                'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '322',
            },
            {
                'key': 'FFmpegMetadata',
            },
            {
                'key': 'EmbedThumbnail',
            }
            ],
                'writethumbnail': True,
            }
        else:
            print("Invalid option.")

        # To download the video.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    
    # Downloads a video from another website.
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