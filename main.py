with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    num_words = len(file_contents.split())
    ret_dict = {}
    for c in file_contents.lower():
        ret_dict[c] = 1 + ret_dict.get(c, 0)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    dict_list = []
    for char, num in ret_dict.items():
        if (char.isalpha()):
            dict_list.append((num, char))
    dict_list.sort(reverse=True)
    for tup in dict_list:
        print(f"The '{tup[1]}' character was found {tup[0]} times")
    print("--- End report ---")
