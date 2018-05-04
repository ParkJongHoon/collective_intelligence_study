# 영화 비평과 영화 평가 정보를 담는 딕셔너리
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
        'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,  'You, Me and Dupree': 2.5},
        'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,  'You, Me and Dupree': 2.0},
        'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
        'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0 }}

from math import sqrt
# 유클리디안 거리점수 공식 메소드
# return값이 1에 가까울수록 동일한 선도호를 갖는다.
# return값이 0에 가까울수록 두 비교체의 선호도가 없다.
def sim_distance(prefs,person1,person2):
    # 공통 항목 목록 추출
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    print("si: ")
    print(si)
    # 공통 평가 항목이 없는 경우 0 리턴
    if len(si)==0: return 0

    # 모든 차이 값의 제곱을 더함
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                    for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))

# p1과 p2에 대한 피어슨 상관계수를 리턴
# return 값의 범위는 -1~1 사이이다
# return 값이 1이면 두 비교체의 속성 전체의 값이 같다
# return 값이 -1이면 두 비교체의 속성 전체의 값이 다르다
def sim_pearson(prefs,p1,p2):
    # 같이 평가한 항목들의 목록을 구함
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    # 요소들의 개수를 구함
    n=len(si)

    # 공통 요소가 없으면 0 리턴
    if n==0: return 0

    # 모든 선호도를 합산함
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    # 제곱의 합을 계산
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    # 곱의 합을 게산
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    # 인자값을 정의하는 구간에서 정의가 아래와 같이 가능하다
    scores=[(similarity(prefs, person, other), other)
                for other in prefs if other != person]
    # 최고점이 상단에 오도록 목록을 정렬
    #print(scores)
    # sort는 정렬인데, 낮은 차순으로 정렬을 한다
    scores.sort()
    #print(scores)
    #낮은 차순 역전하기 위해서 reverse를 사용한다
    scores.reverse()
    #print(scores)
    # scores[0:n] 의 의미
    # 정렬이 된 scores 라면 [첫번째 인자값: 두번째 인자값]
    # 두번째 인자값은 정렬된 상태에서 차례대로 출력할 개수를 의미한다
    # 첫번째 인자값은 개수를 자를경우 개층을 의미한다
    return scores[0:n]

# 유클리디안 거리점수를 이용평론가 순위 매기는 메소드
def distanceTopMatches(prefs, person, n=5, similarity=sim_distance):
    scores=[(similarity(prefs, person, other), other) for other in prefs if other != person]

    # 최고점이 상단에 오도록 목록을 정렬
    scores.sort()
    scores.reverse()
    return scores[0:n]
# 피어슨 상관점수를 이용평론가 순위 매기는 메소드
def pearsonTopMatches(prefs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(prefs, person, other), other) for other in prefs if other != person]

    # 최고점이 상단에 오도록 목록을 정렬
    scores.sort()
    scores.reverse()
    return scores[0:n]

# 다른 사람과의 순위의 가중평균값을 이용해서 특정 사람에 추천
# similarity=sim_pearson 함수 바꿔치기가 가능
def getRecommendations(prefs, person, similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        #나와 나를 비교하지 말 것
        print('other1: ' + other);
        if other == person : continue
        sim=similarity(prefs,person,other)
        # 0 이하 점수는 무시함

        if sim<=0:
            print('continue person: ' +other)
        if sim<=0:  continue
        for item in prefs[other]:
            # 내가 보지 못한 영화만 대상
            print('other: ' + other)
            print('item: ' + item)
            if item not in prefs[person] or prefs[person][item] == 0:
                # 유사도 * 점수
                if not totals:
                    print('--------------totals-------------')
                    print(totals)
                    print('---------------------------------')
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                print('--------------totals-------------')
                print(totals)
                print('---------------------------------')



                if not simSums:
                    print('--------------simSums-------------')
                    print(simSums)
                    print('---------------------------------')
                # 유사도 합계
                simSums.setdefault(item,0)
                simSums[item]+=sim
                print('--------------simSums-------------')
                print(simSums)
                print('---------------------------------')

    # 정규화된 목록 생성

    rankings=[(item,total/simSums[item]) for item, total in totals.items()]

    # 정렬된 목록 리턴
    rankings.sort()
    rankings.reverse()
    return rankings
