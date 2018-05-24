import sys, encoder, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calculate(code):
    return sys.getsizeof(code) / 1024

def main():
    # Выбор режима кодирования
    action = input("Введите кодировщик(BasicEncode/OwnEncode): ").lower()
    while action != "ownencode" and action != "basicencode":
        cls()
        action = input("Введите кодировщик(basicencode/ownencode): ").lower()

    # Ввод сообщения для кодирования
    message = input("Введите сообщение: ").upper()

    encoder.Encoder(message)

    if action == "ownencode":
        code = encoder.Encoder(message).ownencode()
    else:
        code = encoder.Encoder(message).basicencode()

    print(code)
    print(len(code))
    print("%.2f" % calculate(code), "КБ")

if __name__ == "__main__":
    main()