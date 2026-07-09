"""
we take each celebrity anf calculate their intersection with other ceelbrities 
We take the max of that their start time is the right time.
"""

def bestTimeToParty(schedule):
  maxcount = 0
  time = 0

  for start, _ in schedule:
    count = sum(
      celebrity_start <= start < celebrity_end
      for celebrity_start, celebrity_end in schedule
    )

    if count > maxcount:
      maxcount = count
      time = start

  print(f"Best time to attend the party is {time} o'clock : {maxcount} Celebriites will be attending!")

schedule = [(6,8), (6,12), (6,7), (7,8), (7,10), (8, 9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]
bestTimeToParty(schedule)