from collections import defaultdict

anagrams = defaultdict(list)
print(anagrams)
print(anagrams.items())
print(anagrams.values())

anagrams['key1'].append('item1')
print(anagrams)
print(anagrams.items())
print(anagrams.values())

anagrams['key2'].append('item2')
print(anagrams.items())
print(anagrams.values())
