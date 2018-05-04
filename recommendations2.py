

# 영화 비평과 영화 평가 정보를 담는 딕셔너리
moviesgrade={'Lady in the Water': {'Lisa Roser': 2.5, 'Gene Seymour': 3.0, 'Michael Phillips': 2.5, 'Mick LaSalle': 3.0, 'Jack Matthews': 3.0},
        'Snakes on a Plane': {'Lisa Roser': 3.5, 'Gene Seymour': 3.5, 'Michael Phillips': 3.0, 'Claudia Puig': 3.5, 'Mick LaSalle': 4.0, 'Jack Matthews': 4.0, 'Toby': 4.5},
        'Just My Luck': {'Lisa Roser': 3.0, 'Gene Seymour': 1.5, 'Claudia Puig': 3.0, 'Mick LaSalle': 2.0},
        'Superman Returns': {'Lisa Roser': 3.5, 'Gene Seymour': 5.0, 'Michael Phillips': 3.5, 'Claudia Puig': 4.0, 'Mick LaSalle': 3.0, 'Jack Matthews': 5.0, 'Toby': 4.0},
        'You, Me and Dupree': {'Lisa Roser': 2.5, 'Gene Seymour': 3.5, 'Claudia Puig': 2.5, 'Mick LaSalle': 2.0, 'Jack Matthews': 3.5, 'Toby': 1.0},
        'The Night Listener': {'Lisa Roser': 3.0, 'Gene Seymour': 3.0, 'Michael Phillips': 4.5, 'Claudia Puig': 4.5, 'Mick LaSalle': 3.0, 'Jack Matthews': 3.0},
        'Superman Returns': {'Lisa Roser': 3.5, 'Gene Seymour': 5.0, 'Michael Phillips': 3.5, 'Claudia Puig': 4.0, 'Mick LaSalle': 3.0, 'Jack Matthews': 5.0, 'Toby': 4.0}}

from math import sqrt

def transformPrefs(prefs) :
    result={}
    for movie in prefs:
        for item in prefs[movie]:
            result.setdefault(item, {})

            # 물건과 사람을 바꿈
            result[item][movie]=prefs[movie][item]
    return result
