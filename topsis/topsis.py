import numpy as np
import pandas as pd


class topsis():
    def __init__(self, decision_matrix, weight, criteria, impact):

        self.decision_matrix = decision_matrix
        self.weight = weight
        self.criteria = criteria
        self.impact = impact

    def __call__(self):
        pass

    def decision_matrix(self):
        n = self.decision_matrix.shape[1]

        if isinstance(decision_matrix, pd.DataFrame):
            decision_matrix = decision_matrix.values

        divisors = np.empty(n)
        A_w = np.zeros(n)
        A_b = np.zeros(n)

        for i in range(n):
            cl = self.decision_matrix[:, i]
            divisors[i] = np.sqrt(cl @ cl)

            max_ = np.max(cl)
            min_ = np.min(cl)

            # Define the worst alternative A_w and the
            # best alternative A_b, based on the positive
            # or negative impact

            if self.impact[i] == '+':
                A_b[i] = max_
                A_w[i] = min_
            elif self.impact[i] == '-':
                A_b[i] = min_
                A_w[i] = max_

        decision_matrix = (self.decision_matrix / divisors) * self.weight

        return decision_matrix, A_w, A_b

    def distance(self):
        m = self.decision_matrix.shape[0]
        dm, A_w, A_b = self.decision_matrix()
        d_b = np.zeros(m)
        d_w = np.zeros(m)
        sw = np.zeros(m)
        for i in range(m):
            d_b_ = dm[i] - A_b
            d_w_ = dm[i] - A_w
            d_b[i] = np.sqrt(d_b_ @ d_b_)
            d_w[i] = np.sqrt(d_w_ @ d_w_)
            if A_w[i] == self.criteria[i] or A_b[i] == self.criteria[i]:
                sw[i] = 0
            sw[i] = d_w[i] / (d_w[i] + d_b[i])
