
#Write a Python program to accept a filename from the user and print the extension of that.

filename=input("\nInput the Filename: ")

f_extension=filename.split()

print("\nThe extension of the file is : ",repr(f_extension[-1]))