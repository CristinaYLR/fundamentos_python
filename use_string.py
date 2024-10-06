"""
Developer : cristina lugo
creation date : 21-sept-2024
Description: Program to learn the use of strings.
Updates: TBD
"""
# Examples to review methods of strins
concatatenation_one = 'amigo'
concatatenation_one_upper = concatatenation_one.upper()
concatatenation_one_low = concatatenation_one.lower()
concatatenation_one_cap = concatatenation_one.capitalize()


# Examples convert int to string then concatenation with a validation.
concatatenation_one = 'amigo'
concatatenationOne = 5.5

if type(concatatenationOne) is str:
    print("Direct concatenation")
    print(concatatenation_one + concatatenation_one)

elif type(concatatenationOne)is not str:
    print(" I will change data")
    conc3 = str(concatatenationOne)
    print("data was changed")
    print(concatatenation_one + conc3)