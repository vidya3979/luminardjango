from functools import*

isl=[
    {"t_name":"mumbaicity","mp":7,"win":5,"drawn":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"t_name":"atk","mp":7,"win":5,"drawn":1,"loss":1,"gf":8,"ga":3,"pts":16},
    {"t_name":"benguluru","mp":7,"win":3,"drawn":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"t_name":"northeast","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"t_name":"jemshedh","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

#print all team namesin uppercase

teams=list(map(lambda team:team["t_name"].upper(),isl))
print(teams)

#print highest point
points=reduce(lambda p1,p2:p1 if p1>p2 else p2,
             list(map(lambda team:team["pts"],isl)))
print(points)

#print minimum points
min_pts=reduce(lambda p1,p2:p1 if p1<p2 else p2,
               list(map(lambda team:team["pts"],isl))
               )
print(min_pts)

#highest win team
high_won= reduce(lambda w1,w2:w1 if w1>w2 else w2,
                 list(map(lambda team:team["win"],isl))
                )
print(high_won)

won_team=list(filter(lambda team:team["win"]==high_won,isl))

print(won_team)