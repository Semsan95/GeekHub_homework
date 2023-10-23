'''
Write a script to remove an empty elements from a list.
Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
'''
# якось дуже складно вийшло. Робиться без len, range і тим більше reverse
# Перероблено

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
for i in reversed(range(len(test_list))):
    if test_list[i]:
        continue
    else:
        test_list.pop(i)
print(test_list)
