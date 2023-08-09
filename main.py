from sys import argv
from json import load, dump
from pathlib import Path


def exit():
	raise SystemExit


def main():
	if len(argv) == 1:
		print(
			"Usage:"
			"""\tmain.py "file" [splitnumber]\n"""
			"*everything betweem brackets is optional*"
		)
		exit()

	file = argv[1]

	if len(argv) == 3:
		try:
			split_num = int(argv[2])
		except ValueError:
			print("Argument must be an int!")
			exit()
	else:
		split_num = 2600

	with open(file, "r") as f:
		data = load(f)
		assert isinstance(data, list), "JSON file is invalid."
		assert split_num <= len(data), "Split number is bigger than the data."

	print("Splitting file")

	file_num = 1
	parsed_path = Path(file)
	for i in range(0, len(data), split_num):
		chunk = data[i:i + split_num]

		print(f"Split into {file_num} files")

		with open(f"""{parsed_path.parent}/{parsed_path.stem}_split{file_num}{parsed_path.suffix}""", "w") as f:
			dump(chunk, f, indent=4)

		file_num += 1


if __name__ == "__main__":
	main()
