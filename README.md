# Name: Python Challenge 1

## Description

This is one of the challenges from the UNC/EDx AI Bootcamp course. Python Challenge 1 provided a starter python menu file and asked us to complete the remaining sections with commented guidelines provided throughout. 

## Usage

The file is a menu ordering system that allows the user to select multiple items from a menu and ultimately receive a list of the items orders and the total price of the items ordered.

## Project Status

The functionality for ordering and output of items order was completed however, the total price is not presented and further effort is needed for this piece. I was unable to come up with the necessary list comparison to get the total from the info I had provided. 

## Acknowledgements

I am proud of the work I managed to do here considering I have no programming experience. I completed the work based on my studies and assistance from chatgpt for two areas in particular as described below:


### Acknowledgement 1 of 2
Within the menu.py file between lines 185 and 203:

After being stuck for some time on an issue with my code not escaping the outer loop, I asked chat gpt why I couldn't get out of a specific loop and showed it my code. It explained the following:

> It looks like there's an issue with the indentation in your code, specifically within the innermost while True loop. The break statement to exit the innermost loop should be outside of the loop that checks keep_ordering. Here's the corrected portion of your code:


> while True:
    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

    # Check the customer's input
    if keep_ordering == "y":
        # Keep ordering
        break  # Exit the keep ordering question loop

    elif keep_ordering == "n":
        print("Thank you for placing your order.")
        place_order = False
        break  # Exit both the inner and outer loops

    else:
        print("Invalid entry. Please try again.")

My original code was as follows:

   > while True:
       # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # 5. Check the customer's input
        if keep_ordering == "y":
                # Keep ordering
            break
                # Exit the keep ordering question loop
        elif keep_ordering != "n":
            print(f"Invalid entry. Please try again.")

     if keep_ordering == "n":
        print(f"Thank you for placing your order.")
        place_order = False
        break

I corrected my entry per the AI's guidance.


### Acknowledgement 2 of 2

I had trouble with the formatting piece at the end where VC wasn't accepting my math for the formatting. I asked the following to chatgpt:

> why can't i reduce the space size by the item size in the following?
f'{item}{(space * 25)-len(item)}|'

Chatgpt indicated chatgpt that it wasn't working due to how I had the parenthesis plus I was attempting to subtract from float. I revised my coding based on the clarifications.