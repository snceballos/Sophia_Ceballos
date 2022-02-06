import sys

#Code given to use
class Node:
    
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

#creating 
def getMinimumCost(root,cost):
    print(cost)
    if(len(root.children)==0 or root.children is None):
        global mincost
        mincost=min(mincost,cost)
        print("mincost=",mincost)
        return
    else:
        for node in root.children:
            getMinimumCost(node,cost+root.cost+node.cost)
        

root=Node(2)
r1=Node(5)
r1.parent=root
r2=Node(3)
r2.parent=root
r3=Node(6)
r3.parent=root
r4=Node (2)
r4.parent=root
r5=Node(4)
r5.parent=r4
r6=Node(2)
r6.parent=r1

l=[]
l.append(r1)
l.append(r2)
l.append(r3)
l.append(r4)
root.children=l
r4.children=[r5]
r1.children=[r6]
#print(r1.children)

mincost=sys.maxsize
getMinimumCost(root,0)
print(mincost)   
