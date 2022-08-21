list_example = [1,2,3,4,5]
tuple_example = (1,2,3,4,5)
set_example = {1,2,3,4,5,4,5}

for i in set_example:
    print(i)

dict_example = {
    '이름' : '임종수',
    '성별' : '남자',
    '나이' : '22'
}
print(dict_example.keys())
print(dict_example.values())
print(dict_example['이름'])

dict_example['추가키'] = '추가값'
