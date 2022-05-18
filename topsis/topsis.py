import numpy as np
import pandas as pd
from scipy.stats import rankdata


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

        _decision_matrix = (self.decision_matrix / divisors) * self.weight

        return _decision_matrix, A_w, A_b

    def _rank(self, data):
        ranks = rankdata(data).astype(np.int32)
        ranks -= 1
        return self.decision_matrix.index[ranks]

    def distance(self):
        m = self.decision_matrix.shape[0]
        dm, A_w, A_b = self.decision_matrix()
        d_b = np.zeros(m)
        d_w = np.zeros(m)
        s_w = np.zeros(m)

        for i in range(m):
            d_b_ = dm[i] - A_b
            d_w_ = dm[i] - A_w
            d_b[i] = np.sqrt(d_b_ @ d_b_)
            d_w[i] = np.sqrt(d_w_ @ d_w_)
            max_, min_ = max(self.criteria), min(self.criteria)
            if A_w[i] == max_ or A_b[i] == max_:
                s_w[i] = 1
            elif A_w[i] == min_ or A_b[i] == min_:
                s_w[i] = 0
            s_w[i] = d_w[i] / (d_w[i] + d_b[i])

        db = self._rank(d_b)
        dw = self._rank(d_w)
        sw = self._rank(s_w)

        ranking = pd.DataFrame(data=zip(sw, db, dw),
                               index=range(1, m+1),
                               columns=["S_w", "d_b", "d_w"])

        return ranking
