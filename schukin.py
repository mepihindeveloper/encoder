# -*- coding: utf8 -*-

import time
import sys

values = {'binary'     : ["00001", "00010", "00011", "00100", "00101", "00110", "00111",
                          "01000", "01001", "01010", "01011", "01100", "01101", "01110",
                          "01111", "10000", "10001", "10010", "10011", "10100", "10101",
                          "10110", "10111", "11000", "11001", "11010", "11011", "11100",
                          '11101', '11110'],
          'managings'  : ["00000", "11111"],
          'firstLine'  : lambda x: (1, 'firstLine',  " eiutsanlrmocd.p,gbqvfhSDxNAPC".find(x)),
          'secondLine' : lambda x: (2, 'secondLine',  "IMFVUEjQL".find(x))}


def add_binary(line_name, letter): return values.get("binary")[values.get(line_name).index(letter)]

def change_line(count=1):
    # if   count ==  3: count    = -1
    # elif count == -3: count    =  1
    if count < 0:
        margin_index = 1  # down
    else:
        margin_index = 0  # up
    return ''.join([values.get("managings")[margin_index] for i in range(0, abs(count))])


def main(): 
    start_time = time.time()
    with open('message.txt', 'r+') as file:
		code, last_line = "", 0
		text = file.read()
		text = text.rstrip()

		message = list(text)
		for letter in message:
			new_level_number, new_level_name, binary_index = list(filter(lambda x: x[2] > -1, [values.get(lvl)(letter) for lvl in ('firstLine', 'secondLine')]))[0]
			code += change_line(last_line - new_level_number) + values.get("binary")[binary_index]
			last_line = new_level_number

		print("--- %s start size Kb ---" % (sys.getsizeof(text) / 1024))
		print("--- %s end size ---" % (sys.getsizeof(code) / 1024))
		#print("--- %s end length ---" % (len(code)))
		print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
