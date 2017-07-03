def teo_3(costs, rewards, energy):
  if energy < 0:
    raise ValueError("Invalid energy!!")

  memo = {}

  memo[(0, 0)] = (0, [0])
  for v in range(1, 64):
    memo[(v, 0)] = None

  for q in range(1, energy+1):
    for v in range(64):
      custo_vizinho = q - costs[v]
      vizinhos = find_neighbors(v)
      if custo_vizinho < 0:
        memo[(v, q)] = None
      else:
        tuplas = [memo[(vizinho, custo_vizinho)] for vizinho in vizinhos if not memo[(vizinho, custo_vizinho)] == None]
        if len(tuplas) > 0:
          melhor_vizinho = max(tuplas, key=lambda x: x[0])
          novo_premio = melhor_vizinho[0] + rewards[v]
          novo_caminho = melhor_vizinho[1][:] + [v]
          memo[(v, q)] = (novo_premio, novo_caminho)
        else:
          memo[(v, q)] = None

  maior = 0
  for q in range(energy, -1, -1):
    x = memo[(0, q)]
    if x != None and x[0] > maior:
      maior = x[0]
      inst = x + (q,)
  return inst


def find_neighbors(pos):
  x = pos/8
  y = pos%8

  naive = [(x-1, y-1), (x-1, y), (x-1, y+1),
           (x,   y-1),           (x,   y+1),
           (x+1, y-1), (x+1, y), (x+1, y+1)]
  filtered = [n for n in naive if n[0]>=0 and n[1]>=0 and n[0]<8 and n[1]<8]

  return map(lambda pos: pos[0]*8+pos[1], filtered)



if __name__ == '__main__':

  import sys
  from time import time

  EXECS_PER_LOOP = 100
  TIME_THRESHOLD = 5

  problems = []
  with open('walk.in') as f:

    q = int(f.readline().strip())
    while q != 0:
      costs   = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])
      rewards = sum([map(int, f.readline().strip().split(' ')) for i in range(8)], [])

      problems.append({'energy': q, 'costs': costs, 'rewards': rewards})

      q = int(f.readline().strip())

  for problem in problems:
    solution = teo_3(problem['costs'], problem['rewards'], problem['energy'])
    print solution[0]
    print solution[2]
    print q
    print ' '.join(str(x) for x in solution[1])