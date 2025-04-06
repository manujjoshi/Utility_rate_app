import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Utility Rate Search", layout="centered")

# ✅ Inject working CSS for full app background
st.markdown("""
    <style>
        .stApp {
            background-color: #e6ffe6;  /* Light green background */
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Header with logo and title
col1, col2 = st.columns([2, 6])  # Wider logo column
with col1:
    st.image(
        "metco.png",  # Replace with your logo path or URL
        width=140
    )
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
df_state = df[df["state"] == selected_state]

# ✅ Step 2: Zip (filtered)
zip_options = sorted(df_state["zip"].dropna().unique())
selected_zip = st.selectbox("Select Zip Code", zip_options)
df_zip = df_state[df_state["zip"] == selected_zip]

# ✅ Step 3: Utility Name (filtered)
utility_options = sorted(df_zip["utility_name"].dropna().unique())
selected_utility = st.selectbox("Select Utility Name", utility_options)
df_utility = df_zip[df_zip["utility_name"] == selected_utility]

# ✅ Step 4: Ownership (filtered)
ownership_options = sorted(df_utility["ownership"].dropna().unique())
selected_ownership = st.selectbox("Select Ownership", ownership_options)
final_df = df_utility[df_utility["ownership"] == selected_ownership]

# ✅ Result Display
if not final_df.empty:
    st.subheader("Filtered Rates")
    st.table(final_df[["comm_rate", "ind_rate", "res_rate"]].reset_index(drop=True))  # No index
else:
    st.warning("No data found for selected filters.")

st.markdown("""
    <hr style="margin-top: 50px; border: none; border-top: 1px solid #bbb;" />
    <div style="text-align: center; font-size: 14px; color: #555;">
        © 2025 METCO R&D Team. All rights reserved.
    </div>
""", unsafe_allow_html=True)

