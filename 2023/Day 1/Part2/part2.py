import regex

match_statment = r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)'

def to_ints(text: list) -> list:
    guh = []
    for num in text:
        gah = num.replace('one', '1')\
        .replace('two', '2')\
        .replace('three', '3')\
        .replace('four', '4')\
        .replace('five', '5')\
        .replace('six', '6')\
        .replace('seven', '7')\
        .replace('eight', '8')\
        .replace('nine', '9')
        guh.append(gah)
    return guh

document = open('../fulldoc.txt', 'r') # Path to your txt file here, just copy pasted from the input provided
garbeld_values = document.readlines()

combined_list = []

for value in garbeld_values:
    print(regex.findall(match_statment, value.replace('\n', ''), overlapped=True))
    converted = to_ints(regex.findall(match_statment, value.replace('\n', ''), overlapped=True))
    combined = converted[0] + converted[-1]
    combined_list.append(int(combined))

print(sum(combined_list))