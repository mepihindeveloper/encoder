values = {'binary'     : ["0001", "0010", "0011", "0100", "0101", "0110", "0111", 
                          "1000", "1001", "1010", "1011", "1100", "1101", "1110"],
          'managings'  : ["0000", "1111"],
          'firstLine'  : lambda x: (1, 'firstLine',  "ОЕАИТНСРВЛКМДП".find(x)),
          'secondLine' : lambda x: (2, 'secondLine', "УЯЫГЗБЧЙХЪЖЬЮ ".find(x)),
          'thirdLine'  : lambda x: (3, 'thirdLine',  "0123456789.,:/".find(x)),
          'fouthLine'  : lambda x: (4, 'fouthLine',  "ШЦЩЭФЁ+-?!()%=".find(x))}

def add_binary(line_name, letter): return values.get("binary")[values.get(line_name).index(letter)]

def change_line(count = 1):
    if   count ==  3: count    = -1
    elif count == -3: count    =  1
    if count < 0: margin_index =  1 # down
    else:         margin_index =  0 # up
    return ''.join([values.get("managings")[margin_index] for i in range(0, abs(count))])

def main():
    message = input("Введите сообщение: ").upper()
    code, last_line = "", 1
    message = list(message)
    for letter in message:
        new_level_number, new_level_name, binary_index = list(filter(lambda x: x[2] >-1, [values.get(lvl)(letter) \
        for lvl in ('firstLine', 'secondLine', 'thirdLine', 'fouthLine')]))[0]
        code += change_line(last_line - new_level_number) +  values.get("binary")[binary_index]
        last_line = new_level_number
    print(code)

if __name__ == "__main__":
    main()