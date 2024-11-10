import streamlit as st
import pandas as pd

# Load data from CSV
data = pd.read_excel('login_db.xlsx')  # Make sure 'products.csv' is the correct file path

# App title
st.title("Product Search Application")

# Choose search option
search_option = st.radio("Search By", ["Product Name", "Group Name"])

# Search by Product Name
if search_option == "Product Name":
    # Dropdown to select product name
    product_name = st.selectbox("Select a Product Name", data['product_name'].unique())

    # Filter and display the data for the selected product
    filtered_data = data[data['product_name'] == product_name]

    if not filtered_data.empty:
        st.write("### Product Details")
        # Display product details row by row
        for _, row in filtered_data.iterrows():
            st.write(f"**Product Name:** {row['product_name']}")
            st.write(f"**DP Price:** {row['dp_price']}")
            st.write(f"**Group Name:** {row['group_name']}")

            st.write("---")  # Divider between entries (if there are multiple)

# Search by Group Name
elif search_option == "Group Name":
    # Dropdown to select a group
    group_name = st.selectbox("Select a Group", ["Premium", "Prestige", "Popular", "Prominent"])

    # Filter and display the data for the selected group
    filtered_data = data[data['group_name'] == group_name]
    st.write(filtered_data[['product_name', 'dp_price', 'mrp_price', 'group_name', 'available_stock']])

else:
    st.error("CSV file is missing required columns. Make sure it contains 'product_name' and 'group_name'.")