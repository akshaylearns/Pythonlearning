text="AkshayDeepakSudarshana"
text1=text.lower()
freq={}
for ch in text1:
    if ch not in freq.keys():
        freq[ch]=text1.count(ch)
print(freq)
