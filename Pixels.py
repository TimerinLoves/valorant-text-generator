import tkinter as tk
import pyperclip

def generate_ascii_art(event=None):
    input_text = entry.get()

    words = input_text.lower().split()

    ascii_arts = {}
    for word in words:
        if len(word) > 6:
            info_label.config(text=f"The word '{word}' has more than 6 letters and cannot be processed.", fg="red")
            return

        lines = [''] * 5

        for i in range(5):
            row_line = ''
            for char in word:
                letter = letters.get(char, letters[' '])
                row_line += letter[i] + '░'
            num_spaces = (26 - len(row_line.strip())) // 2
            lines[i] += '░' * num_spaces + row_line.strip() + '░' * num_spaces

        ascii_art = ''
        for line in lines:
            ascii_art += line + '\n'
        ascii_art += '\n'

        ascii_arts[word] = ascii_art

    for widget in copy_frame.winfo_children():
        widget.destroy()

    for word in words:
        copy_button = tk.Button(copy_frame, text=f"Copy '{word}'", command=lambda w=word: copy_to_clipboard(ascii_arts[w], w))
        copy_button.pack()

def copy_to_clipboard(ascii_art, word):
    pyperclip.copy(ascii_art)
    copied_label.config(text=f"'{word}' copied to clipboard.", fg="green")

root = tk.Tk()
root.title("ASCII Valorant Text Generator")

letters = {
        'a': [
            '███',
            '█░█',
            '███',
            '█░█',
            '█░█'
        ],
        'b': [
            '██░',
            '█░█',
            '██░',
            '█░█',
            '██░'
        ],
        'c': [
            '███',
            '█░░',
            '█░░',
            '█░░',
            '███'
        ],
        'd': [
            '██░',
            '█░█',
            '█░█',
            '█░█',
            '██░'
        ],
        'e': [
            '███',
            '█░░',
            '███',
            '█░░',
            '███'
        ],
        'f': [
            '███',
            '█░░',
            '███',
            '█░░',
            '█░░'
        ],
        'g': [
            '███',
            '█░░',
            '█░█',
            '█░█',
            '███'
        ],
        'h': [
            '█░█',
            '█░█',
            '███',
            '█░█',
            '█░█'
        ],
        'i': [
            '███',
            '░█░',
            '░█░',
            '░█░',
            '███'
        ],
        'j': [
            '░██',
            '░░█',
            '░░█',
            '█░█',
            '███'
        ],
        'k': [
            '█░█',
            '█░█',
            '██░',
            '█░█',
            '█░█'
        ],
        'l': [
            '█░░',
            '█░░',
            '█░░',
            '█░░',
            '███'
        ],
        'm': [
            '█░█',
            '███',
            '█░█',
            '█░█',
            '█░█'
        ],
        'n': [
            '███',
            '█░█',
            '█░█',
            '█░█',
            '█░█'
        ],
        'o': [
            '███',
            '█░█',
            '█░█',
            '█░█',
            '███'
        ],
        'p': [
            '███',
            '█░█',
            '███',
            '█░░',
            '█░░'
        ],
        'q': [
            '███',
            '█░█',
            '███',
            '░░█',
            '░░█'
        ],
        'r': [
            '███',
            '█░█',
            '██░',
            '█░█',
            '█░█'
        ],
        's': [
            '███',
            '█░░',
            '███',
            '░░█',
            '███'
        ],
        't': [
            '███',
            '░█░',
            '░█░',
            '░█░',
            '░█░'
        ],
        'u': [
            '█░█',
            '█░█',
            '█░█',
            '█░█',
            '███'
        ],
        'v': [
            '█░█',
            '█░█',
            '█░█',
            '█░█',
            '░█░'
        ],
        'w': [
            '█░█',
            '█░█',
            '█░█',
            '███',
            '█░█'
        ],
        'x': [
            '█░█',
            '█░█',
            '░█░',
            '█░█',
            '█░█'
        ],
        'y': [
            '█░█',
            '█░█',
            '███',
            '░█░',
            '░█░'
        ],
        'z': [
            '███',
            '░░█',
            '░█░',
            '█░░',
            '███'
        ],
        ' ': [
            '░░░',
            '░░░',
            '░░░',
            '░░░',
            '░░░'
        ],
        '!': [
            '░█░',
            '░█░',
            '░█░',
            '░░░',
            '░█░'
        ],
        '?': [
            '███',
            '░░█',
            '░█░',
            '░░░',
            '░█░'
        ],
        ',': [
            '░░░',
            '░░░',
            '░░░',
            '░█░',
            '░█░'
        ],
        '.': [
            '░░░',
            '░░░',
            '░░░',
            '░░░',
            '░█░'
        ],
        '1': [
            '░█░',
            '██░',
            '░█░',
            '░█░',
            '███'
        ],
        '2': [
            '██░',
            '░░█',
            '░██',
            '█░░',
            '███'
        ],
        '3': [
            '██░',
            '░░█',
            '██░',
            '░░█',
            '██░'
        ],
        '4': [
            '█░█',
            '█░█',
            '███',
            '░░█',
            '░░█'
        ],
        '5': [
            '███',
            '█░░',
            '██░',
            '░░█',
            '██░'
        ],
        '6': [
            '███',
            '█░░',
            '███',
            '█░█',
            '███'
        ],
        '7': [
            '███',
            '░░█',
            '░░█',
            '░░█',
            '░░█'
        ],
        '8': [
            '███',
            '█░█',
            '███',
            '█░█',
            '███'
        ],
        '9': [
            '███',
            '█░█',
            '███',
            '░░█',
            '███'
        ],
        '(': [
            '░█░',
            '█░░',
            '█░░',
            '█░░',
            '░█░'
        ],
        ')': [
            '░█░',
            '░░█',
            '░░█',
            '░░█',
            '░█░'
        ],
        ':': [
            '░░░',
            '░█░',
            '░░░',
            '░█░',
            '░░░'
        ],
        ';': [
            '░░░',
            '░█░',
            '░░░',
            '░█░',
            '░█░'
        ],
        '>': [
            '█░░',
            '░█░',
            '░░█',
            '░█░',
            '█░░'
        ],
        '<': [
            '░░█',
            '░█░',
            '█░░',
            '░█░',
            '░░█'
        ],
            
    }
input_label = tk.Label(root, text="Enter words: (not more then 6 Letters)")
input_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

entry.bind("<Return>", generate_ascii_art)

generate_button = tk.Button(root, text="Generate Valorant Text", command=generate_ascii_art)
generate_button.pack()

copy_frame = tk.Frame(root)
copy_frame.pack()

copied_label = tk.Label(root, text="", fg="green")
copied_label.pack()

root.mainloop()
