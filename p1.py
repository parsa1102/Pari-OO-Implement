from queue import Queue

#class Node
class Node :
    #the constructor only get a uuid (the unique id of the Node) 
    def __init__(self, uuid) :
        #adj : list of adjacent nodes to the self node
        self.adj = []
        self.uuid = uuid

#the graph class reptresenting a graph object
class Graph :
    #the constructor only needs a list of nodes : nodes of the self graph
    def __init__(self, Nodes) :
        self.Nodes = Nodes
    #simple function to get node object by uuid
    def getNodeByUuid(self, uuid) :
        for node in self.Nodes :
            if node.uuid == uuid :
                return node
        return None
    #the bfs function that runs BFS from the given root value and returns a 
    #dict parent : indicating each nodes parent in the final spanning tree
    #dict depth : indicating each nodes depth from root in the final spanning tree
    #list leaves : contaning all the leaves in the final spanning tree
    def Bfs(self, root) :
        q = Queue(maxsize=len(self.Nodes))
        q.put(root)
        # a dict to keep each nodes height in regard to the root in the final spanning tree
        depth = {
            root : 0
        }
        # a dict to keep each nodes parent in the final spanning tree
        parent = {
            root : -1
        }
        leaves = []
        visited  = []
        while not q.empty() :
            curr = q.get()
            visited.append(curr)
            leaf = True
            for i in curr.adj :
                if i not in visited :
                    leaf = False
                    depth[i] = depth[curr] + 1
                    q.put(i)
                    visited.append(i)
                    continue
            if leaf :
                leaves.append(curr)
        return parent, depth, leaves
    def getLowestDepthFromRoot(self, root) :
        parent, depth, leaves = self.Bfs(root)
        leafDepths = []
        for leaf in leaves :
            leafDepths.append((depth[leaf], leaf.uuid))
        return min(leafDepths)
    
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
    print(G.getLowestDepthFromRoot(n1))
    
    
    
__main__()
                    