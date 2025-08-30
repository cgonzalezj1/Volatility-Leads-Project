# Volatility Leads Project: Does VIX Implied Volatility Predict SP500 Realized Volatility?

## 📌 Overview
This project investigates whether **implied volatility from VIX options** leads **realized volatility of the SP500**.  
Using **WRDS TAQ tick data** and **OptionMetrics VIX options**, we:
1. Construct daily **realized volatility** from tick-by-tick SPY trades.
2. Extract daily **implied volatility** measures from VIX option chains.
3. Test the relationship using:
   - Simple correlation
   - Cross-correlation (lead/lag structure)
   - Granger causality (predictive direction)

The central question:  
👉 *Do option traders anticipate future volatility before it shows up in realized SP500 movements?*

---

## 🔬 Methodology

### 1. Data Sources
- **Realized volatility (RV):** Computed from SPY tick-level returns (NYSE TAQ).  
- **Implied volatility (IV):** Extracted from OptionMetrics IvyDB VIX option chains.  
- **Sample period:** 2010–2023 (daily frequency).  

⚠️ Note: **Raw data from WRDS cannot be redistributed.**  
This repo only contains **code** and **results**, not proprietary data.

---

### 2. Realized Volatility Construction
- SPY tick data → minute returns → daily realized variance:  

\[
RV_t = \sqrt{\sum_{i=1}^N r_{t,i}^2}
\]

- Annualized to match option IV scale.  

---

### 3. Implied Volatility Extraction
- From VIX options:
  - Filter for ATM (moneyness ≈ 1.0)  
  - Nearest maturity (15–45 days)  
  - Midpoint of bid/ask IV  
- Daily series constructed by averaging across filtered contracts.  

---

### 4. Statistical Tests
1. **Correlation:**  
   - Pearson = 0.53 → moderate positive co-movement.  
   - Rolling 63-day correlation median ≈ 0.41.  

2. **Cross-Correlation:**  
   - Contemporaneous ≈ 0.53 across lags.  
   - No obvious lead visually.  

3. **Granger Causality:**  
   - **IV → RV:** Highly significant at lags 2–5 (p < 0.01).  
   - **RV → IV:** Weak, inconsistent predictive power.  
   - Conclusion: *Implied volatility significantly improves forecasts of future realized volatility.*  

---

## 📊 Key Results
- Implied volatility **Granger-causes** realized volatility at 2–5 day horizons.  
- Realized volatility does **not** Granger-cause implied volatility consistently.  
- Interpretation: **Options markets embed forward-looking information faster than underlying returns.**  

---

## 📈 Example Visuals
- Correlation plots  
- Cross-correlation function (CCF)  
- Granger causality summary table  
- Timeline diagram: “IV spike at day t → RV spike at day t+3”  

(see `/results/figures/`)

---

## ⚙️ Repository Structure
- `/src/` → reusable Python functions  
- `/notebooks/` → analysis steps (from raw data → results)  
- `/results/` → plots, tables  
- `/data/` → (empty, local only; WRDS data excluded)  

---

## 🚀 How to Reproduce
1. Download TAQ tick data for SPY and VIX options from WRDS.  
2. Place raw files in `/data/` (not tracked by git).  
3. Run notebooks in order (`01` → `06`).  
4. Results will be saved under `/results/`.

---

## 📚 Skills Demonstrated
- High-frequency data cleaning (TAQ tick data).  
- Option data processing (OptionMetrics).  
- Time-series econometrics (VAR, Granger causality).  
- Financial interpretation of volatility dynamics.  
- End-to-end reproducible research pipeline.

---

## 🙏 Acknowledgments
- **WRDS** for providing TAQ and OptionMetrics data.  
- **ChatGPT (GPT-5)** assisted in structuring the pipeline and refining code.  
- Research design, data handling, and final interpretation are my own.

---

## 📄 License
MIT License. This repository contains only original code, no WRDS data.

