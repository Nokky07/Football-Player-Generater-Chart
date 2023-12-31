def read(file):
  players = [""] * 234
  nationality = [""] * 234
  position = [''] * 234
  goals = [0] * 234
  i = 0

  with open(f"{file}") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
      items = line.split(",")
      players[i] = items[0]
      nationality[i] = items[1]
      position[i] = items[2]
      goals[i] = int(items[3])

      line = readfile.readline().rstrip('\n')
      i += 1

  return players, nationality, position, goals



players, nationality, position, goals = read("players.csv")

def split(plist):

  first = [""] * 234
  second = [""] * 234
  
  for x in range(233):      # Num of players
    items = plist[x].split(" ")
    first[x] = items[0]
    second[x] = items[1]

  return first, second

splitn, splits = split(players)




def findmax(list):
  max = list[0]
  for i in range(1, 233):
    if max < list[i]:
      max = list[i]

  return max



with open("IDnumbers.csv", "w") as rfile:
  ID = ""
  for x in range(233):
    ID += splitn[x][0]
    ID += splits[x][len(splits[x]) - 3:]
    ID += str(ord(position[x]))
    rfile.write(ID + "\n")
    ID = ""


print(f"Most goals scored by a player was: {max}")
for i in range(233):
  if goals[i] > 200:
    print(players[i])
