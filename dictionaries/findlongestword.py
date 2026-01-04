text=" I am a dog and I bark all the time relentlessly"

words = text.split()
longest_word = max(words, key=len)
print(longest_word)