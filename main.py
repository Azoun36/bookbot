#Sorting dictionary
def char_list_sorting(dict):
    sorted = []
    for char in dict:
        sorted.append({"char": char, "number": dict[char]})
    sorted.sort(key=currently_sorting,reverse=True)
    return sorted

def currently_sorting(x):
    return x["number"]

#Count the number of each letter
def characters(input_text):
    chars = {}
    for x in input_text:
        lowercase = x.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

#Get the book location
def booktext(path):
    with open(path) as f:
        return f.read()

#Count the number of words   
def wordcount(input_text):
    count = input_text.split()
    return len(count)

def main():
    location = "books/frankenstein.txt"
    text = booktext(location)
    words = wordcount(text)
    char_num = characters(text)
    sorted_list = char_list_sorting(char_num)
    print(f"*** Begin report of {location} ***")
    print(f"{words} total words found")
    print("")

    for x in sorted_list:
        if not x["char"].isalpha():
            continue
        print(f"{x['char']} is repeated {x['number']} times")

    print("")
    print("*** End report ***")

main()