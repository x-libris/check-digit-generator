# Barcode Check Digit Generator

Barcode Check Digit Generator (BCDG) was originally developed to faciliate the creation of 14-digit barcodes compatible with [innovative's Sierra ILS](https://www.iii.com/products/sierra-ils/). However, given that many different barcode formats utilize the mod-10 algorithm for calculating check digits, this application can apply the same algorithm towards barcodes of any character count (but your mileage may vary beyond the intended scope!).

Python libraries required to run the application:
- tkinter
- pyperclip
- datetime (in standard library)

How to Use:

1. Install dependencies: Using pip, install the required libraries listed above. Dependencies can also be installed from the 'requirements.txt' file.
2. Run the app: Navigate to the directory containing the app script (e.g., 'check_digit_generator.py') and run the program.
3. Input a barcode number that needs a check digit (if testing the program, input a barcode number omitting the check digit).
4. If multiple barcodes are desired, check the 'Generate in sequence' box and enter a valid amount. (Barcodes will then be generated incrementally from the 'seed' barcode)
5. Click the 'Calculate' button. If a sequence was requested, the barcodes will be saved to a text file in the same directory as 'check_digit_generator.py'. If only one barcode was requested, it will be copied to the clipboard.
