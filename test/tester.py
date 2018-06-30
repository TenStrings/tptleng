#!/usr/bin/env python3
import yaml
import json
import sys

def main(original, converted):
    with open(original, "r") as f1:
        with open(converted, "r") as f2:
            js = json.load(f1)
            ym = yaml.load(f2)
            print(js == ym)

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Deben ingresarse dos archivos")

    main(sys.argv[1], sys.argv[2])
