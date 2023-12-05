""" A améliorer: ajouter des règles, ex ne pas autoriser que a->b si b->a already + ne pas autoriser certaines relations ex: on ne veut pas que c offre à d """

import argparse
import random
from name_encoder import NameEncoder
from names import get_names


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--participants', type=str, default="participants.txt", required=True)
parser.add_argument('-v', '--shift-value', type=int, default=3, help="shift value to use for the Cesar cipher", dest="shift_value")
args = parser.parse_args()


def get_assignment(names) -> list:
    """ Shuffles the input list until each name is matched to a different name than itself. """

    candidate = get_candidate(names)
    while not is_good_partition(candidate):
        candidate = get_candidate(names)

    return candidate


def is_good_partition(names_list: list):
    """ Tests that each name has not been matched with itself. """

    for i, name in enumerate(names_list):
        if i == original[name]:
            return False
    return True


def get_candidate(l: list):
    c = l.copy()
    random.shuffle(c)
    return c


if __name__ == "__main__":

    names = get_names(args.participants)

    indices = list(range(len(names)))
    original = dict(zip(names.copy(), indices))
    print(original)

    assignment = get_assignment(names)

    print(f"\nFound a solution:")
    for name, idx in original.items():
        print(f"{name} -> {assignment[idx]}")

    print(f"\nEncoding result...")
    encoder = NameEncoder(code=args.shift_value)
    max_length = max([len(n) for n in assignment])
    encoded_res = { name: encoder.encode_name(assignment[idx], max_length) for name, idx in original.items() }

    print(f"\nResult:")
    for k, v in encoded_res.items():
        print(f"{k} -> {v}")
