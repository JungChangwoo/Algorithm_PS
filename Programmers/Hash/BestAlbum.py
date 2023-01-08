from collections import defaultdict
def solution(genres, plays):
    list_dict, count_dict = defaultdict(list),  defaultdict(int)
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        list_dict[genre].append((play, i))
        count_dict[genre] += play
        
    count_dict = sorted(list(count_dict.items()), key = lambda x: x[1], reverse = True)
    for genre, play in list_dict.items():
        list_dict[genre] = sorted(play, key = lambda x: (x[0], -x[1]), reverse = True)
        
    result = []
    for genre, play in count_dict:
        temp = list_dict[genre]
        if len(temp) == 1:
            result.append(temp[0][1])
        else:
            for i in range(2):
                result.append(temp[i][1])
    return result