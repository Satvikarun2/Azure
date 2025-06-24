import nltk
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
import heapq


#necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__, template_folder='templates3')

def summarize_text(text, num_sentences=3):
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_tokenizer = PunktSentenceTokenizer(punkt_param)
    sentences = punkt_tokenizer.tokenize(text)


    stop_words = set(stopwords.words('english') + list(punctuation))
    word_frequencies = {}

    for word in word_tokenize(text.lower()):
        if word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if len(sentence.split(' ')) < 30:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return ' '.join(summary_sentences)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = None
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = request.form.get('num_sentences', 3)
        try:
            num_sentences = int(num_sentences)
        except ValueError:
            num_sentences = 3
        summary = summarize_text(text, num_sentences=num_sentences)
    return render_template('index3.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
