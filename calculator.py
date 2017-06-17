# user_input = raw_input("Type the expression to calculate, use only numbers and 'plus', 'minus' 'multiplied by', 'divided by':")
# print user_input
user_input = "1 plus 1 minus 1 multiplied by 1 divided by 1"
p = user_input.replace('plus', '+')
m = p.replace('minus', '-',)
mm = m.replace('multiplied by', '*')
d = mm.replace('divided by', '/')
print d
# print type(user_input)
# try split()
print int(d)
