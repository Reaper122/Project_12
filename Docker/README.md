# Learning Assistant Tool

## Overview

The Learning Assistant Tool is designed to automate various educational tasks using machine learning techniques. It integrates YouTube video downloading, transcription, summarization, note generation, and multiple-choice question (MCQ) generation. Below are the key components and techniques used in the tool:

## Components and Techniques

1. **YouTube Video Downloading and Audio Extraction**
   - Technique: Using the `YouTubeDownloader` class for video download and audio extraction.
   - Libraries: `pytube` for downloading YouTube videos.

2. **Video Transcription**
   - Technique: Transcribing video content to text using the `VideoTranscriber` class.
   - Model: Automatic Speech Recognition (ASR) model.

3. **Text Summarization**
   - Technique: Summarizing transcriptions with the `TextSummarizer` class.
   - Model: BART (Bidirectional and Auto-Regressive Transformers) for summarization.

4. **Note Generation**
   - Technique: Generating notes from summarized text using the `NoteGenerator` class.
   - Model: BART for condensing content into notes.

5. **MCQ Generation**
   - Technique: Creating multiple-choice questions from text with the `MCQGenerator` class.
   - NLP Techniques: Tokenization, POS tagging, and synonym extraction using NLTK.

## Integration with Streamlit

The tool is integrated with Streamlit, a web application framework, to provide a user-friendly interface. Users input a YouTube video link, and the tool processes the video to display the transcript, summary, notes, and MCQs.

## Intended Functionality

The tool aims to assist in educational content creation by automating transcription, summarization, note generation, and MCQ generation. It leverages ASR and NLP techniques along with pre-trained models like BART for efficient processing and content generation.

## Models and Improvements

- ASR Model: Utilizes Whisper or similar ASR models for accurate transcription.
- Summarization Model: Uses BART for summarizing text and generating notes.
- NLP Techniques: Employed for MCQ generation to identify key terms and create questions.

The tool enhances the efficiency of converting video content into structured educational material, providing a comprehensive learning assistant experience.

 
