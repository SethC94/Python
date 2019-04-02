# We can’t modify the elements of a tuple, but we can make a variable reference a
# new tuple holding different information. Thankfully we can also use the slice
# operation on tuples as well as strings and lists. To construct the new tuple, we
# can slice parts of the old tuple and join up the bits to make the new tuple. So
# julia has a new recent film, and we might want to change her tuple. We can
# easily slice off the parts we want and concatenate them with the new tuple.


julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

# TODO: Create a new list using the 9th through 12th elements (four items in all) of new_lst and assign it to the variable sub_lst.
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]

sub_lst = new_lst[8:12]
print(sub_lst)
