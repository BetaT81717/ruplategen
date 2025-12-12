regcode = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10","11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30","31", "32", "33", "34", "35", "36", "37", "38", "39", "40","41", "42", "43", "44", "45", "46", "47", "48", "49", "50","51", "52", "53", "54", "55", "56", "57", "58", "59", "60","61", "62", "63", "64", "65", "66", "67", "68", "69", "70","71", "72", "73", "74", "75", "76", "77", "78", "79", "83","86", "87", "89", "102", "702", "105", "113", "116", "716", "95","121", "122", "93", "123", "193", "323", "84", "88", "124", "81","159", "125", "126", "131", "134", "136", "85", "138", "91", "142","147", "90", "150", "190", "250", "550", "750", "790", "152", "252","154", "155", "156", "161", "761", "163", "763", "164", "96", "196","172", "173", "174", "774", "97", "99", "177", "197", "199", "777","797", "799", "977", "98", "178", "198", "186"]
reglet = ['А', 'В', 'Е', 'К', 'М','Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
regdip = ['CD','D','T']

import random

print('Ruplategen v1.0\nMade by BetaT81717(!!Power) on 12.12.2025')
while True:
	def generate(t):
		if t == '1':
			print('\n'+random.choice(reglet)+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+random.choice(reglet)+random.choice(reglet)+gencod+'\n')
		elif t == '2':
			print('\n'+random.choice(reglet)+random.choice(reglet)+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+gencod+'\n')
		elif t == '3':
			print('\n'+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+random.choice(reglet)+random.choice(reglet)+gencod+'\n')
		elif t == '4':
			print('\n'+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+random.choice(regdip)+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+gencod+'\n')
		elif t == '5':
			print('\n'+random.choice(reglet)+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+gencod+'\n')
		elif t == '0':
			quit()
	generate(input('Choose type:\n1.Regular\n2.Public\n3.Military\n4.Diplomatic\n5.Police\n0.Exit\nYour choice:'))