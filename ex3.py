def remove_chars(strr: str):
    oper = ('+', '-', '*', '/', '(', ')', '.')
    for item in strr:
        if (not item.isdigit() and item not in oper):
            strr = strr.replace(item, "")
    return strr

while (True):
    n = input()
    if (n == "exit"):
        break
    final = remove_chars(n)
    if final != '':
        res = eval(final)
        print("Res: ", res)
