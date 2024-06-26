import streamlit as st
import pandas as pd
import os
import shutil
import click

from Youtube_reader.youtube_reader2 import YouTubeDownloader
from Video_Transcriber2.video_transcriber import VideoTranscriber
from Summarizer2.summarize import TextSummarizer
from Note_Generator2.note_gen import NoteGenerator
from Mcq_Generator2.mcq_gen import MCQGenerator


st.title('Learning assistant; video transcriber; summarizer; mcq generator; notes generator ')

url = st.text_input("Enter a Youtube video link :")

downloader = YouTubeDownloader()
downloader.download_video_and_audio(url)

video_filename="your_video.mp4"
video_filename = downloader.download_video_and_audio(url)
video_path=""
if video_filename:
    print(f"Downloaded video filename: {video_filename}")
    video_path = os.path.join("downloads", video_filename)
    st.write("This is the video")
    st.video(video_path)

# Video Downloader
transcriber = VideoTranscriber()
transcriber.transcribe_video_in_chunks(video_path)

if video_filename:
    video_filename = video_filename.replace(".mp4", "") # Removing ".mp4"
    with open("transcripts/"+video_filename+".txt", "r") as file:
        text_content = file.read()
    
    st.title('Video Transcript :')
    st.write(text_content)

    # Summarizer
    summarizer = TextSummarizer()
    text_file_path = 'transcripts/'+video_filename+'.txt'
    summarizer.summarize_text_file(text_file_path)
    summary_text='transcripts/summary/'+video_filename+'_summary.txt'
    st.title("Summarize the Content :")
    csv_file="transcripts/summary/"+video_filename+"_summary.csv"
    data = pd.read_csv(csv_file)
    st.write(data)

    # Note Generator
    note_generator = NoteGenerator()
    note_generator.generate_notes_from_file(summary_text)
    csv_file="notes/"+video_filename+"_summary_notes.csv"
    data = pd.read_csv(csv_file)
    st.title('Note :')
    st.write(data)

    # Mcq Generator
    mcq_generator = MCQGenerator(summary_text)
    mcq_generator.generate_and_save_mcqs('mcqs.csv', 'mcqs.txt')
    data = pd.read_csv('mcqs.csv')
    st.title('MCQ :')
    st.write(data)

    # Delete extra folder used for streamlit
    shutil.rmtree('downloads')
    shutil.rmtree('transcripts')
    shutil.rmtree('notes')
