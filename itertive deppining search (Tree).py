from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

	def __init__(self,vertices):

		# No. of vertices
		self.V = vertices

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function to perform a Depth-Limited search
	# from given source 'src'
	def DLS(self,src,target,maxDepth):

		if src == target : return True

		# If reached the maximum depth, stop recursing.
		if maxDepth <= 0 : return False

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False

	# IDDFS to search if target is reachable from v.
	# It uses recursive DLS()
	def IDDFS(self,src, target, maxDepth):

		# Repeatedly depth-limit search till the
		# maximum depth
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False


g = Graph (7); # there are 7 vertices in this graph tree,,,imagine a graph tree hai not matrix.
g.addEdge(0, 1)#0 bata tala 1 ani 2
g.addEdge(0, 2)#0 bata tala 1 ani 2
g.addEdge(1, 3)#1 bata tala 3 ra 4
g.addEdge(1, 4)#1 bata tala 3 ra 4
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 1; maxDepth = 10; src = 0 # target bhane required point , mxdept bane kati lvl samma janu milne? src(source) start kata bata garne?

if g.IDDFS(src, target, maxDepth) == True:
	print ("Target is reachable within max depth")
else :
	print ("Target is not reachable")



