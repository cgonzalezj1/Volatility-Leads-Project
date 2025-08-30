import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("rv_vs_iv_vix.csv", parse_dates=["date"]).sort_values("date")
df = df[["realized_vol_SP500", "implied_vol_VIX"]].dropna()

def cross_corr(x, y, max_lag=10):
    """Corr of x_t with y_{t+k}. Positive k means y leads x."""
    out = []
    for k in range(-max_lag, max_lag+1):
        if k < 0:
            cc = x[:k].corr(y[-k:])
        elif k > 0:
            cc = x[k:].corr(y[:-k])
        else:
            cc = x.corr(y)
        out.append((k, cc))
    return pd.DataFrame(out, columns=["lag_k", "corr"])

ccf = cross_corr(df["realized_vol_SP500"], df["implied_vol_VIX"], 10)
print(ccf)



