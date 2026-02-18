# parentheses stack validation
# 

print("start")

def is_valid(string):
	stack=list()

	print(string)
	for ch in string:
		print("Stack:",stack)
		print("Character:",ch)
		if ch in ('(', '[', '{'):
			stack.append(ch)
		if ch in (')', ']', '}'):
			if not stack:
				return False		         
			if stack:
				if ch == ')':
					if stack[-1] == '(':
						stack.pop()
					else: 
						return False
				if ch == '}':
					if stack[-1] == '{':
                                        	stack.pop()
					else:
						return False
				if ch == ']':
					if stack[-1] == '[':
                                        	stack.pop()
					else:
						return False
			 
	return True

def testing(string, real_result):
	test_result=is_valid(string)
	if test_result != real_result:
		print("ERROR: test_result:", test_result, "real_result:", real_result)
	else:
	        print("SUCCESS: test_result:", test_result, "real_result:", real_result)



testing("()[]{}", True)
testing("(]", False)
testing("([)]", False)
testing("{[]}", True)

print("end")



