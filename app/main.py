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

    def peek():
        return file_contents[index + 1] if index+1 < len(file_contents) else None
    
    def advance():
        nonlocal index
        index += 1

    # Uncomment this block to pass the first stage
    error_flag = False
    line_counter = 1
    index = 0
    # equal2_flag = False
    # bang_equal = False
    if file_contents:
        while index < len(file_contents):
            # if equal2_flag:
            #     equal2_flag = False
            #     continue
            # if bang_equal:
            #     bang_equal = False
            #     continue

            char = file_contents[index]

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
            # elif char == '=':
            #     try:
            #         if file_contents[index+1] == '=':
            #             equal2_flag = True
            #             print('EQUAL_EQUAL == null')
            #         else:
            #             print('EQUAL = null')
            #     except IndexError:
            #         print('EQUAL = null')
            # elif char == '!':
            #     try:
            #         if file_contents[index+1] == '=':
            #             bang_equal= True
            #             print('BANG_EQUAL != null')
            #         else:
            #             print('BANG ! null')
            #     except IndexError:
            #         print('BANG ! null')

            elif char == '=':
                if peek() == '=':
                    advance()
                    print('EQUAL_EQUAL == null')
                else:
                    print('EQUAL = null')

            elif char == '!':
                if peek() == '=':
                    advance()
                    print('BANG_EQUAL != null')
                else:
                    print('BANG ! null')

            elif char == '<':
                if peek() == '=':
                    advance()
                    print('LESS_EQUAL <= null')
                else:
                    print('LESS < null')
            
            elif char == '>':
                if peek() == '=':
                    advance()
                    print('GREATER_EQUAL >= null')
                else:
                    print('GREATER > null')

            elif char == '\n':
                print('EOF  null')
                line_counter += 1
            else:
                print(f'[line {line_counter}] Error: Unexpected character: {char}',file=sys.stderr)
                error_flag = 1
            
            index +=1
        print('EOF  null')
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner
    
    if not error_flag:
        sys.exit(0)
    else:
        sys.exit(65)


if __name__ == "__main__":
    main()
