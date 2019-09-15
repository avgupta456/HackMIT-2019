import enchant, difflib

d = enchant.Dict("en_US")

def complete(str):
    out = ""
    for s in str.split(" "):
        out += __complete__(s) + " "
    return out

def __complete__(str):
    try:
        dict, max = {}, 0
        a = set(d.suggest(str))

        for b in a:
           tmp = difflib.SequenceMatcher(None, str, b).ratio();
           dict[tmp] = b
           if tmp > max: max = tmp

        return dict[max]
    except KeyError:
        return str
