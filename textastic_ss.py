"""
DS 3500 HW 7 Extensible NLP Frameworks
Gabrielle Bambalan, Desiree DeGennaro, Zoe Chapman, Miguel (Iggy) Gonzales
Description: Reusable library for text analysis and comparison
"""
import matplotlib.pyplot as plt
import random as rnd
from collections import Counter, defaultdict
import nltk
from nltk.tokenize import word_tokenize



class Textastic:
    def __init__(self):
        self.data = defaultdict(dict)  # default dictionary of dictionaries

    @staticmethod
    def _default_parser(filename):
        """a default text parser for processing simple unformatted text files"""
        with open(filename) as file:
            text = file.readlines()
            text = text.replace("\n", "").strip()
        return text

    def load_text(self, filename, label=None, parser=None):  # write text parser here
        # default parser should take a regular text file with no special parsing
        # result is a dictionary
        if parser is None:
            results = Textastic._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        for k, v in results.items():
            self.data[k][label] = v

        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        tokens = word_tokenize(text)
        stopwords = self.load_stop_words('stopwords.txt')
        filtered_tokens = [word for word in tokens if word not in stopwords]
        word_count = Counter(filtered_tokens)
        word_count = self.data['word_count'][label]

    def load_stop_words(self, filename):
        """loads in a list of stop words from a file"""
        with open(filename) as file:
            content = file.readlines()
            stopwords = [i.strip() for i in content]

        return stopwords

    # Below are functions for visualization purposes:

    def wordcount_sankey(self, word_list=None, k=5):
        if word_list is None:
            word_lists = [Counter(self.data['word_count'][label]).most_common(k) for label in self.data['word_count']]
            common_words = set(word for word, _ in sum(word_lists, []))
        else:
            common_words = set(word_list)

        # sankey
        sources = []
        targets = []
        values = []
        label_mapping = {}
        for i, label in enumerate(self.data['word_count']):
            label_mapping[label] = i
            word_count = self.data['word_count'][label]
            for word, count in word_count.items():
                if word in common_words:
                    sources.append(i)
                    targets.append(len(self.data['word_count']) + list(common_words).index(word))
                    values.append(count)
        # plot
        sankey = Sankey(flows=values, labels=list(self.data['word_count']) + list(common_words))
        sankey.finish()
        plt.show()

    def compare_num_words(self):
        """simplistic viz that creates a bar chart comparing num of words NOT TO BE USED IN HW"""
        for label, nw in self.data['numwords'].items():
            plt.bar(label, nw)
        plt.show()
        # extracting label value pairs from numwords dict to a tuple

    def subplot(self):
        num_files = len(self.data['word_count'])
        fig, axes = plt.subplots(1, num_files)
        for i, label in enumerate(self.data['word_count']):
            word_count = self.data['word_count'][label]
            words, counts = zip(*word_count.items())
            axes[i].bar(words, counts)
            axes[i].set_title(label)

        plt.tight_layout()
        plt.show()

    def overlay(self):
        fig, ax = plt.subplots(figsize=(10, 6))

        for label, word_count in self.data['word_count'].items():
            words, counts = zip(*word_count.items())
            ax.plot(words, counts, label=label)

        ax.legend()
        ax.set_xlabel('Words')
        ax.set_ylabel('Counts')
        plt.show()
