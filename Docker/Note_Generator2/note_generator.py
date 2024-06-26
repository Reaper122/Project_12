import os
import csv
from transformers import pipeline

class NoteGenerator:
    def __init__(self, model_name='facebook/bart-large-cnn', chunk_size=512, note_length=150, output_path='./notes'):
        self.summarizer = pipeline('summarization', model=model_name)
        self.chunk_size = chunk_size
        self.note_length = note_length
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

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

    def generate_notes(self, text):
        try:
            notes = self.summarizer(text, max_length=self.note_length, min_length=int(self.note_length / 2), do_sample=False)
            notes_text = notes[0]['summary_text']
            return notes_text
        except Exception as e:
            print(f"Error generating notes: {e}")
            return None

    def save_notes(self, original_text, notes, filename):
        text_file_path = os.path.join(self.output_path, filename + '_notes.txt')
        csv_file_path = os.path.join(self.output_path, filename + '_notes.csv')

        # Save as text file
        try:
            with open(text_file_path, 'w') as text_file:
                text_file.write(notes)
            print(f"Notes saved as text file: {text_file_path}")
        except Exception as e:
            print(f"Error saving text file: {e}")

        # Save as CSV file
        try:
            with open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Original Text', 'Notes'])
                writer.writerow([original_text, notes])
            print(f"Notes saved as CSV file: {csv_file_path}")
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    def generate_notes_from_file(self, text_file_path):
        text = self.load_text(text_file_path)
        if text:
            chunks = self.split_text(text)
            generated_notes = [self.generate_notes(chunk) for chunk in chunks]
            generated_notes = [note for note in generated_notes if note]  # Filter out None values
            final_notes = ' '.join(generated_notes)
            if final_notes:
                filename = os.path.splitext(os.path.basename(text_file_path))[0]
                self.save_notes(text, final_notes, filename)

# Example usage:
if __name__ == "__main__":
    text_file_path = 'Generative AI in a Nutshell - how to survive and thrive in the age of AI_video.txt'
    note_generator = NoteGenerator()
    note_generator.generate_notes_from_file(text_file_path)
