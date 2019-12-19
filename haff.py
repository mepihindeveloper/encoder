# -*- coding: utf8 -*-
import sys
import time

def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    #assert(sum(p.values()) == 1.0) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    #sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    sorted_p = sorted(p.items(), key=lambda x: x[1])	
    return sorted_p[0][0], sorted_p[1][0]

def calculate(code):
    return sys.getsizeof(code) / 1024

def freq():
	b = {}
	c = 0
	with open('message.txt',"r") as f:
		for l in f.read():
			l = l.lower()
			if (l in 'abcdefghijklmnopqrstuvwxyz0123456789.,:/+-?!()%= '):
				c +=1
				if (l in b):
					b[l] +=1
				else:
					b[l] = 1
	ex = {}
	#s = 0;
	for u in b.keys():
	#	print('Символ {} занимает {:.1f}% текста'.format(u,10/c*b[u]))
		ex[u] = (100/c*b[u]);
	#	s += (100/c*b[u]);
	return ex
	
start_time = time.time()
freq = huffman(freq());
encoded_message = '';
with open('message.txt',"r") as f:
	for l in f.read():
		l = l.lower()
		if (l in freq):
			encoded_message += freq[l];
			
print("--- %s seconds ---" % (time.time() - start_time))
print("%.5f" % calculate(encoded_message) + "КБ")
