import tkinter as tk
import datetime
import pyperclip

class BarcodeGenerator: 
    # Class func "get_barcodes" calls on "check_digit" to populate container with valid barcodes.
    def __init__(self, barcode: str, barcode_amount: str):
        self.barcode = barcode
        self.barcode_amount = int(barcode_amount)
        self.container = []

    def check_digit(self, barcode: str):
        barcode_digits = [int(digit) for digit in barcode]

        # Luhn algorithm: every other number is multiplied by 2 starting w/ the first number.
        # if the product is greater than 10, we take the sum of digits (e.g. 14 --> 1 + 4 = 5).
        # every other number is taken as is. We later take the sum of this list.
        products = [(digit * 2) if i % 2 == 0 and (digit * 2) < 10 
                    else int(str(digit * 2)[0]) + int(str(digit * 2)[1]) if i % 2 == 0 and (digit * 2) < 10 
                    else digit for i, digit in enumerate(barcode_digits, 2)
                    ]

        digits_sum = sum(products)

        if str(digits_sum)[-1] == "0":
            return "0"
        else:
            return str(10 - int(str(digits_sum)[-1]))
        
    def get_barcodes(self):
        for i in range(self.barcode_amount):
            self.container.append(str(int(self.barcode) + i) + self.check_digit(str(int(self.barcode) + i)))

def validate(): # Checking if user input is valid in order to begin barcode processing.
    barcode = enter_barcode.get()

    # sequence_var = checkbox that determines if user has requested to generate a sequence,
    # or if only one barcode has been requested. if no sequence, program defaults to amt of 1.
    if sequence_var.get():
        amount = enter_amount.get()
    else:
        amount = "1"

    # Error cases for invalid barcodes.
    if len(barcode) < 2 or barcode.isnumeric() == False:
        app_message.configure(text="Please enter a valid barcode.", 
                              highlightthickness="2", highlightbackground="red")
        return None
    # Error cases for invalid amounts.
    elif amount.isnumeric() == False or int(amount) < 0 : 
        app_message.configure(text="Please enter a valid amount.", 
                              highlightthickness="2", highlightbackground="red")
        return None
    # Error case for when the barcode + amount would result in a barcode length > than the original length.
    elif len(str(int(barcode) + int(amount))) > len(barcode):
        app_message.configure(text="Amount outpaces barcode length.\n Please try a different barcode / amount.", 
                              highlightthickness="2", highlightbackground="red")
        return None
    else:
        return generate_barcodes(barcode, amount)

def generate_barcodes(barcode, amount): 
    # Barcodes are generated and stored to a list in a "BarcodeGenerator" object.
    new_sequence = BarcodeGenerator(barcode, amount)
    new_sequence.get_barcodes()

    if sequence_var.get(): # If user has requested a sequence, barcodes are saved to txt file.
        return write_barcodes(new_sequence.container)
    else: # Otherwise, new code is shown in app/copied to clipboard.
        pyperclip.copy(f"{new_sequence.container[0]}")
        app_message.configure(text=f"Validated barcode copied to clipboard:\n {new_sequence.container[0]}",
                               highlightthickness="2", highlightbackground="green")

def write_barcodes(barcodes: list):
    # New text file will be named after date / time of processing.
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
    with open(f"{current_time}.txt", "w") as newfile:
        for barcode in barcodes:
            newfile.write(f"{barcode}\n")
    app_message.configure(text="Barcode sequence successfully\n processed to text file!",
                           wraplength=200, highlightthickness="2", highlightbackground="green")

#### GUI Stuff Below ####

root = tk.Tk()
root.title("BCDG")

empty_spacing = tk.Label(root, text="")

app_message = tk.Label(root,
                         text = " *✧ Barcode Check Digit Generator ✧* ",
                         font="Arial 9 italic",)

instructions = tk.Label(root,
                        text=" Please enter a valid barcode number. ",
                        font="Arial 9")

barcode_entry_label = tk.Label(root,
                               text="Barcode ",
                               font="Arial 9 bold",
                               justify="right")

amount_entry_label = tk.Label(root,
                              text="Amount ",
                              font="Arial 9 bold")

enter_barcode = tk.Entry(root,
                         justify="right",
                         font="Arial 9")

enter_amount = tk.Entry(root,
                        justify="right",
                        font='Arial 9')

generate_button = tk.Button(root,
                   text="Calculate check digit(s)",
                   command=validate,
                   relief="groove")

sequence_var = tk.BooleanVar() 

def toggle_entry(): # Checkbox opens / hides the amount entry field.
    if sequence_var.get() == True:
        amount_entry_label.grid(row=3, column=0, sticky="E")
        enter_amount.grid(row=3, column=1, columnspan=1, sticky="W", ipadx=5, padx=5, pady=5)
    else:
        enter_amount.grid_remove()
        amount_entry_label.grid_remove()

sequence_option = tk.Checkbutton(root, text="Generate in sequence?", variable=sequence_var, command=toggle_entry)

app_message.grid(row=0, column=0, columnspan=3, pady=10)
instructions.grid(row=1, column=0, columnspan=3, pady=20, padx=10)
barcode_entry_label.grid(row=2, column=0, sticky="E")
enter_barcode.grid(row=2, column=1, columnspan=1, sticky="W", ipadx=5, padx=5, pady=5)
generate_button.grid(row=5, column=0, columnspan=3, sticky="EW", padx=20, pady=10)
sequence_option.grid(row=6, column=0, columnspan=3, padx=20)
empty_spacing.grid(row=7)

root.mainloop()
    




