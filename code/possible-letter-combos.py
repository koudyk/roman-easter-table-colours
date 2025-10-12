import itertools

letters = "RGBRGB"
duples = ["RR", "GG", "BB"]

possible_combinations = {
    # 2: [],
    3: [],
    # 4: [],
}
for length in possible_combinations.keys():
    out = itertools.permutations(letters, length)
    options = []
    for item in out:
        options.append("".join(item))

    cleaned_options = []
    for option in options:
        keep = True
        for duple in duples:
            if duple in option:
                keep = False
        if keep:
            cleaned_options.append(option)

    possible_combinations[length] = cleaned_options

print(possible_combinations)
d = 1
