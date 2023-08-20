# 5 Students and 5 Places
s = [1, 2, 3, 4, 5]  # student index
p = [1, 2, 3, 4, 5]  # place index
# indicators by which each s chooses a p
# each s ranks all the p
# indicators by which each p chooses a s
# each p ranks all the s
number = 0
# input rankings by each person
# for person in s:
#    pranks = input("Input your ranks for P:")
#    pranks = pranks.split(',')
#    for number in range(len(pranks)):
#        pranks[number] = int(pranks[number])
#    srankings += [pranks]
# for person in p:
#    sranks = input("Input your ranks for S:")
#    sranks = sranks.split(',')
#    for number in range(len(sranks)):
#        sranks[number] = int(sranks[number])
#    prankings += [sranks]
srankings = [[2, 1, 3, 4, 5], [3, 2, 1, 4, 5], [4, 5, 1, 3, 2], [5, 4, 1, 3, 2], [4, 2, 3, 1, 5]]
prankings = [[4, 2, 3, 1, 5], [2, 1, 4, 5, 3], [3, 1, 4, 5, 2], [2, 1, 3, 4, 5], [4, 5, 3, 2, 1]]
pairs = [[0, 0]]  # where each pair consists of [s, p]
print("The first pair is ", [pair[0] for pair in pairs])
print("The second pair is ", [pair[1] for pair in pairs])
while len(pairs) < 6:
    for person in s:
        print("S person is:", person)
        preference_rank = 0
        while person not in [pair[0] for pair in pairs]:
            print("S Person is", person, "and their preference rank is", preference_rank)
            s_person_rankings = srankings[person-1]
            print("Their rankings are", s_person_rankings)
            preference = s_person_rankings[preference_rank]
            print("Their P preference is", preference)
            print("P's who are already taken: ", [pair[1] for pair in pairs])
            if preference not in [pair[1] for pair in pairs]:  # p person is free as well
                pairs.append([person, preference])
                print("Official pairs are: ", pairs)
                preference_rank = -1
                continue
            elif preference in [pair[1] for pair in pairs]:  # p person is not free, so check p person's rankings
                p_persons_in_pair_list = [pair[1] for pair in pairs]
                preference_index_in_pair_list = p_persons_in_pair_list.index(preference)
                pair_mate = pairs[preference_index_in_pair_list][0]  # s person already matched to p
                preference_rankings = prankings[preference-1]
                print("P Person rankings are", preference_rankings)
                if preference_rankings.index(person) < preference_rankings.index(pair_mate):
                    print("P Person", preference, "prefers S Person", person, "over current pair mate S Person", pair_mate)
                    pairs[preference_index_in_pair_list][0] = person  # match new s person to p instead
                    print("S Person", person, "took over", "S Person ", pair_mate)
                    preference_rank = -1
                else:
                    print("P Person", preference, "prefers current S Person", pair_mate, "over new S Person", person)
            preference_rank += 1

pairs.remove([0, 0])
print("Final pairs are:", pairs)
