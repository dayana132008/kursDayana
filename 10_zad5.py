import os
current_directory = os.getcwd()
print(f"{current_directory}")
os.chdir('..')
new_directory = os.getcwd()
print(f"{new_directory}")