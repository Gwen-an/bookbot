
def book_to_string(b_path):
    with open(b_path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    ltext = text.lower()
    characters = {}
    for c in ltext:
        if c in characters:
            characters[c] +=1
        else:
            characters[c] = 1
    return characters

def dico_to_list(d):
    l = []
    for k in d:
        l.append({"character":k, "num":d[k]})
    return l

def sort_on(dict):
    return dict["num"]

def sort_dico(dico):
    dico.sort(reverse=True, key=sort_on)

def print_report(book, wc, characters):
    print(f"###Report for {book} ###")
    print(f"There are {wc} words in the book !")
    for k in characters:
        if k["character"].isalpha():
            print(f"The {k['character']} character has been found {k['num']} times.")


def main():
    book = "books/frankenstein.txt"
    text = book_to_string(book)
    wc = word_count(text)
    char = dico_to_list(char_count(text))
    sort_dico(char)
    print_report(book,wc,char)
      
     
main()