fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print (fruits)

print("====================================\n")

print(fruits[1])

#menambah data ke list

fruits.append("mango")

for fruit in fruits:
    print(fruit)
print("=================================\n")

#menghapus data dari list

fruits.remove("banana")
for fruit in fruits:
    print(fruit)

print("============================\n")