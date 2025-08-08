import os
def list_files():
    user_input = input("Enter directory: ")
    os.system("ls " + user_input)  # 🚨 Vulnerable: unsanitized user input
