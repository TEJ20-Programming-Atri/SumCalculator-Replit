# function that makes sure input is valid
def valid_input(prompt:str):
  while True:
    try:
      res = int(input(prompt))
      if res > 0:
        return res
      print("Value must be a positive integer")
    except ValueError:
      print("Value must be a positive integer")

input_num = valid_input("Enter a positive integer: ")

#Summation Formula N(N+1)/2, Without Loops
sum = ((input_num+1)*input_num)//2
print(f"The sum of numbers from 0 to {input_num} is: {sum}")

# Sum Calculator using while loop
counter = 0
sum = 0
while counter <= input_num:
  sum += counter
  counter += 1
print(f"The sum of numbers from 0 to {input_num} is: {sum}")
