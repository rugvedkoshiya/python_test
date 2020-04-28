def avg_finder(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
print(avg_finder([1,2,3],[4,5,6],[7,8,9])) # Output : [4.0, 5.0, 6.0]

# Now we make this in one line...
new_avg = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(new_avg([1,2,3],[4,5,6],[7,8,9])) # Output : [4.0, 5.0, 6.0]