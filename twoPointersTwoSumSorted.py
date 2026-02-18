# two pointers challenge
# two sum sorted
# find two sums that add up to the target
# return the indices of these two numbers , 0- or 1- indexed
# time complexity only pass through the list once
# space complexity no dict or extra space allowed and only a few variables

print("start")

def two_sum_sorted(numbers, target):
	frontDistance=0
	backDistance=len(numbers)-1
	sum=0

	sum=numbers[frontDistance] + numbers[backDistance] 
	while sum != target:
		#print(f"Current sum: {numbers[frontDistance] + numbers[backDistance]} , not yet {target}")
		if sum < target:
			#print("to the right!")
			frontDistance=frontDistance+1
		if sum > target:
			#print("to the left!")
			backDistance=backDistance-1

		sum=numbers[frontDistance] + numbers[backDistance] 


		if frontDistance+1 > len(numbers)-1 or backDistance < 1:
			print("No possible solution. Distances: ", frontDistance, ",", backDistance)
			break

		
		

	answer=[numbers[frontDistance], numbers[backDistance]]
	#print("answer array:", answer, "target:", target)
	return answer


def testing(numbers, target):
	result=two_sum_sorted(numbers, target)
	if target == result[0] + result[1]:
		print("SUCCESS: Both numbers",result[0]," and ",result[1]," sum up to the target ", target)
	else:
   		print("ERROR: The numbers",result[0]," and ",result[1]," do not sum up to the target ", target)



testing([0,1,2,3,4,5], 1)
testing([0,1,2,3,4,5], 2)
testing([0,1,2,3,4,5], 3)
testing([0,1,2,3,4,5], 4)
testing([0,1,2,3,4,5], 5)
testing([0,1,2,3,4,5], 6)
testing([0,1,2,3,4,5], 7)
testing([0,1,2,3,4,5], 8)
testing([0,1,2,3,4,5], 9)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 31)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 60)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 70)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 44)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 80)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 90)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 100)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 99)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 140)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 120)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 110)
testing([1,2,3,4,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 800)
testing([1,3,5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 7)
testing([5, 7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 7)
testing([7, 9, 11, 14, 16, 18, 20, 24, 28, 29, 33, 38, 42, 48, 55], 7)

print("end")



