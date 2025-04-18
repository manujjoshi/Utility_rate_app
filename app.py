import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Utility Rate Search", layout="centered")

# ✅ Inject working CSS for full app background
st.markdown("""
    <style>
        .stApp {
            background-color: #e6ffe6;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Header with logo and title
col1, col2 = st.columns([2, 6])
with col1:
    st.image("metco.png", width=140)
with col2:
    st.markdown("## Utility Rate Search Tool")

# ✅ Load data
@st.cache_data
def load_data():
    return pd.read_csv("combined_file_2023.csv")

df = load_data()

# ✅ Step 1: Select State
state_options = sorted(df["state"].dropna().unique())
selected_state = st.selectbox("Select State", state_options)
df_filtered = df[df["state"] == selected_state]

# ✅ Optional Step 2: Zip Code
zip_options = ["All"] + sorted(df_filtered["zip"].dropna().unique())
selected_zip = st.selectbox("Select Zip Code (Optional)", zip_options)
if selected_zip != "All":
    df_filtered = df_filtered[df_filtered["zip"] == selected_zip]

# ✅ Optional Step 3: Utility Name
utility_options = ["All"] + sorted(df_filtered["utility_name"].dropna().unique())
selected_utility = st.selectbox("Select Utility Name (Optional)", utility_options)
if selected_utility != "All":
    df_filtered = df_filtered[df_filtered["utility_name"] == selected_utility]

# ✅ Optional Step 4: Ownership
ownership_options = ["All"] + sorted(df_filtered["ownership"].dropna().unique())
selected_ownership = st.selectbox("Select Ownership (Optional)", ownership_options)
if selected_ownership != "All":
    df_filtered = df_filtered[df_filtered["ownership"] == selected_ownership]

# ✅ Sorting Options
st.markdown("### Sort Results")
sort_column = st.selectbox("Sort by", ["comm_rate", "ind_rate", "res_rate"])
sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)

ascending = True if sort_order == "Ascending" else False
df_sorted = df_filtered.sort_values(by=sort_column, ascending=ascending)

# ✅ Show table
if not df_sorted.empty:
    st.subheader("Filtered Rates")
    st.table(df_sorted[["zip", "utility_name", "comm_rate", "ind_rate", "res_rate"]].reset_index(drop=True))
else:
    st.warning("No data found for selected filters.")

# ✅ Footer
st.markdown("""
    <hr style="margin-top: 50px; border: none; border-top: 1px solid #bbb;" />
    <div style="text-align: center; font-size: 14px; color: #555;">
        © 2025 METCO R&D Team. All rights reserved.
    </div>
""", unsafe_allow_html=True)
