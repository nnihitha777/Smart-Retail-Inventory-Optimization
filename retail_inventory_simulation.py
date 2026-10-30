import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

np.random.seed(42)

days = 180

dates = pd.date_range(
    start="2026-01-01",
    periods=days,
    freq="D"
)

base_demand = 50

trend = np.linspace(0, 10, days)

seasonality = 8 * np.sin(
    2 * np.pi * np.arange(days) / 30
)

weekend_effect = np.where(
    dates.dayofweek >= 5,
    -8,
    0
)

random_variation = np.random.normal(
    0,
    5,
    days
)

demand = (
    base_demand
    + trend
    + seasonality
    + weekend_effect
    + random_variation
)

demand = np.maximum(
    demand,
    5
)

data = pd.DataFrame({
    "Date": dates,
    "Demand": demand
})

data["Day"] = data["Date"].dt.dayofweek
data["DayOfMonth"] = data["Date"].dt.day
data["Month"] = data["Date"].dt.month

data["Previous_Day_Demand"] = (
    data["Demand"].shift(1)
)

data["Previous_Week_Demand"] = (
    data["Demand"].shift(7)
)

data = data.dropna().reset_index(
    drop=True
)

features = [
    "Day",
    "DayOfMonth",
    "Month",
    "Previous_Day_Demand",
    "Previous_Week_Demand"
]

train_size = 140

train = data.iloc[
    :train_size
].copy()

test = data.iloc[
    train_size:
].copy()

X_train = train[features]

y_train = train["Demand"]

X_test = test[features]

