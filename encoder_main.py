values = {
        'binary': ["0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
                  "1101", "1110"],
        'managings': ["0000", "1111"],
        'firstLine': ["О", "Е", "А", "И", "Т", "Н", "С", "Р", "В", "Л", "К", "М", "Д", "П"],
        'secondLine': ["У", "Я", "Ы", "Г", "З", "Б", "Ч", "Й", "Х", "Ъ", "Ж", "Ь", "Ю", " "],
        'thirdLine': ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", "/"],
        'fouthLine': ["Ш", "Ц", "Щ", "Э", "Ф", "Ё", "+", "-", "?", "!", "(", ")", "%", "="]
    }


def add_binary(line_name, letter):
    global values
    return values.get("binary")[values.get(line_name).index(letter)]


def change_line(direction, count=1):
    global values
    code = ""
    if direction == "down":
        if count == 1:
            code = values.get("managings")[1]
        else:
            for _ in range(count):
                code += values.get("managings")[1]
    else:
        if count == 1:
            code = values.get("managings")[0]
        else:
            for _ in range(count):
                code += values.get("managings")[0]

    return code


def main():
    global values
    message = input("Введите сообщение: ").upper()
    message = list(message)
    code = ""

    last_line = 1
    for letter in message:
        if letter in values.get('firstLine'):
            if last_line == 2:
                code += (change_line(direction="up") + add_binary(line_name="firstLine", letter=letter))
            elif last_line == 3:
                code += (change_line(direction="up", count=2) + add_binary(line_name="firstLine", letter=letter))
            elif last_line == 4:
                code += (change_line(direction="down") + add_binary(line_name="firstLine", letter=letter))
            else:
                code += add_binary(line_name="firstLine", letter=letter)
            continue

        elif letter in values.get('secondLine'):
            if last_line == 1:
                code += (change_line(direction="down") + add_binary(line_name="secondLine", letter=letter))
            elif last_line == 3:
                code += (change_line(direction="up") + add_binary(line_name="secondLine", letter=letter))
            elif last_line == 4:
                code += (change_line(direction="up", count=2) + add_binary(line_name="secondLine", letter=letter))
            else:
                code += add_binary(line_name="secondLine", letter=letter)
            last_line = 2
            continue

        elif letter in values.get('thirdLine'):
            if last_line == 1:
                code += (change_line(direction="down", count=2) + add_binary(line_name="thirdLine", letter=letter))
            elif last_line == 2:
                code += (change_line(direction="down") + add_binary(line_name="thirdLine", letter=letter))
            elif last_line == 4:
                code += (change_line(direction="up") + add_binary(line_name="thirdLine", letter=letter))
            else:
                code += add_binary(line_name="thirdLine", letter=letter)
            last_line = 3
            continue

        elif letter in values.get('fouthLine'):
            if last_line == 1:
                code += (change_line(direction="up") + add_binary(line_name="fouthLine", letter=letter))
            elif last_line == 2:
                code += (change_line(direction="down", count=2) + add_binary(line_name="fouthLine", letter=letter))
            elif last_line == 3:
                code += (change_line(direction="down") + add_binary(line_name="fouthLine", letter=letter))
            else:
                code += add_binary(line_name="fouthLine", letter=letter)
            last_line = 4
            continue
    print(code)


if __name__ == "__main__":
    main()
