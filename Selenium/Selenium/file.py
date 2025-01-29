with open('text.txt','r') as file:
    x=file.readlines()
    reversed(x)
    with open('text.txt','w') as writer:
        for i in reversed(x):
            writer.write(i)
        print(".....................")
    with open('text.txt', 'r') as file2:
        print(file2.read())








