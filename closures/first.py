def sort_prority(values, group, sgroup=None):
    found = False
    def helper(x):
        nonlocal found
        if x in sgroup:
            found = True
            return 0
        elif x in group:
            found = True
            return 1
        return 2
    values.sort(key=helper)
    return found


values = list(range(10))
group = (2, 3, 5, 7)
super_group = (8, 9)
found = sort_prority(values, group, super_group)
print(values, found)


# Same but with classes
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


sorter = Sorter(group)
values.sort(key=sorter)
assert sorter.found is True
