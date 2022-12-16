inp = input("Input: ")
for characters in "aeiouAEIOU":
    inp = inp.replace(characters, "")
print(f"Output: {inp}")