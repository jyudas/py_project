# 베스트앨범
import operator


def solution(genres, plays):
    set_genres = set(genres)
    list_genres = list(set_genres)
    song = []

    idx = 0

    for g in list_genres:
        plays_sum = 0
        for k in range(0, len(genres)):
            if genres[k] == g:
                plays_sum += plays[k]
                song.append([genres[k], plays[k], k])

        if idx == 0:
            dic = {g: plays_sum}
        else:
            dic[g] = plays_sum
        idx += 1

    answer = []
    result = {}
    result_order = {}
    sorted_dict = []

    for z, k in sorted(dic.items(), key=operator.itemgetter(1), reverse=True):

        del sorted_dict[:]

        for m in range(0, len(song)):
            if song[m][0] == z:
                # print("{}번째{}".format(m,song[m]))
                result[song[m][2]] = song[m][1]
        sorted_dict = list(sorted(result.items(), key=operator.itemgetter(1), reverse=True))

        tot_idx = 0

        for key, value in sorted_dict:
            if tot_idx < 2:
                answer.append(key)
                tot_idx += 1
        result.clear()

    return answer


# 다른풀이
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer