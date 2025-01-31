import random

class Person:
	def __init__(self, name, age=0):
	    self.name = name
	    self.age=age
	    self.happiness = 50
	    self.health = 50
	    self.smarts = 50

	def age_up(self):
		self.age += 1
		self.happiness += random.randint(-5, 5)
		self.health += random.randint(-5, 5)

	def study(self):
		self.smarts += random.randint(5, 10)
		self.happiness -= random.randint(0, 5)

	def play(self):
		self.happiness += random.randint(5, 10)
		self.health += random.randint(0, 5)

	def stats(self):
		print(f"Name: {self.name}, Age: {self.age}")
		print(f"Happiness: {self.happiness}, Health: {self.health}, Smarts: {self.smarts}")


def main():
	name = input("Enter Your Character's Name: ")
	player = Person(name)

	while True:
		player.stats()
		print("\nWhat do you want to do?")
		print("1. Age up")
		print("2. Study")
		print("3. Play")
		print("4. Exit")

		choice = input("Enter you choice: ")

		if choice == "1":
			player.age_up()
		elif choice == "2":
			player.study()
		elif choice == "3":
			player.play()
		elif choice == "4":
			break
		else:
			print("Invalid choice.")

if __name__== "__main__":
    main()