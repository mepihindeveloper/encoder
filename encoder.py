import timeit
class Encoder:
    message = None
    code = ""
    letters = None

    def __init__(self, enteredMessage):
        self.message = enteredMessage
        self.letters = list(self.message)  # разбиваем сообщение на буквы

    def ownencode(self):
        '''Строки кодирования сообщения (некий алфавит своего порядка)'''
        values = ["0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
                  "1101", "1110"]
        firstLine = ["О", "Е", "А", "И", "Т", "Н", "С", "Р", "В", "Л", "К", "М", "Д", "П"]
        secondLine = ["У", "Я", "Ы", "Г", "З", "Б", "Ч", "Й", "Х", "Ъ", "Ж", "Ь", "Ю", " "]
        thirdLine = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", "/"]
        fouthLine = ["Ш", "Ц", "Щ", "Э", "Ф", "Ё", "+", "-", "?", "!", "(", ")", "%", "="]

        lastLine = 1

        for letter in self.letters:
            founded = 0
            index = 0
            for i in firstLine:
                if letter == i:
                    if lastLine == 2:
                        self.code += "0000"
                        self.code += values[index]
                    elif lastLine == 3:
                        self.code += "0000"
                        self.code += "0000"
                        self.code += values[index]
                    elif lastLine == 4:
                        self.code += "1111"
                        self.code += values[index]
                    else:
                        self.code += values[index]
                    founded = 1
                    break
                index += 1
            if founded == 0:
                index = 0
                for i in secondLine:
                    if letter == i:
                        if lastLine == 1:
                            self.code += "1111"
                            self.code += values[index]
                        elif lastLine == 3:
                            self.code += "0000"
                            self.code += values[index]
                        elif lastLine == 4:
                            self.code += "0000"
                            self.code += "0000"
                            self.code += values[index]
                        else:
                            self.code += values[index]
                        founded = 1
                        lastLine = 2
                        break
                    index += 1
                if founded == 0:
                    index = 0
                    for i in thirdLine:
                        if letter == i:
                            if lastLine == 2:
                                self.code += "1111"
                                self.code += values[index]
                            elif lastLine == 1:
                                self.code += "1111"
                                self.code += "1111"
                                self.code += values[index]
                            elif lastLine == 4:
                                self.code += "0000"
                                self.code += values[index]
                            else:
                                self.code += values[index]
                            founded = 1
                            lastLine = 3
                            break
                        index += 1
                    if founded == 0:
                        index = 0
                        for i in fouthLine:
                            if letter == i:
                                if lastLine == 3:
                                    self.code += "1111"
                                    self.code += values[index]
                                elif lastLine == 1:
                                    self.code += "0000"
                                    self.code += values[index]
                                elif lastLine == 2:
                                    self.code += "1111"
                                    self.code += "1111"
                                    self.code += values[index]
                                else:
                                    self.code += values[index]
                                founded = 1
                                lastLine = 4
                                break
                            index += 1

        return self.code

    def basicencode(self):
        startTime = timeit.default_timer()
        '''Строки кодирования сообщения (некий алфавит своего порядка)'''
        values = ["00000000", "00000001", "00000010", "00000011", "00000100", "00000101", "00000110", "00000111",
                  "00001000", "00001001", "00001010", "00001011", "00001100", "00001101", "00001110", "00001111",
                  "00010000", "00010001", "00010010", "00010011", "00010100", "00010101", "00010110", "00010111",
                  "00011100", "00011101", "00011110", "00011111", "00100000", "00100001", "00100010", "00100011",
                  "00100100", "00100101", "00100110", "00100111", "00101000", "00101001", "00101010", "00101011",
                  "00101100", "00101101", "00101110", "00101111", "00110000", "00110001", "00110010", "00110011",
                  "00110100", "00110101", "00110110", "00111000", "00111001", "00111010", "00111011", "00111100"]
        line = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У",
                "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", " ", "0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "+", "-", "=", "/", ".", ",", "?", "!", "(", ")", "%", ":"]

        # Цикл для формирования сообщения с поиском по индексу
        for letter in self.letters:
            index = 0
            for i in line:
                if letter == i:
                    self.code += values[index]
                    break
                index += 1
        print(timeit.default_timer() - startTime)
        return self.code