from optimizer import optimize_warehouses
import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GRIDPOINT",
    page_icon="📍",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📍 GRIDPOINT")
st.subheader("Warehouse Location Optimization System")

st.write(
    "Optimize warehouse locations based on neighborhood "
    "coordinates, order demand and delivery distance."
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("⚙️ Configuration")

num_warehouses = st.sidebar.number_input(
    "Number of Warehouses",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

st.sidebar.info(
    "Enter the number of warehouses you want "
    "the optimization algorithm to consider."
)

# --------------------------------------------------
# NEIGHBORHOOD INPUT
# --------------------------------------------------

st.header("🏘️ Neighborhood Data")

num_neighborhoods = st.number_input(
    "Number of Neighborhoods",
    min_value=2,
    max_value=50,
    value=5,
    step=1
)

# Default data
default_data = pd.DataFrame({
    "Neighborhood": [f"N{i+1}" for i in range(num_neighborhoods)],
    "X Coordinate": [10 * (i + 1) for i in range(num_neighborhoods)],
    "Y Coordinate": [10 * (i + 1) for i in range(num_neighborhoods)],
    "Orders": [100 * (i + 1) for i in range(num_neighborhoods)]
})

# Editable table
data = st.data_editor(
    default_data,
    use_container_width=True,
    num_rows="fixed",
    column_config={
        "Neighborhood": st.column_config.TextColumn(
            "Neighborhood"
        ),
        "X Coordinate": st.column_config.NumberColumn(
            "X Coordinate",
            min_value=0
        ),
        "Y Coordinate": st.column_config.NumberColumn(
            "Y Coordinate",
            min_value=0
        ),
        "Orders": st.column_config.NumberColumn(
            "Orders",
            min_value=0
        )
    }
)

st.divider()

# --------------------------------------------------
# BUTTON
# --------------------------------------------------

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    optimize = st.button(
        "🚀 Optimize",
        type="primary",
        use_container_width=True
    )

with col2:
    clear = st.button(
        "🔄 Reset",
        use_container_width=True
    )

# --------------------------------------------------
# OPTIMIZATION RESULT
# --------------------------------------------------

if optimize:

    if data["Orders"].sum() == 0:
        st.error("Please enter at least one order.")
        st.stop()

    st.success("Optimization completed!")

    # --------------------------------------------------
    # REAL OPTIMIZER
    # --------------------------------------------------
if optimize:
    warehouses, assignments, total_cost = optimize_warehouses(
        data,
        num_warehouses
    )

    st.success("Optimization completed!")

    st.header("📊 Optimization Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Warehouses", num_warehouses)

    with col2:
        st.metric(
            "Total Orders",
            int(data["Orders"].sum())
        )

    with col3:
        st.metric(
            "Total Delivery Cost",
            f"{total_cost:,.2f}"
        )

    st.divider()

    st.subheader("📦 Warehouse Assignments")

    for i, assignment in enumerate(assignments):

        warehouse = warehouses[i]

        st.write(f"### 🏭 Warehouse {i + 1}")

        st.write(
            f"Location: ({warehouse['x']:.2f}, "
            f"{warehouse['y']:.2f})"
        )

        if assignment:
            st.write(
                "Serves: " + ", ".join(assignment)
            )
        else:
            st.write("No neighborhoods assigned.")
    # --------------------------------------------------
    # DATA TABLE
    # --------------------------------------------------

    st.subheader("📋 Input Data")

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "GRIDPOINT | Warehouse Location Optimization | Hack-a-Matics 2026"
)