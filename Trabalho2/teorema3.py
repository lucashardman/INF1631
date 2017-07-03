import sys

def read_file (file):
	file_name = file[1]

	content = []
	aux = ""
	aux2 = []
	flag = 0

	with open(file_name, "r") as f:
		for line in f:
			line = line.rstrip("\n")
			if flag == 1:
				aux = line
				aux2 = []
				flag = 0
			elif flag == 2:
				aux2.append(line)
				counter = counter - 1
				if counter == 0:
					variable = [aux, aux2]
					content.append(variable)
					flag = 0
			if len(line) > 0:
				if (line[0] == "T") and (len(line) == 1):
					flag = 1
				if line[0] == "W":
					flag = 2
					counter = int(line[2])
	return content


args = read_file(sys.argv)
print("\n\n")
for x in range (0, len(args)):
	print("Buscando na string: " + args[x][0] + "\n")
	for y in range(0, len(args[x][1])):
		print(">>> " + args[x][1][y])
		positions = []
		aux = 0

		print("Buscando apenas por correspondências exatas (case sensitive)")
		temp = args[x][0].split(" ")
		for z in range (0, len(temp)):
			if temp[z] == args[x][1][y]:
				positions.append(z)

		print("Foram achadas " + str(len(positions)) + " correspondências.")
		print("\n")

		positions = []
		print("Buscando por qualquer tipo de correspondência (case sensitive)")
		while (args[x][0].find(args[x][1][y], aux) > 0):
			aux = args[x][0].find(args[x][1][y], aux)
			positions.append(aux)
			aux = aux + 1

		print("Foram achadas " + str(len(positions)) + " correspondências.")
		print("\n")

		args[x][1][y] = args[x][1][y].upper()
		

	args[x][0] = args[x][0].upper()
	for y in range (0, len(args[x][1])):
		print(">>> " + args[x][1][y])
		positions = []
		aux = 0

		print("Buscando apenas por correspondências exatas (sem case sensitive)")
		temp = args[x][0].split(" ")
		for z in range (0, len(temp)):
			if temp[z] == args[x][1][y]:
				positions.append(z)

		print("Foram achadas " + str(len(positions)) + " correspondências.")
		print("\n")

		positions = []
		print("Buscando por qualquer tipo de correspondência (sem case sensitive)")
		while (args[x][0].find(args[x][1][y], aux) > 0):
			aux = args[x][0].find(args[x][1][y], aux)
			positions.append(aux)
			aux = aux + 1

		print("Foram achadas " + str(len(positions)) + " correspondências.")
		print("\n")