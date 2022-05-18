import numpy as np


class topsis():
    def __init__(self, decision_matrix, weight_matrix, benefit_criteria, cost_criteria):

        self.decision_matrix = decision_matrix
        self.weight_matrix = weight_matrix
        self.benefit_criteria = benefit_criteria
        self.cost_criteria = cost_criteria

    def __call__(self):
        pass

    def test(self):
        m = self.decision_matrix.shape[0]
        n = self.decision_matrix.shape[1]

        divisors = np.empty(n)
        a_pos = np.zeros(n)
        a_neg = np.zeros(n)

        for i in range(n):
            cl = self.decision_matrix.iloc[:, i]
            divisors[i] = np.sqrt(cl @ cl)

            max_ = np.max(cl.values)
            min_ = np.min(cl.values)

            try:
                for b in self.benefit_criteria:
                    a_pos[i] = max_
