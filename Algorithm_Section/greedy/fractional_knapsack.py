from typing import List, Tuple, Dict


def f_n(list_of_weight_val_tuple: List[Tuple], capacity: int) -> Dict:
    density = []
    for elm in list_of_weight_val_tuple:
        density.append((elm, elm[1]/elm[0]))  # [((3, 4), 4/3)]

    sorted_density = sorted(density, key=lambda x: x[1], reverse=True)

    max_val = 0
    result = {}
    while capacity:
        eshgham_behtarin = sorted_density.pop(0)[0]
        weight = eshgham_behtarin[0]
        value = eshgham_behtarin[1]
        if capacity >= weight:
            result[eshgham_behtarin] = 1
            max_val += value
            capacity -= weight
        else:
            fraction = capacity/weight
            result[eshgham_behtarin] = fraction
            max_val += fraction * value
            capacity = 0
    return result, max_val


data = [(4, 5), (3, 7), (2, 2), (7, 3)]
W = 1

print(f_n(data, W))
