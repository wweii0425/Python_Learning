List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List[1])
print(List[0])

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
List.pop()
print(List)
print(len(List))


grading = ["Tests", "Quizzes", "Individual Labs", "Group Labs", "Hackathons"]
grades = [300, 60, 120, 60, 120, 90]
oddjob = [1, 5.6, True, 4-7j, "Hello", [1, 2], [3.9, "World"]]
# We access individual elements using the index
# The first element is at index 0
print(grades[1], oddjob[4])
# We access the elements from the back using negative indices
# -1 is the last, -2 is the last but one and so on
print(grades[-1], grades[-3])
print(max(grades), min(grades))


animals = ['bear', 'bird', 'cat', 'dog', 'elephant', 'fox']
print(animals)

del animals[2]  # 刪除第三個元素"cat"
print(animals)

animals.pop()  # 刪除最尾巴的"fox"
print(animals)

animals.remove("dog")  # 刪除"dog"
print(animals)
