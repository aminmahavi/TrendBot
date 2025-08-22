from googleapiclient.discovery import build
from deep_translator import GoogleTranslator
from pytube import YouTube

YOUTUBE_API_KEY = "AIzaSyDhxsHocknUtE8pf8-akAnfQw8JmNakOu0"
YOUTUBE_API_SERVICE = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_trending_videos(region_code="US", max_results=5):
    youtube = build(YOUTUBE_API_SERVICE, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

    # گرفتن لیست ویدیوهای ترند
    request = youtube.videos().list(
        part="snippet,statistics,status",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for video in response.get("items", []):
        title = video["snippet"]["title"]
        views = int(video["statistics"]["viewCount"])
        video_id = video["id"]
        license_type = video["status"].get("license", "")
        videos.append((title, views, video_id, license_type))

    # مرتب سازی
    videos.sort(key=lambda x: x[1], reverse=True)

    # نمایش و دانلود Creative Commons
    for title, views, video_id, license_type in videos:
        fa_title = GoogleTranslator(source='en', target='fa').translate(title)
        print(f"{fa_title} — {views:,} بازدید — مجوز: {license_type}")

        if license_type.lower() == "creativecommon":
            print("دانلود ویدئو...")
            url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            stream.download(output_path="downloads")
            print("✅ ویدیو در پوشه downloads ذخیره شد")
        else:
            print("❌ این ویدیو مجوز Creative Commons ندارد")

if __name__ == "__main__":
    get_trending_videos()
