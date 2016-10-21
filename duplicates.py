#!/usr/bin/env python3

import os
import argparse
from hashlib import sha1


def _create_duplicates_tree(directory):
    tree = {}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                stat = os.stat(filepath)
            except FileNotFoundError:
                continue

            file_hash = sha1(
                bytes("%s-%s" % (filename, stat.st_size), "utf-8")
            ).hexdigest()

            if tree.get(file_hash, None) is None:
                tree[file_hash] = [filepath]
            else:
                tree[file_hash].append(filepath)

    return tree


def get_duplicates(directory):
    dup_tree = _create_duplicates_tree(directory)

    return list(filter(lambda it: len(it) > 1, dup_tree.values()))


def main():
    description = "Find duplicate files in DIRECTORY"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-d", "--directory",
        type=str,
        required=True,
        help="Directory to find duplicates"
    )

    args = parser.parse_args()
    duplicates = get_duplicates(args.directory)
    count_duplicates = len(duplicates)
    line_width = len(str(count_duplicates)) + 20

    print("Duplicates founded: {}".format(count_duplicates))
    for items in duplicates:
        print("-" * line_width)
        for item in items:
            print("* " + item)


if __name__ == '__main__':
    main()
