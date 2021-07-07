#BOOK Titles:
'''
recall the readlines() method, which returns a list containing the lines of 
the file. Also, remember that all linese, except the last one, contain a \n at the end, 
which should not be included in the character count.
'''
book = []
x = 0
with open('book.txt', "r") as f:
    for line in f:
        book.append(line.strip())
        code = (book[x][0]+ str(len(line)))
        x += 1 
        print(code)
