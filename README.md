# Smart Retail Inventory Optimization Using Machine Learning

## Project Overview

Smart Retail Inventory Optimization is a Python-based project that uses Machine Learning to predict retail product demand and improve inventory replenishment decisions.

Retail businesses often face two major challenges: overstocking and understocking. Overstocking increases storage and holding costs, while understocking can lead to stockouts and lost sales.

This project uses a Random Forest Regression model to forecast demand and compares a traditional inventory management strategy with an AI-based inventory strategy.

## Objectives

- Predict future retail demand using Machine Learning.
- Analyze historical demand patterns and trends.
- Compare traditional and AI-based inventory management strategies.
- Reduce excess inventory and overall inventory costs.
- Maintain product availability while optimizing stock levels.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Algorithm:** Random Forest Regression
- **Data Processing:** NumPy, Pandas
- **Data Visualization:** Matplotlib

## Methodology

### 1. Synthetic Data Generation

A synthetic retail demand dataset covering 180 days is generated using Python.

The generated demand incorporates:
- Base demand
- Increasing demand trend
- Seasonal patterns
- Weekend effects
- Random variations

### 2. Demand Prediction

A Random Forest Regression model is trained using the generated demand data.

**Input Features:**
- Day of the week
- Day of the month
- Month
- Previous day's demand
- Demand from seven days earlier

The dataset is divided chronologically into training and testing observations.

The model uses 100 decision trees to predict future demand.

### 3. Inventory Strategy Comparison

Two inventory management strategies are evaluated.

**Traditional Inventory Strategy**
- Uses a fixed reorder point.
- Uses a fixed order quantity.
- Follows predefined replenishment rules.

**AI-Based Inventory Strategy**
- Uses predicted demand to calculate target inventory.
- Considers lead time and a safety factor.
- Determines replenishment quantity based on the inventory target.

### 4. Performance Evaluation

The strategies are compared using:
- Mean Absolute Error (MAE)
- Total Inventory Cost
- Holding Cost
- Ordering Cost
- Excess Inventory
- Stockouts
- Service Level

## Results

### Machine Learning Performance

| Metric | Result |
|---|---:|
| Dataset Duration | 180 Days |
| Training Observations | 140 |
| Number of Trees | 100 |
| Mean Absolute Error | 5.21 |

### Inventory Strategy Comparison

| Metric | Traditional | AI-Based |
|---|---:|---:|
| Total Cost | 3911.43 | 3614.59 |
| Holding Cost | 2911.43 | 1964.59 |
| Ordering Cost | 1000 | 1650 |
| Excess Inventory | 3922.66 | 2028.99 |
| Stockouts | 0 | 0 |
| Service Level | 100% | 100% |

### Key Findings

- **7.59% reduction** in total inventory cost.
- **48.28% reduction** in the accumulated excess-inventory measure.
- Both strategies achieved a **100% service level**.
- Both strategies experienced zero stockouts.
- The Random Forest model achieved an MAE of 5.21.

The results demonstrate the potential of demand prediction to support more cost-efficient inventory decisions.

## Project Structure

```text
Smart-Retail-Inventory-Optimization/
│
├── retail_inventory_simulation.py
└── README.md
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/nnihitha777/Smart-Retail-Inventory-Optimization.git
```

### 2. Navigate to the Project Directory

```bash
cd Smart-Retail-Inventory-Optimization
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 4. Run the Project

```bash
python3 retail_inventory_simulation.py
```

The program generates demand predictions, evaluates both inventory strategies, displays performance metrics, and produces visualizations.

## Limitations

- Uses synthetic data instead of real retail sales data.
- Does not include promotions, holidays, or product-specific demand patterns.
- Uses simplified inventory and ordering cost assumptions.
- Does not simulate actual supplier delivery delays.
- Uses a fixed safety factor.

## Future Enhancements

- Integrate real-world retail sales datasets.
- Incorporate promotions, holidays, and changing customer behavior.
- Model actual supplier lead times and delayed replenishment.
- Implement dynamic safety stock calculations.
- Develop an interactive inventory monitoring dashboard.

## Conclusion

This project demonstrates how Machine Learning-based demand forecasting can support retail inventory optimization. By comparing traditional replenishment rules with a prediction-based strategy, the simulation achieved lower total inventory costs and reduced excess inventory while maintaining the same service level.

**Note:** This is an academic proof-of-concept simulation using synthetic data. The reported cost values are simulation units, not actual currency.

## Author

**Nihitha Varma**

GitHub: [nnihitha777](https://github.com/nnihitha777)
