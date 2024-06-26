import os
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from moviepy.editor import *

class YouTubeDownloader:
    def __init__(self):
        self.download_path = './downloads'
        os.makedirs(self.download_path, exist_ok=True)
    
    def get_video_details(self, video_url):
        try:
            response = requests.get(video_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract video title
            title_tag = soup.find('meta', {'name': 'title'})
            title = title_tag['content'] if title_tag else 'N/A'
            
            # Extract video description
            description_tag = soup.find('meta', {'name': 'description'})
            description = description_tag['content'] if description_tag else 'N/A'
            
            # Extract view count
            view_count_tag = soup.find('meta', itemprop='interactionCount')
            views = view_count_tag['content'] if view_count_tag else 'N/A'
            
            # Extract likes and dislikes
            like_button = soup.select_one('button[aria-label*="like this video"]')
            dislike_button = soup.select_one('button[aria-label*="dislike this video"]')
            likes = like_button.text.strip().split(' ')[0] if like_button else 'N/A'
            dislikes = dislike_button.text.strip().split(' ')[0] if dislike_button else 'N/A'
            
            video_details = {
                'title': title,
                'description': description,
                'views': views,
                'likes': likes,
                'dislikes': dislikes
            }
            return video_details
        
        except Exception as e:
            print(f"Error fetching video details: {e}")
            return None

    def download_video_and_audio(self, video_url):
        try:
            yt = YouTube(video_url)
            
            # Get video details
            video_details = self.get_video_details(video_url)
            if video_details:
                print("Video Details:")
                for key, value in video_details.items():
                    print(f"{key.capitalize()}: {value}")
            
            # Download video
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if video_stream:
                video_filename = f"{yt.title}_video.mp4"
                video_path = video_stream.download(output_path=self.download_path, filename=video_filename)
                print(f"Video downloaded to: {video_path}")
                
                # Convert audio to MP3
                self.convert_audio_to_mp3(video_path)
                
            else:
                print("Failed to download video stream.")
            
        except Exception as e:
            print(f"Error: {e}")

    def convert_audio_to_mp3(self, video_path):
        try:
            video = VideoFileClip(video_path)
            audio = video.audio
            audio_filename = os.path.splitext(video_path)[0] + '.mp3'
            audio.write_audiofile(audio_filename, codec='libmp3lame')
            print(f'Audio converted to MP3 successfully: {audio_filename}')
        except Exception as e:
            print(f'Error converting audio to MP3: {e}')

# Example usage:
if __name__ == "__main__":
    downloader = YouTubeDownloader()
    video_url = 'https://www.youtube.com/watch?v=2IK3DFHRFfw'
    downloader.download_video_and_audio(video_url)
