import re


def main() -> None:
  iFirstNum: int = input_number("Enter first number: ")
  iSecondNum: int = input_number("Enter second number: ")

  print(f"{iFirstNum} + {iSecondNum} = {iFirstNum + iSecondNum}")


def input_number(text: str) -> int:
  while True:
    sNum: str = input(text)

    if re.match(r"^-?\d+$", sNum) is not None:
      return int(sNum)

    print("Sorry, you write not a number")


if __name__ == "__main__":
  main()
