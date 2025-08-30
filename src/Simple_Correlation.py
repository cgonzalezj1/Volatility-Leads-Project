import pandas as pd

# Load your merged dataset
df = pd.read_csv("rv_vs_iv_vix.csv", parse_dates=["date"]).sort_values("date")
df = df[["date", "realized_vol_SP500", "implied_vol_VIX"]].dropna()

# Pearson correlation
pearson = df["realized_vol_SP500"].corr(df["implied_vol_VIX"])
print(f"Pearson correlation (levels): {pearson:.3f}")

# Rolling correlation (optional)
roll = df["realized_vol_SP500"].rolling(63).corr(df["implied_vol_VIX"])
print(f"Rolling corr (63d) – median: {roll.median():.3f}")
