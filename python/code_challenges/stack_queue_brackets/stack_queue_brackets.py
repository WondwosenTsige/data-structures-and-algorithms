def validate_brackets(string):
    stack = []

    for char in string:

        # If its opening bracket, so push it in the stack
        if char == '{' or char == '(' or char == '[':
            stack.append(char)

        # Else if its closing bracket then check if the stack is empty then return false or
        # Pop the top most element from the stack and compare it
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            top_bracket = stack.pop()

            # Compare whether two brackets are corresponding to each other
            if not compare(top_bracket, char):
                return False


    # Check if the stack is empty or not
    if len(stack) != 0:
        return False

    return True

def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False

