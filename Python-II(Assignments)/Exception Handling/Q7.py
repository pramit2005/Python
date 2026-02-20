#Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    a=int(input('Enter a number: '))
except KeyboardInterrupt:
    print('\nThe input is halted using keyboard interrupt')
else:
    print('The input number is:',a)
