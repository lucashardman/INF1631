import sys 

def read_file(file):
	
	file_name = file[1]
	mynumbers = []
	with open (file_name, "r") as f:
		for line in f:
			mynumbers.append([int(n) for n in line.strip().split(' ')])
			
	flag1 = 0
	edge = 0
	vertice = 0
	
	for pair in mynumbers:
		try:
			x,y = pair[0],pair[1]
			if flag1 == 0:
				edge = x
				vertice = y
				graph = [[0 for w in range(vertice)] for h in range(edge)]
				flag1 = 1
			else:
				graph[x][y] += 1
			#print
        # Do Something with x and y
		except IndexError:
			print ("A line in the file doesn't have enough entries.")
	return graph

def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return None
	
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

def find_paths(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):                    
                    cycles.append(path)
    return cycles

def find_cycle(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    if path[0] in graph[path[len(graph)-1]]:
                        #print path[0], graph[path[len(graph)-1]]
                        path.append(path[0])
                        cycles.append(path)
    return cycles

graph = read_file(sys.argv)
	
print ("Finding Hamiltonian Paths----")
a= find_paths(graph)
print ("Number of Hamiltonian Paths=", len(a))
print ("Finding Hamiltonian Cycles----")
a= find_cycle(graph)
print ("Number of Hamiltonian Cycles=", len(a))
print ("done!")