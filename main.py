import sys
import json


def main(*args, **kwargs):
    print("Hello world from a public repo (dev branch)!")
    print(f"Here are the positional args: {args}")
    print(f"Here are the named args: {kwargs}")


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
