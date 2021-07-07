
books = []  #製作書名的清單
book = []  #只有書名
with open('book.txt',"r",encoding= 'utf-8') as f:   #先讀取舊有的檔案，之後再繼續寫入新的資料
    for line in f:
        if 'titles,names' in line:  #如果這個字串菜檔案裡
            continue
        title, name = line.strip().split(',') 
        books.append([title, name])
while True:
    name = input('請輸入書名: ')
    if name == 'q':
        break
    name.strip()
    book.append(name)
print(book)


for b in book:
    title = b[0].capitalize()+str(len(b))
    books.append([title, b])
print(books)

for b in books:  #這裡的b是小清單
    print(b[0],'的書名是:', b[1])    

with open('book.txt', 'w',encoding= 'utf-8') as f:
    f.write(('titles,names\n'))  
    for b in books:
        f.write(b[0]+ ',' + b[1] + '\n')        