def romanToInt(s: str) -> int:
    sum = 0
    i = 0
    while i < len(s):
        if s[i] == "I":
            if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                sum += 4 if s[i+1] == "V" else 9
                i += 2
            else:
                sum += 1
                i += 1
        elif s[i] == "X":
            if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                sum += 40 if s[i+1] == "L" else 90
                i += 2
            else:
                sum += 10
                i += 1
        elif s[i] == "C":
            if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                sum += 400 if s[i+1] == "D" else 900
                i += 2
            else:
                sum += 100
                i += 1
        elif s[i] == "V":
            sum += 5
            i += 1
        elif s[i] == "L":
            sum += 50
            i += 1
        elif s[i] == "D":
            sum += 500
            i += 1
        elif s[i] == "M":
            sum += 1000
            i += 1
    return sum


print(romanToInt("IVIX"))
