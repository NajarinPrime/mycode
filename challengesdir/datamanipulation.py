#!/usr/bin/env python3

import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)
print(d)

data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]

x= pd.DataFrame(data2, index=["first", "second"])

print(x)
