import os
import csv
from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name='facebook/bart-large-cnn', chunk_size=512, summary_length=150, transcript_path='./transcripts/summary'):
        self.summarizer = pipeline('summarization', model=model_name)
        self.chunk_size = chunk_size
        self.summary_length = summary_length
        self.transcript_path = transcript_path
        os.makedirs(self.transcript_path, exist_ok=True)

    def load_text(self, text_file_path):
        try:
            with open(text_file_path, 'r') as file:
                text = file.read()
            print(f"Loaded text from {text_file_path}")
            return text
        except Exception as e:
            print(f"Error loading text file: {e}")
            return None

    def split_text(self, text):
        words = text.split()
        chunks = [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]
        return chunks

    def summarize_text(self, text):
        try:
            summary = self.summarizer(text, max_length=self.summary_length, min_length=int(self.summary_length / 2), do_sample=False)
            summarized_text = summary[0]['summary_text']
            return summarized_text
        except Exception as e:
            print(f"Error summarizing text: {e}")
            return None

    def save_summary(self, original_text, summary, filename):
        text_file_path = os.path.join(self.transcript_path, filename + '_summary.txt')
        csv_file_path = os.path.join(self.transcript_path, filename + '_summary.csv')

        # Save as text file
        try:
            with open(text_file_path, 'w') as text_file:
                text_file.write(summary)
            print(f"Summary saved as text file: {text_file_path}")
        except Exception as e:
            print(f"Error saving text file: {e}")

        # Save as CSV file
        try:
            with open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Original Text', 'Summary'])
                writer.writerow([original_text, summary])
            print(f"Summary saved as CSV file: {csv_file_path}")
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    def summarize_text_file(self, text_file_path):
        text = self.load_text(text_file_path)
        if text:
            chunks = self.split_text(text)
            summarized_chunks = [self.summarize_text(chunk) for chunk in chunks]
            summarized_chunks = [chunk for chunk in summarized_chunks if chunk]  # Filter out None values
            final_summary = ' '.join(summarized_chunks)
            if final_summary:
                filename = os.path.splitext(os.path.basename(text_file_path))[0]
                self.save_summary(text, final_summary, filename)

# # Example usage:
# if __name__ == "__main__":
#     text_file_path = 'Generative AI in a Nutshell - how to survive and thrive in the age of AI_video.txt'
#     summarizer = TextSummarizer()
#     summarizer.summarize_text_file(text_file_path)
