from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from component.Youtube_reader.youtube_reader2 import YouTubeDownloader
from component.Video_Transcriber2.video_transcriber import VideoTranscriber
from component.Summarizer2.summarize import TextSummarizer
from component.Note_Generator2.note_gen import NoteGenerator
from component.Mcq_Generator2.mcq_gen import MCQGenerator

import pandas as pd
import shutil

app = FastAPI()

# Allowing CORS Headers
origins = ["http://localhost:3000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
# Global variable
var = {} # Dict

# Download video 
@app.post("/url")
async def url(url_P: str):
        try:
            downloader = YouTubeDownloader()
            downloader.download_video_and_audio(url_P)
            video_filename = downloader.download_video_and_audio(url_P)
            video_path = "downloads/"+video_filename
            var['video_filename'] = video_filename.replace(".mp4", "")
            var['video_path'] = video_path
            return {"message": "Video downloaded successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

@app.get('/get_transcriped')
async def get_transcriped():
    try:
        transcriber = VideoTranscriber()
        transcriber.transcribe_video_in_chunks(var['video_path'])
        print("/Video: Transcribe successfully") #Log message
        return {"message": "Transcribe successfully"}
    except Exception as e:
        # Handle errors 
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/get_summarized')
async def get_summarized():
    try:
        summarizer = TextSummarizer()
        var['transcripts_path'] = 'transcripts/'+var['video_filename']+'.txt'
        summarizer.summarize_text_file(var['transcripts_path'])
        var['summary_path'] = 'transcripts/summary/'+ var['video_filename'] +'_summary.txt'
        print("/Transciped: Summarized successfully") #Log message
        return {"message": "Summarized successfully"}
    except Exception as e:
        # Handle errors 
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/get_notes')
async def get_notes():
    try:
        note_generator = NoteGenerator()
        note_generator.generate_notes_from_file(var['transcripts_path'])
        print("/Transcriped: Generated Note") #Log message
        return {"message": "Generated Note"}
    except Exception as e:
        # Handle errors 
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/get_mcq')
async def get_mcq():
    try:
        mcq_generator = MCQGenerator(var['transcripts_path'])
        mcq_generator.generate_and_save_mcqs('mcqs.csv', 'mcqs.txt')
        print("/Transcripts: Generated Mcq successfully") #Log message
        return {"message": "Generated Mcq successfully"}
    except Exception as e:
        # Handle errors 
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/delete_folder')
async def delete_folder():
    try:
        shutil.rmtree('downloads')
        shutil.rmtree('transcripts')
        shutil.rmtree('notes')
        shutil.rmtree('mcqs.csv')
        shutil.rmtree('mcqs.txt')
        print("/Folder: Deleted successfully") #Log message
        return {"message": "Deleted successfully"}
    except Exception as e:
        # Handle errors 
        raise HTTPException(status_code=500, detail=str(e))