class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        obj_fun= lambda x: x*x
        # Derivative:         f'(x) = 2x
        d_obj_fun = lambda x: 2*x
        x=init
        # Update rule:        x = x - learning_rate * f'(x)
        for i in range(iterations):
            x = x - learning_rate * d_obj_fun(x)

        # Round final answer to 5 decimal places
        return round(x,5)
