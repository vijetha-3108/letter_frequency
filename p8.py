def letter_frequency(sentence):
    frequency = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = letter_frequency(sentence)
    print("Letter frequencies:")
    for letter, count in result.items():
        print(f"{letter}: {count}")
