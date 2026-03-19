class Navivorit():
    def __init__(self, text="Перше слово посередині останнє. Ще одне тестове речення."):
        self.text = text
    def diya(self):
        if not isinstance(self.text, str) or ("." not in self.text):
            return ('введіть повноцінне речення')
        else:
            self.raw_sentences = self.text.split('.')
            self.processed_sentences = []
            for sentence in self.raw_sentences:
                clean_sentence = sentence.strip()
                if len(clean_sentence) > 0:
                    words_buffer = clean_sentence.split(' ')
                    if len(words_buffer) > 1:
                        words_buffer[0], words_buffer[-1] = words_buffer[-1], words_buffer[0]
                    new_sentence = " ".join(words_buffer) + "."
                    self.processed_sentences.append(new_sentence)
            self.final_text = " ".join(self.processed_sentences)
            return self.final_text
if __name__ == '__main__':
    text = "Друге слово посередині останнє. Ще одне тестове речення."
    app=Navivorit(text)
    print(app.diya())