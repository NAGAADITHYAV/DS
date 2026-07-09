"""
You are given a schedule of celebritites
schedule = [(6,8), (9,10)]
find the interval (exaxt-time) when you need to attend to get maximum selfies with celebrities.
Brute force
calulate ceelbrity density at each time and select the max
"""
def celebrityDensity(schedule, start, end):
  count = [0]*(end+1)
  for i in range(start, end+1):
    count[i]=0
    for c in schedule:
      if c[0]<=i and c[1]>i:
        count[i] += 1
  return count

def bestTimeToParty(schedule):
  start = schedule[0][0]
  end = schedule[0][1]

  for c in schedule:
    if start > c[0]:
      start = c[0]
    if end < c[1]:
      end  = c[1]
  
  count = celebrityDensity(schedule, start, end)

  maxcount = 0
  time = start
  for i in range(start, end+1):
    if count[i] > maxcount:
      maxcount = count[i]
      time = i
    
  print(f"Best time to attend the party is {time} o'clock : {maxcount} Celebriites will be attending!")

    

schedule = [(6,8), (6,12), (6,7), (7,8), (7,10), (8, 9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]
bestTimeToParty(schedule)