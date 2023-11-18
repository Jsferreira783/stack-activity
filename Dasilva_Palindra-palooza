'''A palindrome is a word, phrase, number, or other sequence of characters that
reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
$In other words, a palindrome remains unchanged when its order is reversed.'''
import time

'''Node class represents a node in a linked list'''
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


'''Stack class represents a stack data structure and
 has methods to push and pop elements.'''
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

'''palindrome_checker function checks whether a given input is a palindrome.
It uses a stack to reverse the alphanumeric characters in the input,
then compares the cleaned input with its reverse to determine if it's a palindrome.'''

def palindrome_checker(input_str):
    print("Checking if the input is a palindrome....")
    time.sleep(1)


    ''' Convert input to lowercase'''
    cleaned_input = input_str.lower()
    clean_list = []
    reverse_stack = Stack()

    ''' List of alphanumeric characters'''
    alphanumeric = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
                   [str(i) for i in range(10)]


    '''Filter out non-alphanumeric characters and push them onto the stack'''
    for char in cleaned_input:
        if char in alphanumeric:
            clean_list.append(char)
            reverse_stack.push(char)

    '''Create a reversed list using the stack'''
    reverse_list = []
    while reverse_stack.top is not None:
        popped = reverse_stack.pop()
        reverse_list.append(popped)

    clean = "".join(clean_list)
    reverse = "".join(reverse_list)

    print(f"""<<<<<<<<<<<<<<<<<<<<<*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
              PALINDROME CHECKER
      Input: {input_str}
      Cleaned: {clean}
      Reverse: {reverse}
       """)
    if clean == reverse:
        print("Result: It is a palindrome.")
    else:
        print("Result: It is not a palindrome.")


time.sleep(1)
print("""
     WELCOME TO PALINDROME CHECKER.......
     <<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     """)

#explanation
'''The program initializes the Palindrome Checker and provides a welcome message.
It runs a loop to take user input for checking palindromes.
After each input, it asks the user if they want to check another input.
The loop continues until the user decides to exit.'''
while True:
    palindrome_input = input("Enter your input: ")
    palindrome_checker(palindrome_input)
    time.sleep(1)
    option = input("Do you still want to check again for another input? (yes/no): ")

    if option.lower() == "yes" & "Yes":
        continue
    else:
        print("Thank you for using the Palindrome Checker!")
        time.sleep(1)
        print("END!!!"
              "Closing the Palindrome Checker...")
        break

