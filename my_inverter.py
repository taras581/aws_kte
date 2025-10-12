def invert_string(s):
    """Функція приймає рядок і повертає його у зворотному порядку"""
    return s[::-1]

def main():
    print("=== Інвертор рядків ===")
    text = input("Введіть рядок: ")
    inverted = invert_string(text)
    print("Віддзеркалений рядок:", inverted)

if __name__ == "__main__":
    main()
