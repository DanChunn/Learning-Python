import matplotlib.pyplot as plt
import numpy as np
np.random.seed(555)
total_walks = []
attempts = 5000
min_steps = 60

for i in range(attempts) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    total_walks.append(random_walk)

#Tranpose Returns a view of the array with axes transposed
np_arr = np.transpose(np.array(total_walks))
ends = np_arr[-1]
plt.hist(ends)
plt.show()
print(sum(ends >= min_steps)/attempts)