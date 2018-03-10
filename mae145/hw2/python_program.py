#A12141970
#! /usr/bin/env python
def computeBFStree(adjTable,start):
    Q=[]
    parent=[-1]*len(adjTable)
    Q.append(start)
    parent[start-1]=start
    while Q != []:
        v=Q.pop(0)
        for node in adjTable[v-1]:
            if parent[node-1] ==-1:
                parent[node-1]=v
                Q.append(node)
    return parent
def computeBFSpath(adjTable,start,goal):
    parent=computeBFStree(adjTable,start)
    path=[goal]
    v=goal
    while parent[v-1] !=v:
        v=parent[v-1]
        if v==-1:
            return []
        path.insert(0,v)
    return path
if __name__ == '__main__':
    start=1
    #adjTable=[[2],[1,3,4],[2,5],[2],[3]]
    adjTable = [[]] * 32
    adjTable[1-1] = [2, 6]
    adjTable[2-1] = [1, 3, 7]
    adjTable[3-1] = [2, 4, 8]
    adjTable[4-1] = [3, 5, 9]
    adjTable[5-1] = [4, 10]
    adjTable[6-1] = [1, 7, 11]
    adjTable[7-1] = [2, 6, 8]
    adjTable[8-1] = [3, 7, 9]
    adjTable[9-1] = [4, 8, 10]
    adjTable[10-1] = [5, 9, 12]
    adjTable[11-1] = [6, 13]
    adjTable[12-1] = [10, 14]
    adjTable[13-1] = [11, 15]
    adjTable[14-1] = [12, 17]
    adjTable[15-1] = [13, 16, 18]
    adjTable[16-1] = [15, 19]
    adjTable[17-1] = [14, 20]
    adjTable[18-1] = [15, 19, 21]
    adjTable[19-1] = [16, 18, 22]
    adjTable[20-1] = [17, 25]
    adjTable[21-1] = [18, 22, 26]
    adjTable[22-1] = [19, 21, 23]
    adjTable[23-1] = [22, 24]
    adjTable[24-1] = [23, 25]
    adjTable[25-1] = [20, 24, 27]
    adjTable[26-1] = [21, 28]
    adjTable[27-1] = [25, 32]
    adjTable[28-1] = [26, 29]
    adjTable[29-1] = [28, 30]
    adjTable[30-1] = [29, 31]
    adjTable[31-1] = [30, 32]
    adjTable[32-1] = [27, 31] 
    parent=computeBFStree(adjTable,start)
    print(parent)
    goal =24
    path=computeBFSpath(adjTable,start,goal)
    print(path)
