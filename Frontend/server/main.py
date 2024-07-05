from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from component.Youtube_reader.youtube_reader2 import YouTubeDownloader
from component.Video_Transcriber2.video_transcriber import VideoTranscriber
from component.Summarizer2.summarize import TextSummarizer
from component.Note_Generator2.note_gen import NoteGenerator
from component.Mcq_Generator2.mcq_gen import MCQGenerator
from fastapi.responses import FileResponse
import shutil

app = FastAPI()

origins = ["http://localhost:3000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

var = {}

class URLRequest(BaseModel):
    url_P: str

@app.post("/process")
async def process(request: URLRequest):
    try:
        # Step 1: Download video
        downloader = YouTubeDownloader()
        downloader.download_video_and_audio(request.url_P)
        video_filename = downloader.download_video_and_audio(request.url_P)
        video_path = "downloads/" + video_filename
        var['video_filename'] = video_filename.replace(".mp4", "")
        var['video_path'] = video_path

        # Step 2: Transcribe video
        transcriber = VideoTranscriber()
        transcriber.transcribe_video_in_chunks(var['video_path'])
        var['transcripts_path'] = 'transcripts/' + var['video_filename'] + '.txt'

        # Step 3: Summarize transcript
        summarizer = TextSummarizer()
        summarizer.summarize_text_file(var['transcripts_path'])
        var['summary_path'] = 'transcripts/summary/' + var['video_filename'] + '_summary.txt'

        # Step 4: Generate notes
        note_generator = NoteGenerator()
        note_generator.generate_notes_from_file(var['transcripts_path'])
        var['notes_path'] = 'notes/' + var['video_filename'] + '_notes.txt'

        # Step 5: Generate MCQs
        mcq_generator = MCQGenerator(var['transcripts_path'])
        mcq_generator.generate_and_save_mcqs('mcqs.csv', 'mcqs.txt')
        var['mcqs_csv_path'] = 'mcqs.csv'
        var['mcqs_txt_path'] = 'mcqs.txt'

        return {
            "video_filename": var['video_filename'],
            "transcripts_path": var['transcripts_path'],
            "summary_path": var['summary_path'],
            "notes_path": var['notes_path'],
            "mcqs_csv_path": var['mcqs_csv_path'],
            "mcqs_txt_path": var['mcqs_txt_path']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/file/{file_path:path}")
async def get_file(file_path: str):
    try:
        return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_path.split("/")[-1])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/delete_folder')
async def delete_folder():
    try:
        shutil.rmtree('downloads')
        shutil.rmtree('transcripts')
        shutil.rmtree('notes')
        shutil.rmtree('mcqs.csv')
        shutil.rmtree('mcqs.txt')
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
