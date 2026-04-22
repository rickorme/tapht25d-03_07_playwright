import re

pattern = r"\d+\s?c?m"
string = "Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."
matches = re.findall(pattern,string)

# set the pattern for extracting the unit
unit_pattern = "c?m"
mismatch = False

for match_idx in range(len(matches)):
    
    unit_match = re.search(unit_pattern, matches[match_idx])
    unit = unit_match[0]
    print(unit)
    if match_idx == 0:
        previous_unit = unit

    else:
        if unit != previous_unit:
            mismatch=True
            break


if mismatch:
    print("Measurement units do not match ❌")
else:
    print("Measurement units are the same ✅")
