dictionary = {}

text = str(input())
texts = text.split()

for word in texts:
    final_word = word[0].upper() + word[1:]

    if final_word not in dictionary:
        dictionary[final_word] = 1
    else:
        dictionary[final_word] += 1

val_based_rev = {k: v for k, v in sorted(dictionary.items(), key=lambda pair: (-pair[1], pair[0]))}

for word, count in val_based_rev.items():
    print(f"{word}{count}" , end= " ")

