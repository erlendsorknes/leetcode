def isValid(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if s[i] in ["[", "(", "{"]:
            stack.append(s[i])
        elif s[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif s[i] == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif s[i] == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(isValid("[([]])"))
