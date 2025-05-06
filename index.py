import streamlit as st

st.title("Pig Farming Profit Calculator")

st.header("Sow Breeding Inputs") sow_cost = st.number_input("Total cost to raise one sow till first birth (INR)", value=35000) litter_size = st.number_input("Average litter size per birth", value=8) litters_per_year = st.number_input("Litters per sow per year", value=2)

st.header("Piglet Growing Inputs") feed_cost = st.number_input("Feed cost per piglet (INR)", value=10000) other_cost = st.number_input("Other costs per piglet (INR)", value=1000) sale_price_per_kg = st.number_input("Meat selling price per kg (INR)", value=170) meat_per_pig = st.number_input("Average meat yield per pig (kg)", value=100)

Calculations

piglet_cost = sow_cost / litter_size per_pig_total_cost = piglet_cost + feed_cost + other_cost revenue_per_pig = meat_per_pig * sale_price_per_kg profit_per_pig = revenue_per_pig - per_pig_total_cost

Annual calculation

piglets_per_sow_per_year = litter_size * litters_per_year annual_profit_per_sow = piglets_per_sow_per_year * profit_per_pig

st.header("Results") st.metric("Piglet cost from breeding", f"INR {piglet_cost:.2f}") st.metric("Total cost per pig (incl. piglet, feed, other)", f"INR {per_pig_total_cost:.2f}") st.metric("Revenue per pig", f"INR {revenue_per_pig:.2f}") st.metric("Profit per pig", f"INR {profit_per_pig:.2f}") st.metric("Estimated annual profit per sow", f"INR {annual_profit_per_sow:.2f}")

