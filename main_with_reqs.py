import sys

import nltk

def main(repeat_times=3, include_tagging=False, sentence=None):
    # Arguments come in as strings from main. Must manually coerce.
    print(include_tagging)
    repeat_times = int(repeat_times)
    include_tagging = True if str(include_tagging).lower() == 'true' else False
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    if not sentence:
        sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    for n in range(repeat_times):
        print(f"repeat time: {n}")
        print(tokens)
    if include_tagging:
        print("Including Tokens")
        tagged = nltk.pos_tag(tokens)
        print(tagged[0:6])

if __name__ == "__main__":
    # We will get either json list of args, a json map of kwargs, both or neither.
    args, kwargs = [], {}
    if len(sys.argv) > 1:
        argvs = [json.loads(w) for w in sys.argv[1:]]
        args = [w for w in argvs if isinstance(w, list)]
        kwargs = [w for w in argvs if isinstance(w, dict)]
    if len(args) > 1 or len(kwargs) > 1 or len(sys.argv) > 3:
        raise ValueError("Only one json list (args) and/or one json map (kwargs) allowed.")
    args = [] if not args else args[0]
    kwargs = {} if not kwargs else kwargs[0]
    main(*args, **kwargs)
