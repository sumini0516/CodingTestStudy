def solution(genres, plays):
    answer = []
    genre_list = []
    dict = {}
    for g in range(len(genres)):
        genre = genres[g]
        if genre in dict:
            dict[genre] += [[plays[g], g]]
        else:
            dict[genre] = [[plays[g], g]]

    for genre in dict:
        total = 0
        dict[genre].sort(key=lambda x: (-x[0], x[1]))
        for play in dict[genre]:
            total += play[0]
        genre_list.append([total, genre])
    genre_list.sort(reverse=True)

    for select in genre_list:
        genre = select[1]
        if len(dict[genre]) == 1:
            answer.append(dict[genre][0][1])
        else:
            answer.append(dict[genre][0][1])
            answer.append(dict[genre][1][1])

    return answer