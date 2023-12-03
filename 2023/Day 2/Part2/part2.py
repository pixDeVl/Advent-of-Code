import re 

lines_match = r'(?<=Game )(\d+): (.*)'
blue_match = r'\d+(?=\sblue)'
green_match = r'\d+(?=\sgreen)'
red_match = r'\d+(?=\sred)'

document = open('../fulltext.txt', 'r')
lines = document.readlines()
lines_legal = []
line_dict = {}
for i in lines:
    line_run = []
    id = re.search(lines_match, i)[1]
    runs = re.search(lines_match, i)[2].split(';')
    for i in runs:
        try: num_r = int(re.search(red_match, i)[0])
        except: num_r = 0
        try: num_b = int(re.search(blue_match, i)[0])
        except: num_b = 0
        try: num_g = int(re.search(green_match, i)[0])
        except: num_g = 0
        line_run.append([int(num_r), int(num_g), int(num_b)])
    line_dict[int(id)] = line_run
print(line_dict)
pows = []
for k, v in line_dict.items():
    legal = True
    min_red = 0
    min_green = 0
    min_blue = 0
    for run in v:
        
        print(f'run for {k}: ' + str(run))
        
        if run[0] > min_red: min_red = run[0]
        if run[1] > min_green: min_green = run[1]
        if run[2] > min_blue: min_blue = run[2]
    pow = min_blue * min_red * min_green
    pows.append(pow)
    if legal: lines_legal.append(k)
print(sum(lines_legal))
print(pows)
print(sum(pows))