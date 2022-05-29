# TOPSIS
Technique for Order of Preference by Similarity to Ideal Solution [1]


## Citation 
If you use this package, please refer [cite](CITATION.cff).


# Installation
## INSTALLING VIA PIP

inbuilt Python package management system, pip. 
You can can install, update, or delete the topsis2.

### install

```bash
pip install topsis2
```
### update
```pip
pip install --upgrade topsis2
```

### uninstall

```pip
pip uninstall topsis2
```
# Citation
If you use this package, please [cite](CITATION.cff) it as below.
```yaml
References:
    Type: API
    Author:
      - Seyedsaman Emami
    Keywords:
      - "TOPSIS"
      - "Ranking"
```


# Usage
Using this TOPSIS implementation is straightforward as importing it and writing only two lines. The important thing is the decision matrix in the type of pandas data frame. 

The decision matrix would be some data frame as the following example.

![![DM](https://github.com/samanemami/TOPSIS/blob/main/doc/decision_matrix.png)](https://github.com/samanemami/TOPSIS/blob/main/doc/decision_matrix.png)

After building your decision matrix, you need to define the criteria types (benefit or cost). To have the type, you can define a list as the impact. For instance, we assume that the first two criteria are benefit criteria and the last is the cost.

```Python
impact = ['+', '+', '-']
```

The ultimate step is assigning the weight array.

```Python
weight = np.array([0.1, 0.7, 0.2])
```

After having the three parameters, the model produces the ranking matrix.

```Python
import numpy as np
import pandas as pd
from topsis import topsis

array = np.random.randint(10, size=(5, 3))

decision_matrix = pd.DataFrame(array, columns=[
                               'criterion_' + str(i) for i in range(1, 4)],
                               index=['option_'+str(i) for i in range(1, 6)])

impact = ['+', '+', '-']
weight = np.array([0.1, 0.7, 0.2])

tp = topsis(decision_matrix=decision_matrix,
            weight=weight, impact=impact)
tp.rank()
```
> ![![ranking](https://github.com/samanemami/TOPSIS/blob/main/doc/Ranking_matrix.png)](https://github.com/samanemami/TOPSIS/blob/main/doc/Ranking_matrix.png)

# Requirements
This package takes advantage of the following libraries, which had already imported to the TOPSIS package:

* scipy
* numpy
* pandas

# Keywords
`TOPSIS`, `MCDM`, `MADM`

# Version
0.0.2

# Updated
2022-05-19

# Date-released
2022-05-18

## Related links
* [What is TOPSIS?](https://samanemami.medium.com/multi-criteria-decision-making-topsis-c122925f89e4)
* [wikipedia](https://en.wikipedia.org/wiki/TOPSIS)
* [A simple but powerful decision method](https://robertsoczewica.medium.com/what-is-topsis-b05c50b3cd05)

# References
[1] Hwang, Ching-Lai, and Kwangsun Yoon. “Methods for multiple attribute decision making.” Multiple attribute decision making. Springer, Berlin, Heidelberg, 1981. 58–191.
