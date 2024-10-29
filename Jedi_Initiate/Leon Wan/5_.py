def midi_chlorians(n):
    start = [0, 1] 
    for i in range(n):
        f = start[i] + start[i+1]
        start.append(f)
    print(start[n])
        

midi_chlorians(4)

