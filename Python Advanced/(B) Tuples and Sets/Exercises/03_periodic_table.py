n = int(input())
chemical_compounds = set()
for _ in range(n):
    user_input = input().split()
    for i in user_input:
        chemical_compounds.add(i)

for j in chemical_compounds:
    print(j)
    