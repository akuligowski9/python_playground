data_type = input("What data type are you working with?   ")

#no case/switch statements in Python. Therefore, dictionary mapping instead
def evaluate_data_type(data_type):
	switcher = {
		numeric: 
			print("The answer to 23 / 3 is:") 
			23 / 3
			print("The answer to 23 // 3 is:") 
			23 // 3
			print("The answer to 23 % 3 is:")
			23 % 3 ,
		1: string,
		2: array
	}
	return switcher.get(data_type, print("Please choose a data_type from the following list: numeric, string, array"))



#numeric data type examples
# evaluate_data_type(numeric)
# print("The answer to 23 / 3 is:") 
# 23 / 3
# print("The answer to 23 // 3 is:") 
# 23 // 3
# print("The answer to 23 % 3 is:")
# 23 % 3 

#evaluate_data_type(string)
#evaluate_data_type(array)