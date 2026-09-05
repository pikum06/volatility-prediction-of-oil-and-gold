# Gold Volatility Analysis

#Date Range: Jan 1, 2014 – Feb 28, 2022


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from arch import arch_model
from statsmodels.graphics.tsaplots import plot_pacf
import yfinance as yf

# Gold Configurations
GOLD_ASSETS = {
    "MGC=F": {"name": "Micro Gold Futures", "p": 1, "q": 0},
    "QO=F": {"name": "E-mini Gold Futures", "p": 1, "q": 2},
    "ZGLD.SW": {"name": "ZKB Gold ETF", "p": 1, "q": 1},
}


# Date Range for Analysis
START_DATE_GOLD = "2014-01-01"
END_DATE_GOLD = "2022-02-28"

# Function to Analyze Gold Volatility

def gold_volatility():
    for ticker, config in GOLD_ASSETS.items():
        print(f"\nProcessing Gold Asset: {config['name']} ({ticker})...")

        # Data Acquisition & Log Returns

        df = yf.download(ticker, start=START_DATE_GOLD, end=END_DATE_GOLD)
        close_col = "Adj Close" if "Adj Close" in df.columns else "Close"
        returns = (
            (df[close_col].pct_change().dropna() * 100)
            if not isinstance(df.columns, pd.MultiIndex)
            else (df[close_col][ticker].pct_change().dropna() * 100)
        )

        # PACF Plot

        fig, ax = plt.subplots(figsize=(8, 3))
        plot_pacf(returns, lags=35, ax=ax, title=f"PACF - {ticker}")
        plt.tight_layout()
        plt.show()

        # Optimal GARCH Model Fitting

        model = arch_model(
            returns,
            vol="Garch",
            p=config["p"],
            q=config["q"],
            mean="Constant",
            dist="normal",
        )
        res = model.fit(disp="off")
        print(res.summary().tables[1])

        # Rolling Forecast

        train_size = int(len(returns) * 0.8)
        rolling_preds = []
        for i in range(train_size, len(returns)):
            roll_model = arch_model(
                returns.iloc[:i],
                vol="Garch",
                p=config["p"],
                q=config["q"],
                mean="Constant",
            )
            roll_fit = roll_model.fit(disp="off")
            pred = np.sqrt(roll_fit.forecast(horizon=1).variance.values[-1, 0])
            rolling_preds.append(pred)

        rolling_series = pd.Series(
            rolling_preds, index=returns.index[train_size:]
        )

        # 7-Day Prediction

        forecast_7d = np.sqrt(res.forecast(horizon=7).variance.values[-1, :])

        # Plotting Graphs
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 4))
        axes[0].plot(
            returns.index,
            returns,
            label="True Returns",
            alpha=0.4,
            color="gray",
        )
        axes[0].plot(
            rolling_series.index,
            rolling_series,
            label="Predicted Volatility",
            color="gold",
        )
        axes[0].set_title(
            f"{ticker} - Volatility Prediction (Rolling Forecast)"
        )
        axes[0].legend()

        axes[1].plot(
            [f"Day {i+1}" for i in range(7)],
            forecast_7d,
            marker="o",
            color="goldenrod",
        )
        axes[1].set_title(f"{ticker} - Volatility Prediction (Next 7 Days)")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    gold_volatility()