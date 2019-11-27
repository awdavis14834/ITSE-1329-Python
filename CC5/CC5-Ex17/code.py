def pet_nums(pets):
    counts = dict()
    for pet in pets:
        counts[pet] = count.get(pet, 0) + 1
    return counts