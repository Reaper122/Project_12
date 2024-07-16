# Learning Assistant video transcriber, summarizer, mcq generator and notes generator

## Overview

The Video Processing Application is designed to streamline the process of extracting valuable information from YouTube videos. It performs the following tasks:
1. Downloads YouTube videos.
2. Transcribes the video audio to text.
3. Summarizes the transcribed text.
4. Generates notes from the transcript.
5. Creates multiple-choice questions (MCQs) based on the transcript.

## Technologies Used

- **Backend:** FastAPI
- **Frontend:** React
- **Containerization:** Docker, Docker Compose
- **NLP & ASR:** Various Python libraries for transcription, summarization, note generation, and MCQ generation
- **HTTP Client:** Axios (for frontend HTTP requests)

## Project Structure

### Backend

The backend, built with FastAPI, handles all the heavy lifting:
- **Video Downloading:** Uses a YouTube downloader library to download video and audio.
- **Transcription:** Utilizes Automatic Speech Recognition (ASR) to convert audio to text.
- **Summarization:** Applies Natural Language Processing (NLP) techniques to summarize the transcribed text.
- **Note Generation:** Chunks the transcript into smaller parts and summarizes each part.
- **MCQ Generation:** Generates multiple-choice questions using NLP for tokenization and synonym extraction.

### Frontend

The frontend, built with React, provides a user-friendly interface:
- **Input Handling:** React state management to handle user inputs.
- **HTTP Requests:** Axios for making HTTP requests to the backend.
- **Conditional Rendering:** Displays the results (transcripts, summaries, notes, MCQs) based on the state of the response.

### Containerization

Docker and Docker Compose are used to containerize and manage the application:
- **Dockerfiles:** Define the environment for both frontend and backend services.
- **Docker Compose:** Manages multi-container Docker applications, specifying services, ports, volumes, and dependencies.

## Running the Application

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Reaper122/Project_12.git
   ```

2. **Run Docker Compose:**
   ```bash
   docker-compose up -
   ```

3. **Access the Application:**
   - Frontend: `http://localhost:3000`
   - Backend API Documentation: `http://localhost:8000/docs`

## Documentation

For a detailed explanation of the project, including code snippets and a comprehensive overview of the implementation, refer to the [Documentation.md](Documentation.md) file.

## Credits

This project was developed by Prashant Bara under the guidance of Akshit, Anand, and Shivlok Sir.

## GitHub Repository

[GitHub Repository](https://github.com/Reaper122/Project_12)

