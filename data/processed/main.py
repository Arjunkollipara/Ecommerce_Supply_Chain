import pandas as pd

# =========================
# LOAD EXISTING OUTPUT FILES
# =========================

forecast_results = pd.read_csv("data/processed/m2_outputs/forecast_results.csv")
monthly_demand = pd.read_csv("data/processed/m2_outputs/monthly_demand.csv")

inventory_df = pd.read_csv("data/processed/m3_outputs/inventory_df.csv")
abc_df = pd.read_csv("data/processed/m3_outputs/abc_df.csv")

master_df = pd.read_csv("data/processed/master_dataset.csv")


# ======================================================
# ================= VIEW 4 – FORECAST ==================
# ======================================================

# Clean columns if needed
forecast_results.columns = forecast_results.columns.str.strip()

# Save to Excel
with pd.ExcelWriter("View4_Forecast.xlsx") as writer:
    monthly_demand.to_excel(writer, sheet_name="Historical_Demand", index=False)
    forecast_results.to_excel(writer, sheet_name="Forecast_Accuracy", index=False)

print("View4_Forecast.xlsx created ✅")


# ======================================================
# ================= VIEW 5 – INVENTORY =================
# ======================================================

# Products needing reorder
if "Current_Stock" in inventory_df.columns:
    reorder_df = inventory_df[inventory_df["Current_Stock"] < inventory_df["ROP"]]
else:
    reorder_df = inventory_df.sort_values("ROP", ascending=False).head(10)

with pd.ExcelWriter("View5_Inventory.xlsx") as writer:
    inventory_df.to_excel(writer, sheet_name="Inventory_Policy", index=False)
    abc_df.to_excel(writer, sheet_name="ABC_Analysis", index=False)
    reorder_df.to_excel(writer, sheet_name="Reorder_List", index=False)

print("View5_Inventory.xlsx created ✅")


# ======================================================
# ================= VIEW 6 – COST ======================
# ======================================================

# Freight metrics
freight_summary = master_df.groupby("order_id").agg(
    order_value=("price", "sum"),
    freight_cost=("freight_value", "sum")
).reset_index()

freight_summary["freight_%"] = (
    freight_summary["freight_cost"] /
    freight_summary["order_value"]
) * 100

# Cost comparison table
cost_columns = [
    "product_id",
    "Current_Cost",
    "Proposed_Cost",
    "Savings",
    "Savings_%"
]

cost_df = inventory_df[cost_columns]

with pd.ExcelWriter("View6_Cost.xlsx") as writer:
    cost_df.to_excel(writer, sheet_name="Cost_Comparison", index=False)
    freight_summary.to_excel(writer, sheet_name="Freight_Analysis", index=False)

print("View6_Cost.xlsx created ✅")

print("\n🔥 All 3 Power BI files are ready.")
