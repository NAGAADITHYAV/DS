"""
You are given a schedule of celebritites
schedule = [(6,8), (9,10)]
find the interval (exaxt-time) when you need to attend to get maximum selfies with celebrities.
optimize 
break all the ins and outs of he celebrities into a times array with (time, 'in'/'out')
now sort them 
  and keep track of counts, in and out in will increase the count and out will decrease the count 
  keep track of maximum it will be the answer.
calulate ceelbrity density at each time and select the max
"""

def chooseTime(times):
  count, maxcount = 0 ,0
  time  = 0
  for t, action in times:
    if action == 'E':
      count -= 1
    else:
      count += 1
    if count > maxcount:
      maxcount = count
      time = t
  return [maxcount, time]

def bestTimeToParty(schedule):
  times = []
  for c in schedule:
    times.append((c[0], 'I'))
    times.append((c[1], 'E'))
  times.sort()
  print(times)
  maxcount, time = chooseTime(times)
  print(f"Best time to attend the party is {time} o'clock : {maxcount} Celebriites will be attending!")

    

schedule = [(6,8), (6,12), (6,7), (7,8), (7,10), (8, 9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]
bestTimeToParty(schedule)