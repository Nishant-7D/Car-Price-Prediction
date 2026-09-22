import pandas as pd
import pickle

# Load original dataset
df = pd.read_csv("Cardetails.csv")

# Create brand and model
df["brand"] = df["name"].str.split().str[0]
df["car_model"] = df["name"].str.split().str[1]

# Create brand -> model mapping
brand_models = (
    df.groupby("brand")["car_model"]
    .apply(lambda x: sorted(x.dropna().unique().tolist()))
    .to_dict()
)

# Create dropdown options
input_options = {
    "brands": sorted(df["brand"].dropna().unique().tolist()),
    "car_models": sorted(df["car_model"].dropna().unique().tolist()),
    "fuel": sorted(df["fuel"].dropna().unique().tolist()),
    "seller_type": sorted(df["seller_type"].dropna().unique().tolist()),
    "transmission": sorted(df["transmission"].dropna().unique().tolist()),
    "owner": sorted(df["owner"].dropna().unique().tolist()),
    "brand_models": brand_models
}

# Save options
with open("input_options.pkl", "wb") as file:
    pickle.dump(input_options, file)

print("Input options updated successfully!")
print("Number of brands:", len(input_options["brands"]))
print("Number of brand-model mappings:", len(input_options["brand_models"]))