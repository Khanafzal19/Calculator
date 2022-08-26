# Suppose you have two sets s1 = {1, 2, 3} and s2 = {3, 4, 5}. Which of the following statements not give us their union?
# A. s1.union({3, 4, 5})
# B. s1 | {3, 4, 5}
# C. s1 | [3, 4, 5]
# D. s1.union(set([3, 4, 5]))

s1 = {1, 2, 3}  
s2 = {3, 4, 5}
print(s1.union({3, 4, 5}))
print(s1 | {3, 4, 5})
print(s1 | [3, 4, 5])