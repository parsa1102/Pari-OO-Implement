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
        print("running BFS")
        print("root depth is considered 0")
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
        print("getting lowest depth node from root")
        parent, depth, leaves = self.Bfs(root)
        leafDepths = []
        for leaf in leaves :
            leafDepths.append((depth[leaf], leaf.uuid))
        return min(leafDepths)
    def sortByDepthFromRoot(self, root) :
        print("getting depth of all nodes")
        parent, depth, leaves = self.Bfs(root)
        Depths = []
        for leaf in self.Nodes :
            Depths.append((depth[leaf], leaf.uuid))
        print("sorting depth list")
        Depths.sort(reverse=True)
        return Depths