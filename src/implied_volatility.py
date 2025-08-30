import pandas as pd
import numpy as np

INFILE  = "icijrgb9w0clwava.csv"              # your VIX options CSV
OUTFILE = "vix_implied_vol_30d_atm.csv"      # output daily series

df = pd.read_csv(INFILE)
df.columns = [c.lower() for c in df.columns]

# Detect required columns
date_col = "date"
dte_col = "dte" if "dte" in df.columns else ("days" if "days" in df.columns else None)
iv_col = "impl_volatility"
delta_col = "delta" if "delta" in df.columns else None
moneyness_col = "moneyness" if "moneyness" in df.columns else None

# Parse dates
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df = df.dropna(subset=[date_col])

# Keep ~30D maturity
df = df[(df[dte_col] >= 28) & (df[dte_col] <= 32)]

# Choose ATM by moneyness≈1 if available; else by |delta|≈0.5
if moneyness_col:
    df["atm_score"] = (df[moneyness_col] - 1.0).abs()
else:
    if delta_col is None:
        raise ValueError("Need either moneyness or delta to pick ATM.")
    df["atm_score"] = (df[delta_col].abs() - 0.5).abs()

# Pick best ATM per date
df = df.sort_values([date_col, "atm_score"])
daily = df.groupby(date_col, as_index=False).first()[[date_col, iv_col]]
daily = daily.rename(columns={iv_col: "implied_vol_VIX"}).sort_values(date_col)

daily.to_csv(OUTFILE, index=False)
print(f"Saved {OUTFILE} with {len(daily)} rows")
