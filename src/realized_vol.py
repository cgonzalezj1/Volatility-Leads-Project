import pandas as pd
import numpy as np
import glob
import os

# path to your folder of yearly csvs
folder = r"C:\Users\cgonza25\Desktop\TAQ_SPY"  
files = glob.glob(os.path.join(folder, "*.csv"))

all_results = []

for f in files:
    print(f"Processing {f}...")
    df = pd.read_csv(f)

    # ensure columns are standardized
    df = df[['DATE', 'TIME_M', 'PRICE']].dropna()
    
    # group by day to handle multiple days per file (if any)
    for date, group in df.groupby('DATE'):
        # sort by time
        group = group.sort_values('TIME_M')
        
        # compute log returns
        prices = group['PRICE'].astype(float).values
        log_returns = np.diff(np.log(prices))
        
        if len(log_returns) > 0:
            rv = np.sum(log_returns**2)   # realized variance
            vol = np.sqrt(rv)             # realized volatility
            all_results.append([date, vol])

# build final dataframe
rv_df = pd.DataFrame(all_results, columns=['date', 'realized_vol_SP500'])

# sort by date
rv_df = rv_df.sort_values('date').reset_index(drop=True)

# save
rv_df.to_csv("spy_realized_vol.csv", index=False)

print("✅ Done. Saved daily realized volatility to spy_realized_vol.csv")
