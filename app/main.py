import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    error_flag = 0
    if file_contents:
        for index,char in enumerate(file_contents):
            if char == '(':
                print('LEFT_PAREN ( null')
            elif char == ')':
                print('RIGHT_PAREN ) null')
            elif char == '{':
                print('LEFT_BRACE { null')
            elif char == '}':
                print('RIGHT_BRACE } null')
            elif char == '*':
                print('STAR * null')
            elif char == '.':
                print('DOT . null')
            elif char == ',':
                print('COMMA , null')
            elif char == '+':
                print('PLUS + null')
            elif char == '-':
                print('MINUS - null')
            elif char == ';':
                print('SEMICOLON ; null')
            elif char == '$':
                print(f'[line {index}] Error: Unexpected character: {char}')
                error_flag = 1
            elif char == '#':
                print(f'[line {index}] Error: Unexpected character: {char}')
                error_flag = 1
        print('EOF  null')
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner
    
    if error_flag == 0:
        return 0
    elif error_flag == 1:
        return 65


if __name__ == "__main__":
    main()
