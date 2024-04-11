"""
Name: Jaime Zamora
Date: 4/5/24
Program Description: This program focuses in the analyses of text sentiment and language correction using TextBlob, also using tkinter to create a front end GUI.

Estimated Development Time: 15 hours

My log:
- 4/5/24: Initial setup and exploration of TextBlob and tkinter (2 hours)
- 4/5/24: Development of sentiment analysis feature (3 hours)
- 4/6/24: Development of language detection and speel checking (4 hours)
- 4/7/24: Design and implementation of GUI with tkinter (4 hours)
- 4/7/24: Integration of TextBlob features with the GUI (2 hours)
- 4/8/24: Testing and bug fixes (2 hours)
- 4/11/24: Video Demo prepping and executing (2 hours)

Total Time Spent: 19 hours

Analysis:
The project took 4 hours longer than anticipated mainly due to unexpected challenges in integrating TextBlob with tkinter.
"""



import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    input_text = text_entry.get("1.0", tk.END)
    blob = TextBlob(input_text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        result_var.set("Positive Sentiment")
    elif sentiment < 0:
        result_var.set("Negative Sentiment")
    else:
        result_var.set("Neutral Sentiment")

def correct_spelling():
    input_text = text_entry.get("1.0", tk.END)
    blob = TextBlob(input_text)
    corrected_text = str(blob.correct())
    correction_var.set(f"Corrected Text: {corrected_text}")

# My Front end / Set up for the GUI using tkinter
root = tk.Tk()
root.title("Jaime Zamora - Text Analysis and Spell Check")

text_entry = tk.Text(root, height=20, width=50)
text_entry.pack()

analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

correct_button = tk.Button(root, text="Correct My Spelling", command=correct_spelling)
correct_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

correction_var = tk.StringVar()
correction_label = tk.Label(root, textvariable=correction_var)
correction_label.pack()

root.mainloop()