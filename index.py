import streamlit as st
import matplotlib.pyplot as plt

# Streamlit Interface
st.title("Pig Farming ROI Calculator")

# Inputs for breeding sows and growing piglets
st.header("Sow Breeding Inputs")
sow_cost = st.number_input("Total cost to raise one sow till first birth (INR)", value=35000)
num_sows = st.number_input("Number of sows", value=10)  # New input for the number of sows
litter_size = st.number_input("Average litter size per birth", value=8)
litters_per_year = st.number_input("Litters per sow per year", value=2)

st.header("Piglet Growing Inputs")
feed_cost = st.number_input("Feed cost per piglet (INR)", value=10000)
other_cost = st.number_input("Other costs per piglet (INR)", value=1000)
sale_price_per_kg = st.number_input("Meat selling price per kg (INR)", value=170)
meat_per_pig = st.number_input("Average meat yield per pig (kg)", value=100)

# Calculations
piglet_cost = sow_cost / litter_size
per_pig_total_cost = piglet_cost + feed_cost + other_cost
revenue_per_pig = meat_per_pig * sale_price_per_kg
profit_per_pig = revenue_per_pig - per_pig_total_cost

# Annual calculation
piglets_per_sow_per_year = litter_size * litters_per_year
annual_profit_per_sow = piglets_per_sow_per_year * profit_per_pig

# Calculate total profit for multiple sows
total_annual_profit = annual_profit_per_sow * num_sows

# ROI Calculation
total_investment = sow_cost * num_sows  # Initial investment in all sows
roi = (total_annual_profit / total_investment) * 100

# Output the ROI and other results
st.header("Results")
st.metric("Piglet cost from breeding", f"INR {piglet_cost:.2f}")
st.metric("Total cost per pig (incl. piglet, feed, other)", f"INR {per_pig_total_cost:.2f}")
st.metric("Revenue per pig", f"INR {revenue_per_pig:.2f}")
st.metric("Profit per pig", f"INR {profit_per_pig:.2f}")
st.metric("Estimated annual profit per sow", f"INR {annual_profit_per_sow:.2f}")
st.metric("Total annual profit for all sows", f"INR {total_annual_profit:.2f}")
st.metric("Annual ROI", f"{roi:.2f}%")

# Generate a graph of ROI over multiple years
years = list(range(1, 11))  # Years from 1 to 10
roi_values = [(total_annual_profit * year / total_investment) * 100 for year in years]

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(years, roi_values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
plt.title("ROI Over Years of Sow Breeding", fontsize=16)
plt.xlabel("Years", fontsize=12)
plt.ylabel("ROI (%)", fontsize=12)
plt.grid(True)
plt.xticks(years)
st.pyplot(plt)
