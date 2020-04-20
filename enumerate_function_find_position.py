names = ['Rugved', 'Shyam', 'Grey']
def find_pos(names,target):
    for pos, name in enumerate(names):
        if name == target:
            return pos
    return -1
print(find_pos(names,'Rugved'))