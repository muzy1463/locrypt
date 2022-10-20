import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from functions import encrypt, data_importer
from PIL import Image, ImageTk

BACKGROUND_COLOR = "black"
FOREGROUND_COLOR = "white"
FONT = "Terminal"


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("LoCrpyt")
        self.iconbitmap("assets/logo.ico")
        self.geometry('900x950')
        self.resizable(False, False)
        self.config(bg=BACKGROUND_COLOR)
        self.is_caesar = False
        self.caesar_step = None
        self.caesar_open = False
        self.key = None

        style = ttk.Style(self)
        style.configure('vista', font=('Helvetica', 12))

        label_text = ["LoCrypto App", "Select an algorithm: ", "© 2022 Muzy1463 TR, Inc. All rights reserved.",
                      "Powered by", "Input: ", "Output: "]

        label_place_x, label_place_y = [450, 450, 300, 720, 110, 115], [70, 125, 900, 900, 230, 550]

        for i in range(0, len(label_text)):
            font_size = 28 if i == 0 else 14
            new_label = ttk.Label(text=label_text[i], font=(FONT, font_size))
            new_label.place(x=label_place_x[i], y=label_place_y[i], anchor="center")
            new_label.config(background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)

        self.algorithm_list = ["Random", "Caesar", "MD5", "SHA1", "SHA224", "SHA3-224", "SHA256", "SHA3-384",
                               "SHA512", "SHA3-512"]

        selected_algorithm = tk.StringVar()

        self.algorithm_combobox = ttk.Combobox(self, textvariable=selected_algorithm, width=30, height=25)
        self.algorithm_combobox['values'] = [i for i in self.algorithm_list]
        self.algorithm_combobox['state'] = 'readonly'
        self.algorithm_combobox.place(x=450, y=165, anchor="center")

        radio_style = ttk.Style()
        radio_style.configure('TRadiobutton', foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR, font=(FONT, 16))

        self.selection = tk.StringVar()
        self.selection.set(1)

        selection_encryption = ttk.Radiobutton(self, text="Encrypt", variable=self.selection, value=1,
                                               style='TRadiobutton')
        selection_encryption.place(x=385, y=205, anchor="center")

        selection_decryption = ttk.Radiobutton(self, text="Decrypt", variable=self.selection, value=-1,
                                               style='TRadiobutton')
        selection_decryption.place(x=515, y=205, anchor="center")

        self.entry = ScrolledText(self, font=(FONT, 16))
        self.entry.place(x=450, y=380, anchor="center", width=750, height=250)

        self.output = ScrolledText(self, font=(FONT, 16))
        self.output["state"] = 'disabled'
        self.output.place(x=450, y=700, anchor="center", width=750, height=250)

        button_commands = [lambda: self.submit(self.algorithm_combobox.get(), self.entry.get('1.0', tk.END)[:-1]),
                           lambda: data_importer(self.entry.get('1.0', tk.END)[:-1], self.output.get('1.0', tk.END),
                           self.algorithm_combobox.get(), key=self.key, direction=int(self.selection.get())),
                           self.destroy]

        button_texts = ["Submit", "Import", "Quit"]
        button_x_place, button_y_place = [773, 664, 773], [530, 850, 850]

        for i in range(0, len(button_texts)):
            new_button = tk.Button(self, text=button_texts[i], background=BACKGROUND_COLOR, fg=FOREGROUND_COLOR,
                                   activebackground="black", width=10, font=(FONT, 14),
                                   command=button_commands[i])

            new_button.place(x=button_x_place[i], y=button_y_place[i], anchor="center")

        python_image = ImageTk.PhotoImage(Image.open("assets/python.png"))
        python_label = ttk.Label(self, image=python_image, background=BACKGROUND_COLOR)
        python_label.image = python_image
        python_label.place(x=800, y=900, anchor="center")

    def submit(self, algorithm, text):
        self.output["state"] = 'normal'
        self.output.delete("1.0", tk.END)

        if int(self.selection.get()) == 1:

            if algorithm == self.algorithm_list[1]:
                if self.caesar_open is False:
                    self.caesar_open = True
                    x = CaesarWindow(self, algorithm, text)
                    x.mainloop()
                    self.caesar_open = False

                else:
                    pass

            else:
                encrypted_text = encrypt(algorithm, text, controller=self)
                self.output.insert(tk.INSERT, encrypted_text)

        else:
            if algorithm == self.algorithm_list[1]:
                x = CaesarWindow(self, algorithm, text)
                x.mainloop()

            elif algorithm == self.algorithm_list[0]:
                self.output.insert(tk.INSERT, "ERROR: You can not reverse a random encryption.")

            else:
                error_text = f"ERROR: You can not reverse the {algorithm} algorithm"
                self.output.insert(tk.INSERT, error_text)


class CaesarWindow(tk.Tk):

    def __init__(self, controller, algorithm, text):
        super().__init__()
        self.geometry("200x140")
        self.resizable(False, False)
        self.config(bg=BACKGROUND_COLOR)

        caesar_style = ttk.Style(self)
        caesar_style.configure('vista', font=('Helvetica', 12))

        intro_label = ttk.Label(self, text="Enter the step: ", font=(FONT, 10))
        intro_label.place(x=100, y=20, anchor="center")
        intro_label.config(background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)

        caesar_step = tk.IntVar()
        step_entry = ttk.Entry(self, textvariable=caesar_step, width=10)
        step_entry.place(x=100, y=60, anchor="center")

        submit_button = tk.Button(self, text="Submit", background=BACKGROUND_COLOR, fg=FOREGROUND_COLOR,
                                  activebackground=BACKGROUND_COLOR,
                                  width=10, activeforeground="white", font=(FONT, 14),
                                  command=lambda: self.submit(controller, step_entry.get(), algorithm, text))

        submit_button.place(x=100, y=110, anchor="center")

    def submit(self, controller, step, algorithm, text):
        try:
            step = int(step)
            controller.caesar_step = step
            controller.output.insert(tk.INSERT, encrypt(algorithm, text, step,
                                                        caesar_direction=int(controller.selection.get()),
                                                        controller=controller))
            controller.caesar_open = False
            self.destroy()

        except ValueError:
            return None
