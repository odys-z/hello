
if __name__ == "__main__":
    with open('inputs.q2', 'r') as f:
        lines = f.readlines()
    
    digits = ['?' for i in range(62)]
    for ln in lines:
        lss = ln.split();
        v10, v62 = int(lss[0].strip()), lss[1].strip()

        print(v10, v62)
        for i, d62 in enumerate(v62[::-1]):
            dx, v10 = v10 % 62, v10 // 62
            print(v10, dx, i, d62)
            d62_known = digits[dx]
            if d62_known == '?':
                digits[dx] = d62
            elif d62_known != d62:
                raise Exception(f'{ln}, {d62_known} != {d62}, decimal: {v10}, {digits}')

    with open('q2.h', 'w') as h:
        h.writelines([
            "char digits[] = {\n",
            "'" + "', '".join(digits) + "'",
            "\n};"])
    
    s = set(digits)
    for c in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        if c not in s:
            print(f"Missing base 62 digit '{c}'.")

        

