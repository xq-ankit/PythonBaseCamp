with open('hello.txt' ,'r') as file:
        content = file.read()
        lines = content.split('\n')
        words = content.split()
print(len(content))
print(len(words))
print(len(lines))
()