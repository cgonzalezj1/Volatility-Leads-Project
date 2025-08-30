import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests

df = pd.read_csv("rv_vs_iv_vix.csv", parse_dates=["date"]).sort_values("date")
df = df[["realized_vol_SP500", "implied_vol_VIX"]].dropna()

# Log differences (stationarity)
gdf = pd.DataFrame({
    "dlog_rv": np.log(df["realized_vol_SP500"]).diff(),
    "dlog_iv": np.log(df["implied_vol_VIX"]).diff()
}).dropna()

MAX_LAG = 10

print("\nGranger: does RV -> IV?")
_ = grangercausalitytests(gdf[["dlog_iv","dlog_rv"]], maxlag=MAX_LAG, verbose=True)

print("\nGranger: does IV -> RV?")
_ = grangercausalitytests(gdf[["dlog_rv","dlog_iv"]], maxlag=MAX_LAG, verbose=True)
