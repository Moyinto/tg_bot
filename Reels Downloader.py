import instaloader
import pyktok as pyk
import yt_dlp

# Function to download Instagram reels.          
def quireel(reel_url):

    # To create an instance of the IG API.
    ig_api = instaloader.Instaloader()

    # This gets the video's unique identifier.
    shortcode = reel_url.split("/")[-2]

    # This is for downloading the reel.
    post = instaloader.Post.from_shortcode(ig_api.context, shortcode)
    ig_api.download_post(post, target="Quireels")

# Function to download TikTok videos.
def tikitokos(tiktok_url):

    # To specify the browser that Pyktok will use.
    pyk.specify_browser("chrome")

    # To download the TikTok
    pyk.save_tiktok(tiktok_url, True, "data.csv")

# Function to download Youtube videos.
def yt_videos(yt_url):

    # Set the options for downloading the best quality video.
    ydl_opts = {

        'format': 'bestvideo[height<=1980]+bestaudio/best[height<=1080]',
        'outtmpl': r'C:\Users\johan\tg_bot\Youtube Videos\%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    # To download the video.
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
    
# Menu to specify what the script will download.
select = int(input("Instagram (1), TikTok (2), Youtube (3): "))

if select == 1:
    reel_url = str(input("Link: "))
    quireel(reel_url)

elif select == 2:
    tiktok_url = str(input("Link: " ))
    tikitokos(tiktok_url)
elif select == 3:
    yt_url = str(input("Link: " ))
    yt_videos(yt_url)
else:
    print("Wtf que pasó")