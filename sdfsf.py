
for x in "0123456789ABCDEFGHIJKLM":
    a = int(f"1{x}1{x}1{x}1{x}1", 23) + int(f"20{x}24", 23) + int(f"1{x}235", 23)
    if a % 22 == 0:
        print(a // 22)
        break