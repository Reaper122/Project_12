API Endpoints
Download Video
Endpoint: /url
Method: POST
Description: Downloads a YouTube video and saves it locally.
Request Parameter:
url_P (str): The URL of the YouTube video.
Response: {"message": "Video downloaded successfully"}
Transcribe Video
Endpoint: /get_transcriped
Method: GET
Description: Transcribes the downloaded video.
Response: {"message": "Transcribe successfully"}
Summarize Transcript
Endpoint: /get_summarized
Method: GET
Description: Summarizes the transcript of the video.
Response: {"message": "Summarized successfully"}
Generate Notes
Endpoint: /get_notes
Method: GET
Description: Generates notes from the transcript.
Response: {"message": "Generated Note"}
Generate MCQs
Endpoint: /get_mcq
Method: GET
Description: Generates MCQs from the transcript.
Response: {"message": "Generated Mcq successfully"}
Delete Folders
Endpoint: /delete_folder
Method: GET
Description: Deletes the download, transcript, notes, and MCQ files.
Response: {"message": "Deleted successfully"}
