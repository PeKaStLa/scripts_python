#really simple travers 
#
 
import random
import time


print("start")

grid_border=6
grid = [['O' for _ in range(grid_border)] for _ in range(grid_border)]
dest = [grid_border-1, grid_border-1]

grid[grid_border-1][grid_border-1] = 'Z'

pp=[0,0] # player_position
grid[0][0] = 'P'

def prgr():
	print("")
	for row in grid:
		print(row)
	print("")

def walk():
	counter=0
	while pp != dest:
		oldwaysign=''
		counter+=1
		print(counter)
		if counter >= 250: break  # one-line if to break
		old_row, old_col = pp[0], pp[1]
		bit = 1 if random.random() < 0.7 else 0
		print("Bit:",bit)
		if bit == 1:
			#bitt = random.randint(0, 1)
			bitt = 1 if random.random() < 0.7 else 0
			print("bitt:", bitt)
			if bitt == 1 and pp[1] != grid_border-1:
				pp[1]+=1
				oldwaysign='->'
			if bitt == 0 and pp[1] != 0:
				pp[1]-=1
				oldwaysign='<-'
		if bit == 0:
			#bittt = random.randint(0, 1)
			bittt = 1 if random.random() < 0.7 else 0
			print("bittt:", bittt)		
			if bittt == 1 and pp[0] != grid_border-1:
				pp[0]+=1
				oldwaysign='v'
			if bittt == 0 and pp[0] != 0:
				pp[0]-=1
				oldwaysign='^'
		if oldwaysign != '':
	            grid[old_row][old_col] = oldwaysign # Leave an arrow at the OLD spot
        	    grid[pp[0]][pp[1]] = 'P' # Place P at the NEW spot
		print("PlayerP:", pp)
		print("\033[H\033[J", end='') #move cursor top and clear
		prgr()
		time.sleep(0.4)

	print("SUCCESS: The random walker made it to the destination!")

prgr()
walk()


print("end")
