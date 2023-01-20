from itertools import permutations
import random


def generate_calendar(teams: list[int], id_championship: int):
    for x in teams:
        if x == 99 or x == 98:
            print( "ALERTE VERTE")       

    list_matches = list(permutations(teams, 2))
    random.shuffle(list_matches)
    final_matches = list()
    for x in range(0, len(list_matches), 2):
        final_matches.append((list_matches[x], list_matches[len(list_matches)-x-1], id_championship))
        if(list_matches[x] == 99 or list_matches[x] == 98) or (list_matches[len(list_matches)-x-1] == 98 or list_matches[len(list_matches)-x-1] == 99):
            print("ALERTE BLEUE")
    return (id_championship, final_matches)    

def generate_all_calendars(teams_per_championship):
    matches_per_championship = []
    for championship in teams_per_championship:
        matches_per_championship.append(generate_calendar(teams_per_championship[championship], championship))
    
    matches = list()
    
    for journee in range(380//2):
        matches.append(list())
        for championnat in range(5):
            matches_champ = matches_per_championship[championnat][1][journee]
            matches[journee].append(matches_champ[0])
            matches[journee].append(matches_champ[1])
    for x in range(len(matches)):
        tmp = tuple(matches[x])
        matches[x] = tmp
    return matches

