from pariGraph import Node
from pariGraph import Graph

def __main__() :
    #initializing Node object
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    #adding adjacency data to nodes
    n1.adj = [n2, n3]
    n2.adj = [n4, n5]
    n3.adj = [n6, n7]
    n4.adj = [n8]
    n5.adj = [n9]
    n6.adj = []
    n7.adj = [n10, n11]
    n8.adj = [n12]
    n9.adj = []
    n10.adj = []
    n11.adj = []
    n12.adj = []
    #initilize Graph
    G = Graph([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])
    #asking for smallest depth from root, root being n1
    ret = G.getLowestDepthFromRoot(n1)
    print("Depth : ", ret[0])
    print("Node : ",  ret[1])
    
    
    
__main__()
                    