**FastAPI Application Documentation**

This FastAPI application is a comprehensive system designed to process YouTube videos and generate various outputs, including transcripts, summaries, notes, and multiple-choice questions (MCQs). Let's break down the components and features:

1. **YouTube Downloader**

   - Downloads video and audio from YouTube.
   - Saves video and audio files to the downloads directory.

2. **Video Transcriber**

   - Transcribes video content into text using speech recognition.
   - Saves the transcript to a text file in the transcripts directory.

3. **Text Summarizer**

   - Summarizes lengthy text into a shorter form.
   - Saves the summary to a text file in the transcripts/summary directory.

4. **Note Generator**

   - Generates concise notes from text.
   - Saves the notes to a text file in the notes directory.

5. **MCQ Generator**

   - Creates multiple-choice questions based on the content.
   - Saves MCQs to both a CSV file and a text file in the mcqs directory.

6. **FastAPI Application**
   - Provides a RESTful API for processing YouTube videos.
   - Utilizes the components mentioned above to perform the tasks.

**API Endpoints:**

- `/process`

  - Method: POST
  - Request Body: `URLRequest` (contains a `url_P` field for the YouTube video URL)
  - Response: JSON object with file paths for the video, transcript, summary, notes, and MCQs.

- `/file/{file_path:path}`

  - Method: GET
  - Path Parameter: `file_path` (path to the file to be downloaded)
  - Response: File download with the specified file path.

- `/delete_folder`
  - Method: GET
  - Response: JSON object with a success message or an error message.

**Models:**

- `URLRequest`
  - `url_P` (str): YouTube video URL.

**Dockerfile:**
This Dockerfile creates a Docker image for the FastAPI application. Here are the instructions:

```Dockerfile
FROM python:3.10-slim
WORKDIR /usr/app
COPY . /usr/app/
RUN pip install fastapi uvicorn -r /usr/app/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**Build and Run:**
To build the Docker image:

```
docker build -t myapp .
```

To run the Docker container:

```
docker run -p 8000:8000 myapp
```

This will start the application on port 8000. You can access it by visiting [http://localhost:8000](http://localhost:8000) in your web browser¹².

Source:
(1) FastAPI - tiangolo. https://fastapi.tiangolo.com/.
(2) Document a FastAPI App with OpenAPI | Linode Docs. https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/.
(3) DevDocs — FastAPI documentation. https://devdocs.io/fastapi/.
(4) Home - FastAPI Tutorial. https://fastapi-tutorial.readthedocs.io/en/latest/.
(5) Tutorial - User Guide - FastAPI - tiangolo. https://fastapi.tiangolo.com/tutorial/.
