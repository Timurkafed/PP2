import os
#1
path = r'C:\Users\user\Desktop\PP2\lab6'
folder = os.path.basename(path)
files = os.listdir(path)
print(f'Содержимое папки "{folder}":\n', files)
print()

#2
print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))
print()

#3
path = r'C:\Users\user\Desktop\PP2\lab6\dir_and_files.py'
if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')
print()

#4
import os
path =  r'C:\Users\user\Desktop\PP2\lab6\txt.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))
print()
    
#5
with open('txt.txt', 'w') as f:
    lst = [1, 'is', 'mine', [1, 1, 1], (1, 7), {1:5}, {1, 4, 5}]
    f.write(' '.join(map(str, lst)))
    f.write('\n')
    f.writelines(map(str, lst))
print()

#6
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in letters:
    filename = f"{letter}.txt"  
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
print()

#7
with open('A.txt', 'r') as f1:
    with open('B.txt', 'w') as f2:
        f2.write(f1.read())
        
#8
path = r'C:\Users\user\Desktop\PP2\lab6\C.txt'
if os.path.exists(path):
    if os.access(path, os.W_OK): 
        os.remove(path) 
        print(f"File '{os.path.basename(path)}' deleted.")
    else:
        print("Permission denied: You don't have the rights to delete this file.")
else:
    print("File not found.")
print()