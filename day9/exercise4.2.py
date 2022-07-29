vowels = {"a","e","i","o","u"}
consonants = {'k', 'g', 'v', 'c', 'j', 'b', 'd', 't', 'y', 'f', 's', 'h', 'x', 'r', 'n', 'q', 'l', 'm', 'p', 'z', 'w'}

def has_letters(sentence):
    sentence = set(sentence.lower())
    has_vowels = True
    has_consonants = True
    if vowels <= (sentence):
        has_vowels = True

    if consonants <= (sentence):
        has_consonants = True
    has_all_letters = has_vowels and has_consonants
    print("Has all vowels: "+str(has_vowels)+"\nHas all consonants: "+str(has_consonants)+"\nHas all letters: "+str(has_all_letters))
has_letters("The quick brown fox jumps over the lazy dog")

def vowel_count():
    with open("input.txt", "r") as reader, open("output.txt","w") as writer:
        lines = reader.read()
        writer.write(str(sum(list((map(lines.lower().count, vowels))))))

def unique_list():
    with open("input.txt", "r") as reader, open("output.txt","w") as writer:
        lines = set(reader.read().replace("\n",""))
        writer.write("\n".join(lines))

unique_list()