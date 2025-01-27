import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import add_numbers

def main():
    result = add_numbers(3, 5)
    print(f"3 + 5 = {result}")

if __name__ == "__main__":
    main()