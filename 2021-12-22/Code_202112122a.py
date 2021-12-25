import re

def intersect(c1, c2, f = 1):
    xl = max(c1[0], c2[0])
    xh = min(c1[1], c2[1])
    yl = max(c1[2], c2[2])
    yh = min(c1[3], c2[3])
    zl = max(c1[4], c2[4])
    zh = min(c1[5], c2[5])
    if xl > xh or yl > yh or zl > zh:
        return None
    return (xl, xh, yl, yh, zl, zh, -c1[6]*f)

def addCube(cubelist, cube):
    applist = []
    for c in cubelist:
        ci = intersect(c, cube)
        if ci is not None:
            applist.append(ci)
    if cube[6] > 0:
        cubelist.append(cube)
    for c in applist:
        cubelist.append(c)


def size(cube):
    return cube[6]*(cube[1]-cube[0]+1)*(cube[3]-cube[2]+1)*(cube[5]-cube[4]+1)

def countOn(cubelist):
    lights = 0
    for cube in cubelist:
        lights += size(cube)
    return lights

def main():
    inputlist = []
    with open('Data.txt', 'r') as file:
        for line in file:
            toks = re.split(' x=|\.\.|,y=|,z=|\s', line)
            if toks[0] == 'on':
                inputlist.append((int(toks[1]), int(toks[2]),\
                                 int(toks[3]), int(toks[4]),\
                                 int(toks[5]), int(toks[6]), 1))
            else:
                inputlist.append((int(toks[1]), int(toks[2]),\
                                 int(toks[3]), int(toks[4]),\
                                 int(toks[5]), int(toks[6]), -1))
    cubelist = []
    workspace = (-50, 50, -50, 50, -50, 50, 1)
    for cube in inputlist:
        ci = intersect(cube, workspace, -1)
        if ci is not None:
            addCube(cubelist, cube)
        if len(cubelist) > 10000000:
            break
    print(len(cubelist))
    print(countOn(cubelist))
if __name__ == "__main__":
    main()
    
