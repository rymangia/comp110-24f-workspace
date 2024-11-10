"""This is the first challenge question"""
from pydoc import __author__
__author__
def mimic(message: str) -> str:
    """This function mimics the input"""
    return message

def main() -> None:
    """This is the main function which will run the function mimic"""
    print(mimic(message=input("What is your message?")))



if __name__ == "__main__":
  main()
