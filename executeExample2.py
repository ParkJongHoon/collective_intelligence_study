from recommendations import critics
from recommendations2 import moviesgrade
from recommendations import sim_distance
from recommendations import sim_pearson
from recommendations import topMatches
from recommendations import pearsonTopMatches
from recommendations import distanceTopMatches
from recommendations import getRecommendations
from recommendations2 import transformPrefs

#print(distanceTopMatches(critics, 'Toby', n=3))



# transformPrefs()는 Map 객체의 key값과 value값을 교환함
movies=transformPrefs(critics)
# Superman Returns과 유사한 영화 top 3
print(topMatches(movies, 'Superman Returns', 2))

# 평론가 추천
print(getRecommendations(movies, 'Just My Luck'))
