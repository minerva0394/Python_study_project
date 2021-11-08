texts = "Life is a chess-board The chess-board is the world: the pieces are the phenomena of the universe; the rules " \
        "of the game are what we call the laws of nature. The player on the other side is hidden from us. We know " \
        "that his play is always fair, just and patient. But also we know, to our cost, that he never overlooks a " \
        "mistake, or makes the smallest allowance for ignorance. "

for ch in ":;,.?!":
    texts = texts.replace(ch, " ")
words = texts.split()
words = sorted(set(words))
print(len(words))
map1 = {}
for word in words:
    if word in map1:
        map1[word] += 1
    else:
        map1[word] = 1
items = list(map1.items())
for item in items:
    word, count = item
    print(word)
