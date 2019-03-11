
# class Word():
#     def __init__(self,text):
#         self.text = text
#
#     def equals(self,word2):
#         return self.text.lower() == word2.text.lower()
#
# first = Word('ha')
# second = Word('HA')
# third = Word("eh")
# print(first.equals(second))
# print(first.equals(third))

print("------------------------------------------")
class Word():
    def __init__(self,text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word(" self.text ")'

first = Word('ha')
second = Word('HA')
third = Word("eh")
print(first == second)

print(first)


