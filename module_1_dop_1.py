grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name_ = list(sorted(students))
list_ = [5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]
average_scores = (sum(list_[0])/len(list_[0]), sum(list_[1])/len(list_[1]),
                  sum(list_[2])/len(list_[2]), sum(list_[3])/len(list_[3]),
                  sum(list_[4])/len(list_[4]))
output_to_the_console = dict(zip(name_, average_scores))
print(output_to_the_console)
