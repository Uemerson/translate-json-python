from googletrans import Translator
import json
import argparse
import os
import sys


def translate_json_recursively(data, src, dest):
    if isinstance(data, str):
        translator = Translator()
        return translator.translate(data, src=src, dest=dest).text
    elif isinstance(data, dict):
        result = {}

        for key, item in data.items():
            result.update({key: translate_json_recursively(item, src, dest)})

        return result
    elif isinstance(data, list):
        result = []

        for item in data:
            result.append(translate_json_recursively(item, src, dest))

        return result
    else:
        return data


def main():
    parser = argparse.ArgumentParser(description="A program to translate a JSON file.")

    parser.add_argument(
        "-i",
        "--ifile",
        metavar="path",
        type=str,
        required=True,
        help="JSON file path to be translated.",
    )
    parser.add_argument(
        "-o",
        "--ofile",
        metavar="path",
        type=str,
        required=True,
        help="translated JSON file path to be saved.",
    )
    parser.add_argument(
        "-s",
        "--src",
        type=str,
        required=False,
        help="the source language you want to translate. (Default: auto)",
    )
    parser.add_argument(
        "-d",
        "--dest",
        type=str,
        required=False,
        help="the destination language you want to translate. (Default: en)",
    )

    args = parser.parse_args()

    if not os.path.isfile(args.ifile):
        print("the specified input file does not exist")
        sys.exit()

    src = "auto" if args.src == None else args.src
    dest = "en" if args.dest == None else args.dest

    inputfile = json.load(open(args.ifile))
    print("working on translations ...")

    translate_json = translate_json_recursively(inputfile, src, dest)

    with open(args.ofile, "w", encoding="utf-8") as f:
        json.dump(translate_json, f, ensure_ascii=False, indent=2)

    print(f"translated JSON file saved as {args.ofile}")


if __name__ == "__main__":
    main()