y_test = test["Demand"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

mae = mean_absolute_error(
    y_test,
    predictions
)

test["Predicted_Demand"] = predictions

print(
    "Mean Absolute Error:",
    round(mae, 2)
)

print("\nActual vs Predicted Demand:")

print(
    test[
        [
            "Date",
            "Demand",
            "Predicted_Demand"
        ]
    ].head(10)
)


plt.figure(
    figsize=(12, 6)
)

plt.plot(
    test["Date"],
    test["Demand"],
    label="Actual Demand"
)

plt.plot(
    test["Date"],
    test["Predicted_Demand"],
    label="Predicted Demand"
)

plt.xlabel(
    "Date"
)

plt.ylabel(
    "Units Sold"
)

plt.title(
    "Actual vs Predicted Retail Demand"
)

plt.legend()

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()


lead_time = 2

safety_factor = 0.10


traditional_inventory = 120

traditional_reorder_point = 120

traditional_order_quantity = 100


ai_inventory = 80


traditional_stockouts = 0

ai_stockouts = 0


traditional_excess = 0

ai_excess = 0


traditional_holding_cost = 0

ai_holding_cost = 0


traditional_ordering_cost = 0

ai_ordering_cost = 0


traditional_inventory_history = []

ai_inventory_history = []


for i in range(
    len(test)
):

    actual_demand = test.iloc[
        i
    ]["Demand"]

    predicted_demand = test.iloc[
        i
    ]["Predicted_Demand"]


    traditional_inventory -= (
        actual_demand
    )


    if traditional_inventory < 0:

        traditional_stockouts += abs(
            traditional_inventory
        )

        traditional_inventory = 0


    if (
        traditional_inventory
        < traditional_reorder_point
    ):

        traditional_inventory += (
            traditional_order_quantity
        )

        traditional_ordering_cost += 50


    traditional_excess += max(
        traditional_inventory
        - actual_demand,
        0
    )


    traditional_holding_cost += (
        traditional_inventory
        * 0.5
    )


    traditional_inventory_history.append(
        traditional_inventory
    )


    ai_inventory -= (
        actual_demand
    )


    if ai_inventory < 0:

        ai_stockouts += abs(
            ai_inventory
        )

        ai_inventory = 0


    ai_target_inventory = (
        predicted_demand
        * lead_time
        * (1 + safety_factor)
    )


    if (
        ai_inventory
        < ai_target_inventory
    ):

        order_quantity = (
            ai_target_inventory
            - ai_inventory
        )

        ai_inventory += (
            order_quantity
        )

        ai_ordering_cost += 50


    ai_excess += max(
        ai_inventory
        - actual_demand,
        0
    )


    ai_holding_cost += (
        ai_inventory
        * 0.5
    )


    ai_inventory_history.append(
        ai_inventory
    )


test[
    "Traditional_Inventory"
] = traditional_inventory_history


test[
    "AI_Inventory"
] = ai_inventory_history


traditional_total_cost = (
    traditional_holding_cost
    + traditional_ordering_cost
)


ai_total_cost = (
    ai_holding_cost
    + ai_ordering_cost
)


total_demand = test[
    "Demand"
].sum()


traditional_service_level = (
    1
    - traditional_stockouts
    / total_demand
) * 100


ai_service_level = (
    1
    - ai_stockouts
    / total_demand
) * 100


print(
    "\n--- INVENTORY SIMULATION RESULTS ---"
)


print(
    "\nTraditional Inventory Strategy"
)

print(
    "Stockouts:",
    round(
        traditional_stockouts,
        2
    )
)

print(
    "Excess Inventory:",
    round(
        traditional_excess,
        2
    )
)

print(
    "Holding Cost:",
    round(
        traditional_holding_cost,
        2
    )
)

print(
    "Ordering Cost:",
    round(
        traditional_ordering_cost,
        2
    )
)

print(
    "Total Cost:",
    round(
        traditional_total_cost,
        2
    )
)

print(
    "Service Level:",
    round(
        traditional_service_level,
        2
    ),
    "%"
)


print(
    "\nAI-Based Inventory Strategy"
)

print(
    "Stockouts:",
    round(
        ai_stockouts,
        2
    )
)

print(
    "Excess Inventory:",
    round(
        ai_excess,
        2
    )
)

print(
    "Holding Cost:",
    round(
        ai_holding_cost,
        2
    )
)

print(
    "Ordering Cost:",
    round(
        ai_ordering_cost,
        2
    )
)

print(
    "Total Cost:",
    round(
        ai_total_cost,
        2
    )
)

print(
    "Service Level:",
    round(
        ai_service_level,
        2
    ),
    "%"
)


cost_reduction = (
    (
        traditional_total_cost
        - ai_total_cost
    )
    / traditional_total_cost
) * 100


print(
    "\nCost Reduction:",
    round(
        cost_reduction,
        2
    ),
    "%"
)


excess_reduction = (
    (
        traditional_excess
        - ai_excess
    )
    / traditional_excess
) * 100


print(
    "Excess Inventory Reduction:",
    round(
        excess_reduction,
        2
    ),
    "%"
)


if traditional_stockouts > 0:

    stockout_reduction = (
        (
            traditional_stockouts
            - ai_stockouts
        )
        / traditional_stockouts
    ) * 100

else:

    stockout_reduction = 0


print(
    "Stockout Reduction:",
    round(
        stockout_reduction,
        2
    ),
    "%"
)


plt.figure(
    figsize=(12, 6)
)

plt.plot(
    test["Date"],
    test["Traditional_Inventory"],
    label="Traditional Inventory"
)

plt.plot(
    test["Date"],
    test["AI_Inventory"],
    label="AI-Optimized Inventory"
)

plt.xlabel(
    "Date"
)

plt.ylabel(
    "Inventory Units"
)

plt.title(
    "Traditional vs AI-Optimized Inventory Levels"
)

plt.legend()

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()


strategies = [
    "Traditional",
    "AI-Optimized"
]


stockouts = [
    traditional_stockouts,
    ai_stockouts
]


plt.figure(
    figsize=(8, 5)
)

plt.bar(
    strategies,
    stockouts
)

plt.ylabel(
    "Stockout Units"
)

plt.title(
    "Stockout Comparison"
)

plt.tight_layout()

plt.show()


costs = [
    traditional_total_cost,
    ai_total_cost
]


plt.figure(
    figsize=(8, 5)
)

plt.bar(
    strategies,
    costs
)

plt.ylabel(
    "Total Inventory Cost"
)

plt.title(
    "Inventory Cost Comparison"
)

plt.tight_layout()

plt.show()


excess_inventory = [
    traditional_excess,
    ai_excess
]


plt.figure(
    figsize=(8, 5)
)

plt.bar(
    strategies,
    excess_inventory
)

plt.ylabel(
    "Excess Inventory Units"
)

plt.title(
    "Excess Inventory Comparison"
)

plt.tight_layout()

plt.show()