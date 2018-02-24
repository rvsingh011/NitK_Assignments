import nltk
from nltk.corpus import gutenberg
# print(gutenberg.fileids())
posting = {}
for file_name in gutenberg.fileids():
    index = file_name
    for word in gutenberg.words(file_name):
        if word in posting:
            if index in posting['word']:
                print(posting['word']['index'])
            else:
                p



