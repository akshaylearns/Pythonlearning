text="This is the word that is being used this word must be free from dups"
text1=text.lower()
text2=text1.split(" ")
freq={}
for ch in text2:
    if ch not in freq:
        freq[ch]=text2.count(ch)
print(freq)