import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets = data.to_dict()
alphabet_data_frame = pandas.DataFrame(alphabets)
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data_frame.iterrows()}

def gen_phonetic():
    user_txt = input("Enter a word: ").upper()
    try:
        output_list = [alphabet_dict[letter] for letter in user_txt]
    except KeyError:
        print("Sorry, only alphabets are allowed")
        gen_phonetic()
    else:
        print(output_list)


gen_phonetic()