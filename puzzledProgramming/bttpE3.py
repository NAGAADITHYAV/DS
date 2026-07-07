"""
we have scheule along with weight 
[(6,8,3), (7,9,1)]
where (start, end, weight) wheight is how much do you want to meet the celebrity. maximizie the total weight. 
instead no of selfies possibel
"""
def bestTimeToParty(schedule):
  maxcount = 0
  time = 0

  for start, _, _ in schedule:
    count = sum( weight
      for celebrity_start, celebrity_end, weight in schedule if celebrity_start <= start < celebrity_end
    )

    if count > maxcount:
      maxcount = count
      time = start

  print(f"Best time to attend the party is {time} o'clock : {maxcount} Celebriites will be attending!")

sched = [(6,8,2), (6.5,12,1), (6.5,7,2), (7,8,2),(7.5,10, 3), (8,9,2), (8,10,1), (9,12,2), (9.5,10,4), (10,11,2),(10,12,3), (11,12,7)]
#ans 11, 13
bestTimeToParty(sched)