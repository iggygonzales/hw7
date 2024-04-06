from collections import Counter
import fitz
import string

with fitz.open("Black_Cat.pdf") as file:
    text = ""
    for page in file:
        text += page.get_text()
    word_counts = Counter()
    total_num_words = 0
    for word in text.lower().split():
        word_counts[word] += 1
        total_num_words += 1
    dict = {'wordcount': word_counts, 'numwords': total_num_words}
    print(dict)
