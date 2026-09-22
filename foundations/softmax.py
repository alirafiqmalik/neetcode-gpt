import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        max_z=max(z)
        for i in range(len(z)):
            z[i]= np.exp(z[i]-max_z)
        
        sigma_exp=sum(z)
        z=z/sigma_exp

        # Hint: subtract max(z) for numerical stability before computing exp
        return np.round(z, 4)
