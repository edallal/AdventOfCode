from queue import PriorityQueue

def tryNeighbour(mat, x, y, dx, dy, dist, pq):
    xnext = x + dx
    ynext = y + dy
    if xnext >= 0 and xnext < len(mat)\
    and ynext >= 0 and ynext < len(mat[0]):
        alt = dist[(x, y)] + mat[xnext][ynext]
        if alt < dist[(xnext, ynext)]:
            dist[(xnext, ynext)] = alt
            pq.put((alt, (xnext, ynext)))

def dijkstra(mat):
    dist = {}
    maxDist = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dist[(i, j)] = float('infinity')
    pq = PriorityQueue()
    dist[(0,0)] = 0
    pq.put((0, (0,0)))

    while not pq.empty():
        u = pq.get()
        x = u[1][0]
        y = u[1][1]
        if dist[(x, y)] != u[0]:
            continue
        tryNeighbour(mat, x, y, -1, 0, dist, pq)
        tryNeighbour(mat, x, y, 1, 0, dist, pq)
        tryNeighbour(mat, x, y, 0, -1, dist, pq)
        tryNeighbour(mat, x, y, 0, 1, dist, pq)
    return dist
        

def main():
    mat = []
    with open('Data.txt', 'r') as file:
        for line in file:
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            row = []
            for c in s:
                row.append(int(c))
            mat.append(row)
    dist = dijkstra(mat)
    print(dist[(len(mat)-1, len(mat[0])-1)])
            
if __name__ == "__main__":
    main()
    
