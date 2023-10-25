"""
 2. Write a script to remove an empty elements from a list.
    test_list = [
    (), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []
]
"""

test_list = [
    (),
    ('hey',),
    ('',),
    ('ma', 'ke', 'my'),
    [''],
    {},
    ['d', 'a', 'y'],
    '',
    []
]

test_list = [i for i in test_list if i]
print(test_list)
