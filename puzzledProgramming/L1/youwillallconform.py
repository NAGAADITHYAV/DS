def pleaseConfirmOnePass(caps):
    if not caps:
        return
    caps = caps + [caps[0]]
    start = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                start = i
            else:
                if start == i-1:
                    print(f"Person at position {start} flip your cap!")
                else:
                    print(f"People in positions {start} through {i-1} flip your caps!")

def pleaseConfirm(caps):
    start = forward = backward = 0
    intervals = []
    if not caps:
        return

    caps = caps+ [caps[0]]
    
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    if forward > backward:
        flip = 'F'
    else:
        flip = 'B'
    
    for start, end, direction in intervals:
        if direction == flip:
            if start == end:
                print(f"Person at position {start} flip your cap!")
            else:
                print(f"People in positions {start} through {end} flip your caps!")

def pleaseConfirmBareHeads(caps):
    start = forward = backward = 0
    intervals = []
    if not caps:
        return

    caps = caps+ [caps[0]]
    
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    if forward > backward:
        flip = 'F'
    else:
        flip = 'B'
    
    for start, end, direction in intervals:
        if direction == flip:
            if start == end:
                print(f"Person at position {start} flip your cap!")
            else:
                print(f"People in positions {start} through {end} flip your caps!")
    

# caps = list('FFBBBFBBBFFBF')
# pleaseConfirmOnePass(caps)
# pleaseConfirm(caps)

# caps = list('')
# pleaseConfirmOnePass(caps)
# pleaseConfirm(caps)

# caps = list('FBFB')
# pleaseConfirmOnePass(caps)
# pleaseConfirm(caps)

# caps = list('FFBHBFBBBFFBF')
# # pleaseConfirmOnePass(caps)
# pleaseConfirmBareHeads(caps)

def runlenEncode(s):
    if not s:
        return
    s = s + s[0]
    start = 0
    splits = []
    for i in range(1,len(s)):
        if s[i] != s[start]:
            splits.append((start, i-1, s[i-1]))
            start = i
    
    res = '' 
    for start, end, char in splits:
        res = res + f"{end-start+1}{char}"
    return res

def runlenDecode(s):
    times_string = ''
    res = ''
    for char in s:
        if char.isalpha():
            res += char*int(times_string)
            times_string = ''
        else:
            times_string += char
    return res

s = 'WWWWWWWWWWBBBBBBWWBBWBWBWBWBWBWB'
print(s)
res = runlenEncode(s)
print(res)
res2 = runlenDecode(res)
print('r',res2)
print('s', s)