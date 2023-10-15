import sys
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init

init(autoreset=True)


def display_menu():
    print("Text Styler Menu:")
    print("1. Change Text Color")
    print("2. Change Text Background Color")
    print("3. Display Text in ASCII Art")
    print("4. Quit")


def change_text_color(text, color):
    return colored(text, color)


def change_text_background_color(text, bg_color):
    return colored(text, on_color=bg_color)


def display_ascii_art(text, font):
    figlet = Figlet(font=font)
    return figlet.renderText(text)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text: ")
            color = input("Enter the color (e.g., red, green, yellow): ")
            print(change_text_color(text, color))

        elif choice == "2":
            text = input("Enter the text: ")
            bg_color = input(
                "Enter the background color (e.g., white, blue, magenta): "
            )
            print(change_text_background_color(text, bg_color))

        elif choice == "3":
            text = input("Enter the text: ")
            font = input("Select a font from the 'fonts' directory (e.g., font1.flf): ")
            print(display_ascii_art(text, f"fonts/{font}"))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
