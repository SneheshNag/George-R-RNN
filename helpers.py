# https://github.com/spro/char-rnn.pytorch

import unidecode
import string
import random
import time
import math
import torch

# from train import vocabulary, vocab_size
# Reading and un-unicode-encoding data

# all_characters = string.printable
# n_characters = len(all_characters)


def read_file(filename):
    file = unidecode.unidecode(open(filename, encoding='utf-8').read())
    return file, len(file)

# Turning a string into a tensor

# def char_tensor(string):
#     tensor = torch.zeros(len(string)).long()
#     for c in range(len(string)):
#         try:
#             tensor[c] = all_characters.index(string[c])
#         except:
#             continue
#     return tensor

# file, file_len = read_file("HarryPotter(All).txt")

# file, file_len = read_file("HarryPotter.txt")

# file = file.replace('\n\n', ' ')
# file = file.replace('\n', ' ')
# file = file.split(' ')
# file_len = len(file)

# Comment this line out when creating a new vocabulary file.
# Uncomment this line after the vocabulary text file has been created.
file, fL = read_file("HarryPotter.txt")
vocabulary = file.split('\n')[:-1]

# vocabulary = list(set(file.split(' ')))
# vocabulary = list(set(file))
# print(vocabulary)
# vocabulary = list(set(file.split(' ')))

# def word_tensor(string):
#     tensor = torch.zeros(len(string.split(' '))).long()
#     for word in range(len(string.split(' '))):
#         try:
#             tensor[word] = vocabulary.index(string.split(' ')[word])
#         except:
#             tensor[word] = len(vocabulary) + 2 #If the word is not found
#     return tensor

def word_tensor(chunk_of_words):
    tensor = torch.zeros(len(chunk_of_words)).long()
    for word in range(len(chunk_of_words)):
        try:
            tensor[word] = vocabulary.index(chunk_of_words[word])
        except:
            continue
            # tensor[word] = len(vocabulary) + 2 #If the word is not found
    return tensor

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

