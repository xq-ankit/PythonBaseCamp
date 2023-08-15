import numpy as np
import random
arr=np.concatenate([np.ones(200),np.full(180,6),np.zeros(100)])
random.shuffle(arr)
new_arr=arr.reshape(8,60)
print(new_arr)