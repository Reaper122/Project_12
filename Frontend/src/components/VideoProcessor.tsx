import React, { useState } from "react";
import axios from "axios";
import "./VideoProcessor.css";

interface ProcessResponse {
  video_filename: string;
  transcripts_path: string;
  summary_path: string;
  notes_path: string;
  mcqs_txt_path: string;
}

const VideoProcessor: React.FC = () => {
  const [url, setUrl] = useState("");
  const [response, setResponse] = useState<ProcessResponse | null>(null);
  const [error, setError] = useState("");
  const [fileContents, setFileContents] = useState<{ [key: string]: string }>(
    {}
  );

  const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
  };

  const handleProcess = async () => {
    try {
      const res = await axios.post<ProcessResponse>(
        "http://localhost:8000/process",
        { url_P: url }
      );
      setResponse(res.data);
      setError("");
      await fetchFileContents(res.data);
    } catch (err) {
      if (axios.isAxiosError(err)) {
        setError("Error: " + (err.response?.data.detail || err.message));
      } else {
        setError("An unexpected error occurred");
      }
    }
  };

  const fetchFileContents = async (data: ProcessResponse) => {
    try {
      const fileKeys: Array<keyof ProcessResponse> = [
        "transcripts_path",
        "summary_path",
        "notes_path",
        "mcqs_txt_path",
      ];
      const contents: { [key: string]: string } = {};
      for (const key of fileKeys) {
        const res = await axios.get(`http://localhost:8000/file/${data[key]}`, {
          responseType: "text",
        });
        contents[key] = res.data;
      }
      setFileContents(contents);
    } catch (err) {
      console.error("Error fetching file contents:", err);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Video Processor</h1>
      <div className="input-container">
        <input
          type="text"
          value={url}
          onChange={handleUrlChange}
          placeholder="Enter YouTube URL"
          className="input"
        />
        <button onClick={handleProcess} className="button">
          Process Video
        </button>
      </div>
      {error && <p className="error">{error}</p>}
      {response && (
        <div className="output-container">
          <p className="filename">Video Name: {response.video_filename}</p>
          <h2>Generated Files:</h2>
          <div className="file-content">
            <h3>Transcripts</h3>
            <pre className="preformatted">
              {fileContents["transcripts_path"]}
            </pre>
          </div>
          <div className="file-content">
            <h3>Summary</h3>
            <pre className="preformatted">{fileContents["summary_path"]}</pre>
          </div>
          <div className="file-content">
            <h3>Notes</h3>
            <pre className="preformatted">{fileContents["notes_path"]}</pre>
          </div>
          <div className="file-content">
            <h3>MCQs (Text)</h3>
            <pre className="preformatted">{fileContents["mcqs_txt_path"]}</pre>
          </div>
        </div>
      )}
    </div>
  );
};

export default VideoProcessor;
