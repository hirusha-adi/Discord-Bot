# import string, secrets, os
# os.system('cls')
# pwd_length = int(input("[?] Enter the password length: "))
# alphabet = string.ascii_letters + string.digits + string.punctuation + string.hexdigits + "{}:<>?)(*&^%$#@!~),.;'[]"
# password = ''.join(secrets.choice(alphabet) for i in range(pwd_length))
# print(str(password))

# def encrypt(string, dictionary):
#     return '.'.join([dictionary.get(each, each) for each in string])

# def decrypt(string, dictionary):
#     dictionary = {dictionary[key]: key for key in dictionary}
#     decoded = [dictionary.get(each, each) for each in string.split('.')]
#     return ''.join(decoded)

# encrypt_dict = {"A": '8', "B": '9', "C": '35', "D": '99', "E": '56', "F": '44', "G": '57', "H": '67', "I": '0',
#                 "J": '4', "K": '100',
#                 "L": '90', "M": '30', "N": '66', "O": '93', 'P': '55', 'Q': '88', 'R': '34', 'S': '98', 'T': '45',
#                 'U': '36', 'V': '22', 'W': '78',
#                 'X': '46', 'Y': '3', 'Z': '1',
#                 'a': '64', 'b': '81', 'c': '1225', 'd': '9801', 'e': '3137', 'f': '1937', 'g': '3136', 'h': '4489',
#                 'i': '10',
#                 'j': '16', 'k': '9604', 'l': '8100', 'm': '47', 'n': '4356', 'o': '8649', 'p': '3025', 'q': '7744',
#                 'r': '1156', 's': '4483',
#                 't': '1936', 'u': '1224', 'v': '484', 'w': '6084', 'x': '2116', 'y': '89', 'z': '2',
#                 '1': "223", '2': "354", '3': "445", '4': "234", '5': "890", '6': "089", '7': "349", '8': "867",
#                 '9': "650", '0': "940",
#                 " ": "547", ",": "865", ";": "149", "@": "887", "!": "809", "#": "768", "&": "795", "(": "678",
#                 ")": "679", "-": "760", "_": "764", '"': "250", "~":"670", "%":"567", "*":"789", ".":"987", ":":"590", 
#                 "<": "709", "=": "710", ">":"711", "{":"765", '}':"761", '|':"690", "?": "691", "[": "692", "]": "693",
#                 "\\": "694", "^": "697", "`": "695", "'": "696"}

# x = encrypt(password, encrypt_dict)
# splitted = x.split('.')
# print(splitted)
# alphabetm = ""
# for i in splitted:
#     alphabetm += i
# print(alphabetm)
# alphabetnew = alphabet + alphabetm
# finalstage = password.join(secrets.choice(alphabetnew) for i in range(pwd_length//2))
# print(finalstage)

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))







