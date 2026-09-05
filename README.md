# Volatility Prediction of Oil and Gold Prices Using GARCH Model

[![Journal](https://img.shields.io/badge/Journal-Indian%20Journal%20of%20Natural%20Sciences-blue)](#citation)
[![Publication Date](https://img.shields.io/badge/Publication-2024-green)](#publication--links)

## Authors
* Piyush Kumar
* Divyansh Sagar
* Lakhwinder Kaur Dhillon

---

## Publication & Links
* **Journal:** Indian Journal of Natural Sciences (Volume 14, Issue 82, Pages 514–524, 2024)
* **Paper Link:** [View on ResearchGate / Google Scholar](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=GwEBOKYAAAAJ&citation_for_view=GwEBOKYAAAAJ:UeHWp8X0CEIC)

---

## Abstract
This study constructs GARCH/ARCH time-series models to predict future price volatility on a rolling basis for energy commodities and precious metals to aid risk management decisions. Financial data spanning from **August 2014 to February 2022** was extracted from Yahoo Finance. Dynamic GARCH models were implemented in Python across various oil and gold futures/ETFs to identify optimal volatility prediction models with lower error rates.

---

## Optimal Model Configurations & Results

| Asset Category | Financial Instrument | Ticker Symbol | Best Performing Model |
| :--- | :--- | :--- | :--- |
| **Oil / Energy** | Brent Oil Futures | `BZ=F` | GARCH(1, 2) |
| **Oil / Energy** | E-Mini Crude Oil Futures | `QM=F` | GARCH(1, 0) |
| **Oil / Energy** | WisdomTree WTI Crude Oil | `CRUD.MI` | GARCH(1, 1) |
| **Gold / Metals** | Micro Gold Futures | `MGC=F` | GARCH(1, 0) |
| **Gold / Metals** | E-Mini Gold Futures | `QO=F` | GARCH(1, 2) |
| **Gold / Metals** | ZKB Gold ETF | `ZGLD.SW` | GARCH(1, 1) |

---

## Visualizations Gallery

Selected GARCH volatility forecasts and 7-day rolling evaluations:

| Oil Volatility Forecasts | Gold Volatility Forecasts |
| :---: | :---: |
| ![Brent Oil GARCH](plots/oil/BZ=F.png) | ![Gold ETF GARCH](plots/gold/ZGLD.SW(1,1).png) |


---

## Citation
If you find this research or model analysis useful, please cite our paper:

```bibtex
@article{kumar2024volatility,
  title={Volatility Prediction of Oil and Gold Prices Using GARCH Model},
  author={Kumar, Piyush and Sagar, Divyansh and Dhillon, Lakhwinder Kaur},
  journal={Indian Journal of Natural Sciences},
  volume={14},
  number={82},
  pages={514--524},
  year={2024}
}
