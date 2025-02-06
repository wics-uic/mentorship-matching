# Gale Shapley Algorithm Stable Matching from https://github.com/shubh11220/The-Stable-Matching-Algorithm/blob/master/Stable_Matching.py
# Initialization
Mentees= ['Mike', 'Harvey', 'Louis', 'Logan']
Mentors= ['Rachel', 'Donna', 'Katrina', 'Sheila']

# Preferences
Mentees_Pref = {  # indicates the preferences of the men
    'Mike':   ['Rachel', 'Katrina', 'Donna', 'Sheila'],
    'Harvey': ['Donna', 'Katrina', 'Rachel', 'Sheila'],
    'Louis':  ['Sheila', 'Donna', 'Katrina', 'Rachel'],
    'Logan':  ['Rachel', 'Katrina', 'Donna', 'Sheila']
}

Mentors_Pref = {  # indicates the preferences of the women
    'Rachel':  ['Mike', 'Logan', 'Harvey', 'Louis'],
    'Donna':   ['Harvey', 'Louis', 'Mike', 'Logan'],
    'Katrina': ['Mike', 'Harvey', 'Louis', 'Logan'],
    'Sheila':  ['Louis', 'Logan', 'Harvey', 'Mike']
}
def main():
    Mentees_Free = list(Mentees)
    Mentors_Free = list(Mentors)

    # Part 3: Proposal
    Matches = {
        'Mike':  '',
        'Harvey': '',
        'Louis': '',
        'Logan': ''
        }
    key_list = list(Matches.keys())

    # the algorithm

    while len(Mentees_Free) > 0:
        for mentee in key_list:
            for mentor in Mentees_Pref[mentee]:
                if mentor not in list(Matches.values()):
                    Matches[mentee] = mentor
                    Mentees_Free.remove(mentee)
                    print('{} is tentatively matched to {} !'.format(mentee, mentor))
                    break
                elif mentor in list(Matches.values()):
                    current_suitor = list(Matches.keys())[list(Matches.values()).index(mentor)]
                    w_list = Mentors_Pref.get(mentor)
                    if w_list.index(mentee) < w_list.index(current_suitor):
                        Matches[mentee] = mentor
                        Mentees_Free.remove(mentee)
                        Matches[current_suitor] = ''
                        Mentees_Free.append(current_suitor)
                        print('{} was earlier matched to {} but now is matched to {}! '.format(mentor, current_suitor, mentee))

    print('\n ')
    print('Stable Matching Finished')
    for mentee in Matches.keys():
        print('{} is matched to {} !'.format(mentee, Matches[mentee]))


if __name__ == "__main__":
    main()