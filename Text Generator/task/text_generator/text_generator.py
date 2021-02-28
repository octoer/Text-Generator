# Write your code here
# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter
from random import choice, choices


def choice_word(word):
    return choices(list(bigrams_fre[tuple(word[-2:])].keys()), list(bigrams_fre[tuple(word[-2:])].values()))[0]


file_name = input()
with open(file_name, "r", encoding="utf-8") as f:
    tokens = WhitespaceTokenizer().tokenize(f.read())
    # print("Corpus statistics\n", f"All tokens: {len(tokens)}\n", f"Unique tokens: {len(unique_tokens)}\n")
    bigrams = [tokens[x:x + 3] for x in range(len(tokens) - 2)]
    bigrams_fre = defaultdict(list)
    for head1, head2, tails in bigrams:
        bigrams_fre[(head1, head2)].append(tails)
    bigrams_fre = {head: dict(Counter(tails)) for head, tails in bigrams_fre.items()}
    # first_word = choice([i for i in bigrams_fre.keys() if i == i.title() if not i.endswith(('.','!'))])
    # #last_word = first_word[0]
    # sentences = [first_word]
    for i in range(10):
        first_word = choice([i for i in bigrams_fre.keys() if i[0].istitle() if not i[0].endswith(('.', '!', '?'))])
        sentences = list(first_word)
        while True:
            sentences.append(choice_word(sentences))
            # print(choices(list(bigrams_fre[sentences[-1]].keys()), list(bigrams_fre[sentences[-1]].values()))[0])
            if len(sentences) >= 5 and sentences[-1].endswith(('.', '!', '?')):
                break
        print(' '.join(sentences))
        # sentences = sentences[-1:]

    # print(f"Number of bigrams: {len(bigrams)}")
    # while True:
    #     index = input("please input number")
    #     if index == 'exit':
    #         exit()
    #     try:
    #         output = tokens[int(index)]
    #         output = bigrams[int(index)]
    #         output = bigrams_fre[index]
    #     except IndexError:
    #     print("Index Error. Please input an integer that is in the range of the corpus.")
    #     print("Index Error. Please input a value that is not greater than the number of all bigrams.")
    #     continue
    #     except ValueError:
    #     print("Type Error. Please input an integer.")
    #     continue
    #     except KeyError:
    #         print("The requested word is not in the model. Please input another word.")
    #     else:
    #         print(output)
    #         print(f"Head: {output[0]} Tail: {output[1]}")
    #         print(f"Head: {index}")
    #         for tail, count in output.items():
    #             print(f"Tail: {tail}\t count: {count}")
