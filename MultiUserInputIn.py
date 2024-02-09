'''
Taking user input - some words and sorting the words in their alphabetic order
'''
n=int(input("hoe many words you wnna take = "))
words = []

for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words.append(word)
print("You entered the following words:", words)
res=sorted(words)
print(f'words in sorted are {res}')
for j in res:
    print(j)
