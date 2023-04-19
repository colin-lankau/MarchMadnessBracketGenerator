'''
A class to handle the March Madness Bracket
'''
from REST.Utils.Team import Team
import random

teams = [ "Alabama", "Texas A&M-CC", "Maryland", "West Virginia", "San Diego St.", "Col of Charleston", "Virginia", "Furman", "Creighton", "NC State", "Baylor", "UCSB", "Missouri", "Utah St.", "Arizona", "Princeton",
        "Purdue", "FDU", "Memphis", "FAU", "Duke", "Oral Roberts", "Tenesee", "Louisiana", "Kentucky", "Providence", "Kansas St.", "Montana St.", "Michigan St.", "USC", "Marquette", "Vermont",
        "Houston", "N Kentucky", "Iowa", "Auburn", "Miami (FL)", "Drake", "Indiana", "Kent St.", "Iowa St.", "Pitt", "Xavier", "Kennesaw St.", "Texas A&M", "Penn St.", "Texas", "Colgate",
        "Kansas", "Howard", "Arkansas", "Illinois", "Saint Mary's", "VCU", "UConn", "Iona", "TCU", "Arizona St.", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St.", "UCLA", "UNC Asheville"
    ]

class Bracket:

    seeds = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]*4
    teams = teams

    def __init__(self):
        # rounds is [ r64, r32, s16, e8, f4, final, champion]
        self.rounds = [
            [ Team(team, seed) for team, seed in zip(self.teams, self.seeds) ], 
            [],
            [],
            [],
            [],
            [],
            []
        ]

    def view_bracket(self):
        for m in range(0, len(self.rounds), 1):
            for i in range(0, len(self.rounds[m]), 2):
                print(f"-----GAME {i//2+1}----")
                print(f"{self.rounds[m][i].name} ({self.rounds[m][i].seed}) vs. {self.rounds[m][i+1].name} ({self.rounds[m][i+1].seed})")

    def pickWinner(self, didTopWin, m, i):
        if didTopWin:
            self.rounds[m].append(self.rounds[m-1][i])
        else:
            self.rounds[m].append(self.rounds[m-1][i+1])
        # if top:
        #     if m == 0: self.round_of_32.append(previous_round[i])
        #     elif m == 1: self.sweet_16.append(previous_round[i])
        #     elif m == 2: self.elite_eight.append(previous_round[i])
        #     elif m == 3: self.final_four.append(previous_round[i])
        #     elif m == 4: self.championship_game.append(previous_round[i])
        #     elif m == 5: self.CHAMPION = f"{previous_round[i].seed}) {previous_round[i].name}"
        # elif bottom:
        #     if m == 0: self.round_of_32.append(previous_round[i+1])
        #     elif m == 1: self.sweet_16.append(previous_round[i+1])
        #     elif m == 2: self.elite_eight.append(previous_round[i+1])
        #     elif m == 3: self.final_four.append(previous_round[i+1])
        #     elif m == 4: self.championship_game.append(previous_round[i+1])
        #     elif m == 5: self.CHAMPION = f"{previous_round[i+1].seed}) {previous_round[i+1].name}"

    def generate_rounds(self, odds, bias, pref, winner=None):
        print(pref)
        for m in range(1, len(self.rounds), 1):
            for i in range(0, len(self.rounds[m-1]), 2):
                # handle force winner
                if (a := self.rounds[m-1][i].name == winner) or self.rounds[m-1][i+1].name == winner:
                    self.pickWinner(a, m, i)
                else:
                    top_odds = int(odds[m-1][ self.rounds[m-1][i].seed ].strip('%'))
                    bottom_odds = int(odds[m-1][ self.rounds[m-1][i+1].seed ].strip('%'))
                    # handle bias level
                    # if top team is fav, else if bottom team is fav
                    if top_odds > bottom_odds:
                        if bias > 0:
                            top_odds += bias
                        else:
                            bottom_odds += -1 * bias
                    else: 
                        if bias > 0:
                            bottom_odds += bias
                        else:
                            top_odds += -1 * bias
                    if bottom_odds == 0: bottom_odds += 1
                    # handle preferences
                    if pref:
                        if self.rounds[m-1][i].name in pref:
                            top_odds += 50
                        elif self.rounds[m-1][i+1].name in pref:
                            bottom_odds += 50
                    adjusted_odds = int( (top_odds / (top_odds + bottom_odds) ) * 100)
                    # print(adjusted_odds)
                    a = adjusted_odds > int(random.random()*100)
                    self.pickWinner(a, m, i)