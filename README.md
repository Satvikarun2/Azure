📌 Overview
This project is a lightweight web application that summarizes input text using a sentence scoring algorithm based on word frequency. It uses Natural Language Toolkit (NLTK) for text processing and Flask as the backend web framework. The app allows users to input long text and receive a concise summary of a specified number of sentences.

🎯 Features
Extractive text summarization using NLTK

Sentence scoring based on word frequency

User-defined number of sentences in summary

Web interface for easy interaction

Deployed locally using Flask

Clean, responsive HTML/CSS UI

🛠️ Technologies Used
Language: Python

Web Framework: Flask

NLP Library: NLTK

Frontend: HTML, CSS (via index3.html)

Runtime: VS Code / Localhost

📂 Project Structure
bash
project-root/
│
├── app3.py                # Flask backend application
├── templates3/
│   └── index3.html        # HTML front-end for the app
├── README.md              # This file
🚀 How to Run the Project
1. 🛠 Prerequisites
Make sure you have Python installed. Then install dependencies:

bash
pip install flask nltk
2. 🔄 Download NLTK Data
The app will automatically download necessary datasets when you first run it. Alternatively, you can do it manually:

python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
3. ▶️ Run the Flask App
From the terminal:

bash
python app3.py
The app will be available at:
http://127.0.0.1:5000/

💡 How It Works
The user enters a block of text in the web interface.

The input is tokenized into words and sentences using NLTK.

Words are scored based on frequency, excluding stopwords and punctuation.

Sentences are scored by summing the scores of their constituent words.

The top n scored sentences (based on user input) are selected as the summary.

📸 Screenshots
![image](https://github.com/user-attachments/assets/5fcbe50a-240e-40c8-8768-6058c40d2334)

🔮 Future Improvements
Add file upload support (PDF, TXT)

Improve summarization with POS tagging and TF-IDF

Deploy the app on cloud (e.g., Heroku, Render, or AWS)

Integrate more summarization techniques (e.g., BERT or spaCy-based)

✍️ Author
Satvik Arun
Postgraduate in Data Science | Machine Learning Engineer
