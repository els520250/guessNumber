import random


start = input('請輸入範圍起始值: ')
end = input('請輸入範圍終止值: ')
start = int(start)
end = int(end)
number = random.randint(start,end)

count = 0
#print(number)
while True:
	guess = input('輸入數字: ')
	guess = int(guess)
	count += 1
	if guess == number:
		print('猜中數字! 你猜了', count, '次')
		break
	elif guess > number:
		print('比', guess, '還要小,你猜了', count, '次')
	elif guess < number:
		print('比', guess, '還要大,你猜了', count, '次')