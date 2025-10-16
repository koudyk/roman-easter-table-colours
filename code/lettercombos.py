import itertools

LETTERS = "RGBRGB"
DUPLES = ["RR", "GG", "BB"]


def list_possible_letter_combinations(length=3):
    out = itertools.permutations(LETTERS, length)
    options = []
    for item in out:
        options.append("".join(item))

    cleaned_options = []
    for option in options:
        keep = True
        for duple in DUPLES:
            if duple in option:
                keep = False
        if keep:
            cleaned_options.append(option)

    unique_cleaned_options = list(set(cleaned_options))
    return unique_cleaned_options
