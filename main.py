import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Add two numbers together.")

    # Add arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    # Parse the arguments
    args = parser.parse_args()

    # Perform the addition
    result = args.num1 + args.num2

    # Print the result
    print(f"The sum of {args.num1} and {args.num2} is {result}")

if __name__ == "__main__":
    main()
