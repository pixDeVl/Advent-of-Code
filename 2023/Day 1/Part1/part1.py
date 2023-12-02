def is_int(char: str) -> bool:
    try:
        int(char)
    except ValueError:
        return False
    return True


document = open('./fulldoc.txt', 'r') # Path to your txt file here, just copy pasted from the input provided
garbeld_values = document.readlines()

combined_list = []

for value in garbeld_values:
    exploded = list(value.replace('\n', ""))
    exploded_ints = [*filter(is_int, exploded)]
    combined = exploded_ints[0] + exploded_ints[-1]
    combined_list.append(int(combined))

print(sum(combined_list))
