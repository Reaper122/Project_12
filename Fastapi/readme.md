# Video Processing API

This FastAPI application provides endpoints for video processing tasks, including downloading videos from YouTube, transcribing videos, summarizing transcripts, generating notes, and creating multiple-choice questions (MCQs).

## Endpoints

1. **Download Video from YouTube**
   - **Endpoint**: `POST /url`
   - **Parameters**: `url_P` (string) - YouTube video URL
   - **Description**: Downloads the video and audio from the provided YouTube URL.

2. **Transcribe Video**
   - **Endpoint**: `GET /get_transcriped`
   - **Description**: Transcribes the downloaded video into text chunks.

3. **Summarize Transcripts**
   - **Endpoint**: `GET /get_summarized`
   - **Description**: Generates a summary of the transcribed text.

4. **Generate Notes**
   - **Endpoint**: `GET /get_notes`
   - **Description**: Creates notes from the transcribed text.

5. **Generate MCQs**
   - **Endpoint**: `GET /get_mcq`
   - **Description**: Generates multiple-choice questions based on the transcribed content.

6. **Delete Folders**
   - **Endpoint**: `GET /delete_folder`
   - **Description**: Deletes temporary folders used for processing.

## Usage
1. Start the FastAPI server.
2. Use the provided endpoints to perform video processing tasks.

## CORS Configuration
- The application allows requests from `http://localhost:3000` and all origins (`*`).

## Dependencies
- Requires the following components:
  - `YouTubeDownloader` for video download
  - `VideoTranscriber` for transcription
  - `TextSummarizer` for summarization
  - `NoteGenerator` for note generation
  - `MCQGenerator` for MCQ creation

## Cleanup
- Use the `/delete_folder` endpoint to remove temporary files and folders.
