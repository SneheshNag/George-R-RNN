import argparse
import os

from helpers import *

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('filename', type=str)
args = argparser.parse_args()

print("Saving vocabulary for {}".format(args.filename))
# file, file_len = read_file("HarryPotter.txt")
file, file_len = read_file(args.filename)

file = file.replace('\n\n', ' ')
file = file.replace('\n', ' ')
file = file.split(' ')
# file_len = len(file)

# vocabulary = list(set(file.split(' ')))
vocabulary = list(set(file))
    
saveFile = os.path.splitext(os.path.basename(args.filename))[0] + '_vocab.txt'
f1 = open(saveFile, 'a')
    # f1 = open("harryPutter.txt", "a")
# f1.write(vocabulary)
for elem in vocabulary:
    f1.write(elem + "\n")

f1.close()

print("Saved vocabulary")