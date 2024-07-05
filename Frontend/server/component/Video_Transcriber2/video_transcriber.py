import os
import csv
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

class VideoTranscriber:
    def __init__(self, download_path='./downloads/split_audio', transcript_path='./transcripts'):
        self.download_path = download_path
        self.transcript_path = transcript_path
        os.makedirs(self.download_path, exist_ok=True)
        os.makedirs(self.transcript_path, exist_ok=True)

    def extract_audio(self, video_path):
        try:
            video = VideoFileClip(video_path)
            audio_path = os.path.join(self.download_path, os.path.splitext(os.path.basename(video_path))[0] + '.wav')
            video.audio.write_audiofile(audio_path, codec='pcm_s16le')
            print(f"Audio extracted to: {audio_path}")
            return audio_path
        except Exception as e:
            print(f"Error extracting audio: {e}")
            return None

    def transcribe_audio(self, audio_path):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                print("Transcription completed.")
                return text
        except sr.RequestError as e:
            print(f"API request error: {e}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except Exception as e:
            print(f"Error transcribing audio: {e}")
        return None

    def save_transcript(self, text, filename):
        text_file_path = os.path.join(self.transcript_path, filename + '.txt')
        csv_file_path = os.path.join(self.transcript_path, filename + '.csv')

        # Save as text file
        try:
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)
            print(f"Transcript saved as text file: {text_file_path}")
        except Exception as e:
            print(f"Error saving text file: {e}")

        # Save as CSV file
        try:
            with open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Time', 'Text'])
                writer.writerow([0, text])
            print(f"Transcript saved as CSV file: {csv_file_path}")
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    def transcribe_video(self, video_path):
        audio_path = self.extract_audio(video_path)
        if audio_path:
            text = self.transcribe_audio(audio_path)
            if text:
                filename = os.path.splitext(os.path.basename(video_path))[0]
                self.save_transcript(text, filename)

    def split_audio(self, audio_path, chunk_length_ms=60000):
        audio = AudioSegment.from_wav(audio_path)
        chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
        chunk_paths = []
        for i, chunk in enumerate(chunks):
            chunk_path = os.path.join(self.download_path, f"{os.path.splitext(os.path.basename(audio_path))[0]}_chunk{i}.wav")
            chunk.export(chunk_path, format="wav")
            chunk_paths.append(chunk_path)
        return chunk_paths

    def transcribe_audio_chunks(self, audio_paths):
        recognizer = sr.Recognizer()
        full_text = ""
        for i, audio_path in enumerate(audio_paths):
            print(f"Transcribing chunk {i+1}/{len(audio_paths)}")
            try:
                with sr.AudioFile(audio_path) as source:
                    audio_data = recognizer.record(source)
                    text = recognizer.recognize_google(audio_data)
                    full_text += text + " "
            except sr.RequestError as e:
                print(f"API request error: {e}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except Exception as e:
                print(f"Error transcribing audio: {e}")
        return full_text

    def transcribe_video_in_chunks(self, video_path):
        audio_path = self.extract_audio(video_path)
        if audio_path:
            chunk_paths = self.split_audio(audio_path)
            full_text = self.transcribe_audio_chunks(chunk_paths)
            if full_text:
                filename = os.path.splitext(os.path.basename(video_path))[0]
                self.save_transcript(full_text, filename)

# Example usage:
# if __name__ == "__main__":
#     video_path = 'downloads/Generative AI in a Nutshell - how to survive and thrive in the age of AI_video.mp4'
#     transcriber = VideoTranscriber()
#     transcriber.transcribe_video_in_chunks(video_path)
