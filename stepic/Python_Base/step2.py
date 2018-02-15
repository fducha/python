objects = list('skefg eufgwooaswecnhwewcuwi23tr8wefyw90hf2cndbwb8c')

# res = set()
# for obj in objects:
#     res.add(id(obj))

print(len(set([id(i) for i in objects])))
