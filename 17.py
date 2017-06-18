'''
Question:
Write a program that computes the net amount of a bank account 
based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

bank_balance = 0

each_line = raw_input()

while each_line:
	val = each_line.split(' ')
	op = val[0]
	amount = int(val[1])
	if op == 'D':
		bank_balance+=amount
	if op == 'W':
		bank_balance-=amount
	each_line = raw_input()
print bank_balance