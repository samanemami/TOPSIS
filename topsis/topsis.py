import numpy as np
import pandas as pd
from scipy.stats import rankdata


class topsis():
    def __init__(self,
                 decision_matrix,
                 weight,
                 criteria,
                 impact):

        self.decision_matrix = decision_matrix
        self.weight = weight
        self.criteria = criteria
        self.impact = impact

    def _decision_matrix(self):

        decision_matrix = self.decision_matrix.values
        n = decision_matrix.shape[1]

        divisors = np.empty(n)
        A_w = np.zeros(n)
        A_b = np.zeros(n)

        for i in range(n):
            cl = decision_matrix[:, i]
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

        dm = (decision_matrix / divisors) * self.weight

        return dm, A_w, A_b

    def _rank(self, data):
        ranks = rankdata(data).astype(np.int32)
        ranks -= 1
        return self.decision_matrix.index[ranks][::-1]

    def rank(self):

        self.__check_params()

        m = self.decision_matrix.shape[0]
        dm, A_w, A_b = self._decision_matrix()
        d_b = np.zeros(m)
        d_w = np.zeros(m)
        s_w = np.zeros(m)

        # Compute the distance between the target
        # in DM and the worst alternative (A_w)
        # and best alternative (A_b)

        # L2-distance
        
        for i in range(m):
            d_b[i] = np.sqrt((dm[i] - A_b)**2)
            d_w[i] = np.sqrt((dm[i] - A_w)**2)

            # Compute the similarity to the worst state
            max_, min_ = max(self.criteria), min(self.criteria)
            for _ in range(A_b.shape[0]):
                if A_w[_] == max_ or A_b[_] == max_:
                    s_w[i] = 1
                elif A_w[_] == min_ or A_b[_] == min_:
                    s_w[i] = 0
            s_w[i] = d_w[i] / (d_w[i] + d_b[i])

        db = self._rank(d_b)
        dw = self._rank(d_w)
        sw = self._rank(s_w)

        ranking = pd.DataFrame(data=zip(sw, db, dw),
                               index=range(1, m+1),
                               columns=["S_w", "d_b", "d_w"])

        return ranking

    def __check_params(self):
        if isinstance(self.decision_matrix, pd.DataFrame) is False:
            raise ValueError(
                "The decision_matrix must be a two-dimensional pandas DataFrame.")

        if isinstance(self.impact, list) is False:
            raise ValueError(
                "impact should be a string list: ['+', '-']"
            )

        impact = len(self.impact)
        cl = self.decision_matrix.shape[1]
        if impact != cl:
            raise ValueError(
                "impact length must be equal to the decision_matrix columns")
