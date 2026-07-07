"""
You are given a schedule of celebritites
schedule = [(6,8), (9,10)]
find the interval (exaxt-time) when you need to attend to get maximum selfies with celebrities.


You yourself is a celebrity and you also have (intime, outtime) so calcualte the max celebrites you can meet/see
"""

def intersection(interval1, interval2):
  return not((interval1[1] <= interval2[0]) or (interval2[1] <= interval1[0]))

def bestTimeToParty(schedule, yourSchedule):
  maxcount = 0
  for celeb in schedule:
    if intersection(celeb, yourSchedule):
      maxcount += 1
  print(f"{maxcount} Celebriites will be attending!")

    

schedule = [(6,8), (6,12), (6,7), (7,8), (7,10), (8, 9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]
bestTimeToParty(schedule, (6, 12))
bestTimeToParty(schedule, (7, 12))
bestTimeToParty(schedule, (8, 12))