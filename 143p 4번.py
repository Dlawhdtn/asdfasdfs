for 앞 in range(2,10):
    if 앞 % 2 == 1:
        for 뒤 in range (1,앞 + 1):
            print(f"{앞} x {뒤} = {앞 * 뒤}")
    else:
        print("")

"""
continue와 break를 사용한 답
for 앞 in range(2,10):
    if 앞 % 2 == 0:
        print("")
        continue
        
    for 뒤 in range (1,10):
         print(f"{앞} x {뒤} = {앞 * 뒤}")
         if 왼 == 오:
         break


"""