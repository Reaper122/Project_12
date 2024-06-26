import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
import random
import pandas as pd

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

class MCQGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.read_text_file(file_path)
        self.mcqs = []

    def read_text_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return text

    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ')
                if synonym.lower() != word.lower():
                    synonyms.add(synonym)
        return list(synonyms)

    def generate_mcqs(self):
        sentences = sent_tokenize(self.text)

        for sentence in sentences:
            words = word_tokenize(sentence)
            words_pos = nltk.pos_tag(words)
            nouns = [word for word, pos in words_pos if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
            
            if nouns:
                correct_answer = random.choice(nouns)
                question_text = sentence.replace(correct_answer, "______")
                synonyms = self.get_synonyms(correct_answer)
                if synonyms and len(synonyms) >= 3:
                    distractors = random.sample(synonyms, 3)
                    options = [correct_answer] + distractors
                    random.shuffle(options)
                    self.mcqs.append([question_text] + options + [correct_answer])

    def save_to_csv(self, filename):
        df = pd.DataFrame(self.mcqs, columns=['Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer'])
        df.to_csv(filename, index=False)

    def save_to_text(self, filename):
        with open(filename, 'w') as f:
            for mcq in self.mcqs:
                f.write(f"Question: {mcq[0]}\n")
                f.write(f"A) {mcq[1]}\n")
                f.write(f"B) {mcq[2]}\n")
                f.write(f"C) {mcq[3]}\n")
                f.write(f"D) {mcq[4]}\n")
                f.write(f"Correct Answer: {mcq[5]}\n\n")

    def generate_and_save_mcqs(self, csv_filename, text_filename):
        self.generate_mcqs()
        self.save_to_csv(csv_filename)
        self.save_to_text(text_filename)
        print(f"{len(self.mcqs)} MCQs generated and saved successfully!")

# # Example usage:
# file_path = 'input_text.txt'  # Update with your file path
# mcq_generator = MCQGenerator(file_path)
# mcq_generator.generate_and_save_mcqs('mcqs.csv', 'mcqs.txt')
