def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        correct_for_counter = file_contents.lower()
        all_counted ={}
        for char in correct_for_counter:
            if char.isalpha():
                if char in all_counted:
                    all_counted[char] +=1 
                else:
                    all_counted[char] = 1
        number_of_words = word_counter(file_contents)
        print_format(all_counted,number_of_words)
    return None

def print_format(dictionary,num_words):
    print ("--- beginning book report of frankenstein.txt ---")
    print(f"there are {num_words} in frankenstein.txt")
    sorted_dict = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse = True ))
    for entry in sorted_dict:
        print(f"the character {entry} has appeared {sorted_dict[entry]} times")
    print("--- end of book report ---")


def word_counter(book):
    return len(book.split())

main()