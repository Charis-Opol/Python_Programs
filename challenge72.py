subject = ["Math", "ICT", "Science", "History", "Geography", "Physics"]
print(subject)
dislike = input("Enter the subject you dislike: ")
index_dislike = subject.index(dislike)
del subject[index_dislike]
print(subject)
subject.remove("History")
print(subject)