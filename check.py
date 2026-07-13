import pandas as pd

files = [
    "outputs/model_comparison.csv",
    "outputs/prophet_forecast.csv",
    "outputs/sarima_forecast.csv",
    "outputs/segment_forecasts.csv",
    "outputs/product_segments.csv"
]

for file in files:
    print("=" * 60)
    print(file)
    df = pd.read_csv(file)
    print(df.columns.tolist())
    print(df.head())
    print()