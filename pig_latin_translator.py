# Pig Latin e.g. pig -> igPay. First bunch of consonants moved to end + ay added in end.

sentence = input("What's your sentence ? ").strip().lower()

words = sentence.split()

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_words.append(word + "yay")
    else:
        vowel_index = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_index += 1
            else:
                break
        consonant_cluster = word[:vowel_index]
        remaining_part = word[vowel_index:]
        new_word = remaining_part + consonant_cluster + "ay"
        new_words.append(new_word)

new_sentence = " ".join(new_words)

print(new_sentence)