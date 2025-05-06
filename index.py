import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Inputs
st.header("Sow Breeding ROI Simulator")

num_sows = st.number_input("Number of sows", value=10)
sow_cost = st.number_input("Cost to raise one sow to first birth (INR)", value=35000)
litter_size = st.number_input("Average litter size per birth", value=8)
litters_per_year = st.number_input("Litters per sow per year", value=2)
piglet_feed_cost = st.number_input("Feed cost per piglet (INR)", value=10000)
other_costs = st.number_input("Other cost per piglet (INR)", value=1000)
selling_price = st.number_input("Selling price per piglet (INR)", value=17000)

# Calculation
total_piglets = num_sows * litter_size * litters_per_year
cost_per_piglet = (sow_cost * num_sows) / total_piglets + piglet_feed_cost + other_costs
profit_per_piglet = selling_price - cost_per_piglet
total_profit = profit_per_piglet * total_piglets

# Display results
st.subheader("Summary")
st.write(f"Total piglets per year: {total_piglets}")
st.write(f"Cost per piglet: ₹{cost_per_piglet:,.2f}")
st.write(f"Profit per piglet: ₹{profit_per_piglet:,.2f}")
st.write(f"Total annual profit: ₹{total_profit:,.2f}")

# Prepare DataFrame for visualization
df = pd.DataFrame({
    "Sows": [num_sows],
    "Piglets": [total_piglets],
    "Profit": [total_profit],
    "Cost/Piglet": [cost_per_piglet],
    "Profit/Piglet": [profit_per_piglet],
})

# Visualization
st.subheader("Profit Visualization")
chart_type = st.selectbox("Choose chart library", ["Matplotlib", "Seaborn", "Plotly"])

if chart_type == "Matplotlib":
    fig, ax = plt.subplots()
    ax.bar(["Cost/Piglet", "Profit/Piglet"], [cost_per_piglet, profit_per_piglet], color=["red", "green"])
    ax.set_ylabel("INR")
    st.pyplot(fig)

elif chart_type == "Seaborn":
    fig, ax = plt.subplots()
    sns.barplot(x=["Cost/Piglet", "Profit/Piglet"], y=[cost_per_piglet, profit_per_piglet], palette="viridis", ax=ax)
    ax.set_ylabel("INR")
    st.pyplot(fig)

elif chart_type == "Plotly":
    fig = px.bar(
        x=["Cost/Piglet", "Profit/Piglet"],
        y=[cost_per_piglet, profit_per_piglet],
        color=["Cost", "Profit"],
        labels={"x": "Category", "y": "INR"},
        title="Cost vs Profit per Piglet"
    )
    st.plotly_chart(fig)
