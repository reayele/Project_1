"""
Program name: UPC Validator
Author: Rediet Ayele
Purpose: Write a program that validates a 12-digit UPC-A code. The program will ask the user for a 12-digit UPC, use a function to calculate the correct check digit, and then inform the user if the full UPC is valid.
Date: 06/26/26
"""

upc = input("Enter a 12-digit UPC: ")


first_11 = upc[:11]
provided_check_digit = upc[-1]

def find_UPC(first_11):
       print("The first 11 digits are  ", first_11)
       print("The provided check digit is ", provided_check_digit)

       print("Calculating...")

       odd_1 = ((int(first_11[0])+ int(first_11[2])+ int(first_11[4])+ int(first_11[6])+ int(first_11[8])+ int(first_11[10]))* 3)
       even_1 = (int(first_11[1])+ int(first_11[3])+int(first_11[5])+int(first_11[7]) + int(first_11[9]))
       check_digits = (odd_1)+(even_1)
       expected_check_digit = find_UPC(first_11)
       expected_check_digit = (10 - (check_digits % 10)) % 10

       return expected_check_digit
    
    