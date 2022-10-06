#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 5, 2022
# a program that calculated the tax


import constants


def main():
    # variables
    subtotal = float(input("Enter subtotal ($ CAD): "))

    # calculations
    tax = subtotal * constants.HST
    total = subtotal + tax

    # displays total amount
    print(f"Your total cost is ${total:.2f}")


if __name__ == "__main__":
    main()
