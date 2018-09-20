def eval(blackpiece, blackpos, whitepiece, whitepos):
	#Mengecek jumlah warna sama dan berbeda yang saling menyerang dan dikeluarkan dalam samecost, differentcost
	samecost = 0;
	differentcost = 0;


	for i, piece in enumerate(blackpiece):
		piecepos = blackpos[1]

		if(piece == 'R'):
			same, different = rookcost(piecepos, blackpos, whitepos)
			samecost += same
			differentcost += different
		elif(piece == 'B'):
			same, different = bishopcost(piecepos, blackpos, whitepos)
			samecost += same
			differentcost += different
		elif(piece == 'Q'):
			same, different = queencost(piecepos, blackpos, whitepos)
			samecost += same
			differentcost += different
		elif(piece == 'K'):
			same, different = knightcost(piecepos, blackpos, whitepos)
			samecost += same
			differentcost += different

	return (samecost, differentcost)


def bishopcost(position, samecolourpiece, differentcolourpiece):
	samecost = 0
	differentcost = 0

	#Up-Right
	x = position[0]
	y = position[1]
	found = false
	while(x < 8 and y < 8 and not found):
		x += 1
		y += 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Down-Right
	x = position[0]
	y = position[1]
	found = false
	while(x < 8 and y > 1 and not found):
		x += 1
		y -= 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Down-Left
	x = position[0]
	y = position[1]
	found = false
	while(x > 1 and y > 1 and not found):
		x -= 1
		y -= 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Up-Left
	x = position[0]
	y = position[1]
	found = false
	while(x > 1 and y < 8 and not found):
		x -= 1
		y += 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	return (samecost, differentcost)

def rookcost(position, samecolourpiece, differentcolourpiece):
	samecost = 0
	differentcost = 0

	#Right
	x = position[0]
	y = position[1]
	found = false
	while(x < 8 and not found):
		x += 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Left
	x = position[0]
	y = position[1]
	found = false
	while(x > 1 and not found):
		x -= 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Up
	x = position[0]
	y = position[1]
	found = false
	while(y < 8 and not found):
		y += 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	#Down
	x = position[0]
	y = position[1]
	found = false
	while(y > 1 and not found):
		y -= 1
		if ((x, y) in samecolourpiece):
			found = true
			samecost += 1
		elif ((x, y) in differentcolourpiece):
			found = true
			differentcost += 1

	return (samecost, differentcost)

def queencost(position, samecolourpiece, differentcolourpiece):
	samecostorthogonal, differentcostorthogonal = rookcost(position, samecolourpiece, differentcolourpiece)
	samecostdiagonal, differentcostdiagonal = bishopcost(position, samecolourpiece, differentcolourpiece)

	samecost = samecostorthogonal + samecostdiagonal;
	differentcost = differentcostorthogonal + differentcostdiagonal;

	return (samecost, differentcost)

def knightcost(position, samecolourpiece, differentcolourpiece):
	samecost = 0
	differentcost = 0

	x = position[0]
	y = position[1]

	coordinates = []
	coordinates.append((x+2, y+1))
	coordinates.append((x+2, y-1))
	coordinates.append((x-2, y+1))
	coordinates.append((x-2, y-1))
	coordinates.append((x+1, y+2))
	coordinates.append((x+1, y-2))
	coordinates.append((x-1, y+2))
	coordinates.append((x-1, y-2))

	for coordinate in coordinates:
		if coordinate in samecolourpiece:
			samecost += 1;
		elif coordinate in differentcolourpiece:
			differentcost += 1;

	return (samecost, differentcost)

