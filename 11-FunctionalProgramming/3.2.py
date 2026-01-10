sentence = 'I completely agree with you'
result = list(map(lambda w: len(w), sentence.split()))
print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")
