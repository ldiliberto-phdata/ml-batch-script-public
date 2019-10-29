import sys

import nltk

def main(repeat_times=3, include_taggging=False, sentence=None):
    # Arguments come in as strings from main. Must manually coerce.
    repeat_times = int(repeat_times)
    include_taggging = True if include_taggging.lower() == 'true' else False
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    if not sentence:
        sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    for n in range(repeat_times):
        print(f"repeat time: {n}")
        print(tokens)
    if include_taggging:
        print("Including Tokens")
        tagged = nltk.pos_tag(tokens)
        print(tagged[0:6])

if __name__ == "__main__":
    kwargs = {i.split("=")[0]:i.split("=")[1]  for i in sys.argv}
    main(**kwargs)
