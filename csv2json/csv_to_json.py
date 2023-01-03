import csv, json, sys
from pathlib import Path
from collections import OrderedDict
from pprint import pprint
from dataclasses import asdict, fields

from data_structures import *

# This is a program that reads in a csv file and outputs the data into json based on some data structures defined in data_structures.py

# IO FUNCTIONS
def output_json(items_dict, out_file):
    with out_file.open('w') as fo:
        json.dump(items_dict, fo, indent=4)
        print(f"Wrote to {out_file}")

def get_from_csv(in_file: str):
    csv_file = Path(in_file)
    with csv_file.open() as fo:
        return [l for l in csv.reader(fo, delimiter=',', quotechar='"')]

# DEBUG
def sanity_check(d: list, length: int, fn: str):
    for idx, l in enumerate(d):
        if not len(l) == length:
            print(f"{fn} - {idx}: {l[0]} - length: {length}")
            sys.exit(1)
    print(f"All are length {length}")


# MAIN
for fstem in [f.stem for f in Path.cwd().glob('*.csv')]:
    csv_input = f"{fstem}.csv"
    print(f"Working on {csv_input}")
    json_output = f"../generator/json/{fstem}.json"

    DataStructure = None
    if fstem.lower() in ("armor", "helmets", "relics", "shields"):
        DataStructure = DefenseEquip
    if "items" in fstem.lower():
        DataStructure = Item
    if "legend" in fstem.lower():
        DataStructure = Legend
    if "weapon" in fstem.lower():
        DataStructure = Weapon
    if "enem" in fstem.lower():
        DataStructure = Enemy
    if "slot" in fstem.lower():
        DataStructure = SlotSkill
    if "dance-actions" in fstem.lower():
        DataStructure = Skill
    if "rage-actions" in fstem.lower():
        DataStructure = RageAction
    if "rage-prop" in fstem.lower():
        DataStructure = RageProp

    # Insert Your Condition Here

    if DataStructure is None:
        print("Cannot determine data structure from file name")
        sys.exit(1)
    lines_raw = get_from_csv(csv_input)
    sanity_check(lines_raw, len(fields(DataStructure)), fstem)
    heading = [asdict(DataStructure(*lines_raw[0]))]
    items = sorted(
        [asdict(DataStructure(*l)) for l in lines_raw[1:]],
        key=lambda d: d["name"]
    )
    output_json(
        heading + items,
        Path(json_output)
    )

