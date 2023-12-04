import re 
match_regex = r"Card\s*(\d+):\s*([\d\s]+)\|\s*([\d\s]*)"

doc = open('../sample.txt', 'r')
lines = doc.readlines()
print(lines)
score_dict = {}

def key_exists(id):
    try:
        score_dict[id]
        return True
    except KeyError: return False



for card in lines:
    card = card.strip()
    search = re.search(match_regex, card)
    id = search[1]
    winning_nums = search[2].strip().split(' ')
    drawn_nums = search[3].strip().split(' ')
    for i in drawn_nums:
        print(i)
        if i in winning_nums and i.isdigit(): 
            print(f'Matched {i} in card {id}')
            if not key_exists(id): score_dict[id] = 1
            else: score_dict[id] = (score_dict[id] * 2) 
print(sum(score_dict.values()))