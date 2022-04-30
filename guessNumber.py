import random

number = random.randint(1,100)
#print(number)
while True:
	guess = input('輸入數字1~100: ')
	guess = int(guess)
	if guess == number:
		print('猜中數字')
		break
	elif guess > number:
		print('比', guess, '還要小')
	elif guess < number:
		print('比', guess, '還要大')