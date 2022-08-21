"""
내가 쓴 답
for b in range(2,10):
    for a in range(2,10):
        print(f'{a} x {b} = {a * b}', end='\t')
    print(f'{a} x {b}') <== 이부분이 틀림 print("")로 띄어쓰기만 해주면 됨
"""
"""
for a in range(2,10):
    print(f'{a} x 1', end='\t')
"""
"""
for b in range(2,10):
    print(f'{a} x {b}')
"""

"""
답
for b in range(2,10):
    for a in range(2,10):
        print(f'{a} x {b} = {a * b}', end='\t')
    print('')
"""
