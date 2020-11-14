import wordcloud
import numpy as np
import io
import sys
from matplotlib import pyplot as plt
from IPython.display import display
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename



Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

f = open(filename, encoding="utf8")
file_contents = f.read()

def rmv_symbols(txt):
    alphastr = ""
    for i in txt:
        if i.isalpha() or i == " ":
            alphastr = alphastr + i
    return alphastr.lower()
    
def rmv_useless(wordlist):
    uninteresting_words = ["in", "for", "not", "on", "so", "much", "mr" , "mrs", "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    newlist = []
    for i in wordlist:
        if i not in uninteresting_words:
            newlist.append(i)
    return newlist
wordslist = rmv_symbols(file_contents).split()
useful_words = rmv_useless(wordslist)
def calculate_frequencies(useful_words):
    dictionary = dict()
    for i in useful_words:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i]=1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dictionary)
    return cloud.to_array()

# Display wordcloud image

myimage = calculate_frequencies(useful_words)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()