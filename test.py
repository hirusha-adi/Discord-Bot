import os
def adds_no(args):
	final_number = 0	
	for arg in args.split(","):
		final_number += int(arg)
	print(final_number)

adds_no("2, 3, 4, 5")	
