import matplotlib as plt
import pandas as pd

stock_prices = pd.DataFrame({'open': [36, 56, 45, 29, 65, 66, 67],
'close': [29, 72, 11, 4, 23, 68, 45],
'high': [42, 73, 61, 62, 73, 56, 55],
'low': [22, 11, 10, 2, 13, 24, 25]},
index=pd.date_range(
"2021-11-10", periods=7, freq="d"))


d=6
if __name__ == "__main__":
    plt.figure()
    # a = np.arange(6)
    # print(a)