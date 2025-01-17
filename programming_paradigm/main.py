import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denomenator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denomenator = sys.argv[2]

    result = safe_divide(numerator, denomenator)

    print(result)

if __name__ == "__main__":
    main()