from recommendations import critics
from recommendations import sim_distance
from recommendations import sim_pearson
from recommendations import pearsonTopMatches
from recommendations import distanceTopMatches
from recommendations import getRecommendations

print(critics['Lisa Rose']['Lady in the Water'])

critics['Toby']['Snakes on a Plane']=5.0
print(critics['Toby'])

result = {'euclidean distance socre' : sim_distance(critics, 'Lisa Rose', 'Gene Seymour')}
print(result)
result = {'Pearson correlation score' : sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')}
print(result)

print(distanceTopMatches(critics, 'Toby', n=3))
print(pearsonTopMatches(critics, 'Toby', n=3))
print('-------------------------------------')
print(getRecommendations(critics, 'Toby'))
print('-------------------------------------')
print('-------------------------------------')
print(getRecommendations(critics, 'Toby', similarity=sim_distance))
