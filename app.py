#!/usr/bin/env python3
"""Sample runner for small Python examples.

Run:
	python app.py
"""

def main():
	print("Sample Python collection")
	print("1) Hello world")
	print("2) Double list (utils.double)")
	print("3) Greeter class")
	print("4) JSON read/write (save_load)")
	print("q) Quit")

	choice = input("Choose 1-4 (q to quit): ").strip()
	if choice == '1':
		import hello
	elif choice == '2':
		from utils import double
		print(double([1, 2, 3, 4]))
	elif choice == '3':
		from greeter import Greeter
		print(Greeter("Dinesh").greet())
	elif choice == '4':
		import save_load
	else:
		print("Goodbye")


if __name__ == "__main__":
	main()