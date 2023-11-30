"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-1
Write a function in that uses the for loop and the range function to find the sum of all the numbers up to and including the number the user input
The function should return the final total of the sum of all of the items in the list
Add a statement that prompts the user to input an integer
Call the function from step 2 and store its output as a variable
Add a statement to print the variable to see the final sum

__________________________________________________________
"""
def sum_up_to_n():
    # This will prompt the user to input an integer
    user_input = int(input("Enter an integer: "))
    
    # This will Initialize a variable to store the sum
    total_sum = 0

    # this will Use a for loop and the range function to calculate the sum
    for num in range(1, user_input + 1):
        total_sum += num

    return total_sum

# this Calls the function and store its output as a variable
result_sum = sum_up_to_n()

# Print the final sum
print("The sum of all numbers up to and including the input is:", result_sum)

"""
Create a Python file named lab_8-2

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function that will take a list of names and write the body of an email to invite them to a party
The body should be something like this: "Hi name, You're invited to my party on Friday!" Where name is the name of each person in the list.
The function should use a for loop and print each invitation after it is generated. There should be at least 3 names in the list.
"""
def generate_party_invitations(names):
    # This Checks if the list has at least 3 names
    if len(names) < 3:
        print("Please provide a list with at least 3 names.")
        return
    
    # this Uses a for loop to generate invitations for each name
    for name in names:
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        print(invitation)

# these are Examples list of names
guest_list = ["Alice", "Bob", "Charlie", "David"]

#  This Calls the function with the example list
generate_party_invitations(guest_list)
