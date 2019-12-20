#!/usr/bin/env python
# https://github.com/spro/char-rnn.pytorch

import torch
import os
import argparse

from helpers import *
from model import *

# file, file_len = read_file("HarryPotter(All).txt")

# file = file.replace('\n\n', ' ')
# file = file.replace('\n', ' ')

# vocabulary = list(set(file.split(' ')))
# vocab_size = len(vocabulary)

# def generate(decoder, prime_str='A', predict_len=100, temperature=0.8, cuda=False):
def generate(decoder, prime_word=['Harry'], predict_len=100, temperature=0.8, cuda=False):
    hidden = decoder.init_hidden(1)
    prime_input = Variable(word_tensor(prime_word).unsqueeze(0))

    if cuda:
        hidden = hidden.cuda()
        prime_input = prime_input.cuda()
    predicted = prime_word[0]

    # Use priming string to "build up" hidden state
    for p in range(len(prime_word) - 1):
        _, hidden = decoder(prime_input[:,p], hidden)
        
    inp = prime_input[:,-1]
    
    for p in range(predict_len):
        output, hidden = decoder(inp, hidden)
        
        # Sample from the network as a multinomial distribution
        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist, 1)[0]
        # Add predicted word to string and use as next input
        predicted_word = vocabulary[top_i]
        predicted = predicted + " " + predicted_word
        inp = Variable(word_tensor([predicted_word]).unsqueeze(0))
        if cuda:
            inp = inp.cuda()

    return predicted

# Run as standalone script
if __name__ == '__main__':

# Parse command line arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('filename', type=str)
# https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
    argparser.add_argument('-p', '--prime_word', nargs="+", type=str, default=['Harry'])
    argparser.add_argument('-l', '--predict_len', type=int, default=100)
    argparser.add_argument('-t', '--temperature', type=float, default=0.8)
    argparser.add_argument('--cuda', action='store_true')
    args = argparser.parse_args()

    decoder = torch.load(args.filename)
    del args.filename
    generated_text = generate(decoder, **vars(args))
    print(generated_text)
    f1 = open("28NovemberPotterOutput.txt", "a")
    f1.write(generated_text)
    f1.close()