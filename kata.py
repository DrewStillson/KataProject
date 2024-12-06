class Kata():
	def convertToRoman(self, num):
		try:
			num = int(num)
			if (num < 1 or num > 3000):
				return "Your number is either too big or too small!"
			
			romanNumeral = ""
			romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
			romanSymbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

			for i in range(len(romanSymbols)):
				while (num >= romanValues[i]):
					romanNumeral += romanSymbols[i]
					num -= romanValues[i]

			return romanNumeral
		
		except ValueError:
			raise ValueError("You need to enter a number!")
		
def main():
	k = Kata()
	for i in range(1,3001):
		print("Number: " + str(i) + " Roman Numeral: " + k.convertToRoman(i))