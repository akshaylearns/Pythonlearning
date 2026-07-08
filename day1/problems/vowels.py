vowels=["a","e","i","o","u"]
word=input("Enter a word").lower()
count=0
for ch in word:
    if ch in vowels:
        count+=1
print(count)