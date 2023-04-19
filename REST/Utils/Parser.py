'''
Utility module for parsing data
'''

# generate list of each round
# each round is stored as a dictionary
def parse(data):

    with open(data) as file:
        lines = [line[:-1] for line in file if line[:-1]]

    rounds = [ i for i, n in enumerate(lines) if n == 'Win %' ]
    results = [ {} for i in range(6) ]

    for m in range(6):
        for i in range(16):
            seed = int(lines[ (rounds[m]+1) + (i*4) ])
            win_odds = lines[ (rounds[m]+1) + 3 + (i*4)]
            results[m][seed] = win_odds
        
    return results