import streamlit as st
import pandas as pd
import pickle
import base64

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background: radial-gradient(circle at 15% 0%, #161a24 0%, #0f1117 45%);
}

/* Hide default streamlit chrome for a cleaner, branded look */
#MainMenu, footer {visibility: hidden;}

/* Header row that holds title + banner */
.app-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    padding-top: 6px;
}

.app-title h1 {
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 2px;
    background: linear-gradient(90deg, #ffffff 0%, #b6c2ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.app-title p {
    color: #9aa3b5;
    font-size: 16px;
    margin-top: 0;
}

/* Section headers */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 6px;
    margin-bottom: 2px;
}

.section-header h3 {
    margin: 0;
    font-weight: 700;
    letter-spacing: 0.2px;
}

.section-caption {
    color: #7d8698;
    font-size: 14px;
    margin-bottom: 14px;
}

/* Card-style container for input groups */
.card {
    background: #141821;
    border: 1px solid #262c3a;
    border-radius: 16px;
    padding: 22px 24px 8px 24px;
    margin-bottom: 22px;
}

/* Predict Button */
div.stButton > button {
    width: 100%;
    height: 56px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
    border: none;
    background: linear-gradient(90deg, #6366f1, #22d3ee);
    color: #0f1117;
    transition: 0.2s ease;
    box-shadow: 0 4px 18px rgba(99, 102, 241, 0.25);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
}

/* Reset button (second button on the page) */
div.stButton:nth-of-type(2) > button {
    height: 46px;
    font-size: 14px;
    font-weight: 600;
    background: #1c212c;
    color: #c6ccd8;
    border: 1px solid #2d3340;
    box-shadow: none;
}

div.stButton:nth-of-type(2) > button:hover {
    border-color: #6366f1;
    color: #ffffff;
}

/* Prediction metric */
[data-testid="stMetric"] {
    background: #171a23;
    border: 1px solid #2d3340;
    padding: 25px;
    border-radius: 18px;
    margin-top: 10px;
}

[data-testid="stMetricValue"] {
    font-size: 42px;
    font-weight: 800;
    color: #22d3ee;
}

[data-testid="stMetricLabel"] {
    font-size: 16px;
    color: #b6c2ff;
}

/* Input fields */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 10px;
    background-color: #10131b;
}

/* Number inputs */
input {
    border-radius: 10px;
}

/* Section spacing */
[data-testid="stVerticalBlock"] {
    gap: 0.6rem;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: #10131b;
    border-right: 1px solid #232837;
}

hr {
    border-color: #232837 !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER (title + banner side by side)
# --------------------------------------------------

col_title, col_banner = st.columns([3, 1])

with col_title:
    st.markdown(
        """
        <div class="app-title">
            <h1>🚗 Car Price Predictor</h1>
            <p>Estimate your car's resale value using Machine Learning</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_banner:
    # Banner image sits top-right, next to the heading.
    # Place car_banner.jpg in the same folder as this script.
    # It's rendered inside a fixed-height, rounded, cropped frame so a
    # wide photo doesn't tower over the title text.
    try:
        with open("car_banner.jpg", "rb") as f:
            banner_b64 = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <div style="
                height: 110px;
                border-radius: 16px;
                overflow: hidden;
                border: 1px solid #2d3340;
                box-shadow: 0 4px 18px rgba(0,0,0,0.35);
            ">
                <img src="data:image/jpeg;base64,{banner_b64}" style="
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    object-position: center 55%;
                    display: block;
                ">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("car_banner.jpg not found — place it next to app.py.")

st.write("")

# --------------------------------------------------
# SIDEBAR — project info
# --------------------------------------------------

with st.sidebar:
    st.markdown("### 🚗 About this app")
    st.write(
        "This tool predicts the estimated resale value of a used car "
        "based on its brand, condition, and specifications, using a "
        "trained Random Forest regression model."
    )
    st.markdown("---")
    st.markdown("**How it works**")
    st.markdown(
        "1. Enter your car's details\n"
        "2. Click **Predict Car Price**\n"
        "3. View the estimated price range"
    )
    st.markdown("---")
    st.caption("Model: Random Forest Regressor")
    st.caption("Built with Streamlit + scikit-learn")

# --------------------------------------------------
# LOAD FILES
# --------------------------------------------------

with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("feature_columns.pkl", "rb") as file:
    feature_columns = pickle.load(file)

with open("input_options.pkl", "rb") as file:
    input_options = pickle.load(file)

# --------------------------------------------------
# CAR INFORMATION
# --------------------------------------------------

st.markdown("---")
st.markdown('<div class="section-header"><h3>🚘 Car Information</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-caption">Enter the details of your car to get an estimated resale price.</div>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        brand = st.selectbox(
            "Car Brand",
            input_options["brands"]
        )

    with col2:
        car_model = st.selectbox(
            "Car Model",
            input_options["brand_models"][brand]
        )

    with col3:
        fuel = st.selectbox(
            "Fuel Type",
            input_options["fuel"]
        )

# --------------------------------------------------
# ENGINE & PERFORMANCE
# --------------------------------------------------

st.markdown('<div class="section-header"><h3>⚙️ Engine & Performance</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-caption">Specify the technical details of the vehicle.</div>', unsafe_allow_html=True)

with st.container():

    col1, col2, col3 = st.columns(3)

    with col1:
        year = st.number_input(
            "Manufacturing Year",
            min_value=1983,
            max_value=2020,
            value=2018,
            step=1
        )

    with col2:
        km_driven = st.number_input(
            "Kilometers Driven",
            min_value=0,
            max_value=1000000,
            value=50000,
            step=1000
        )

    with col3:
        mileage = st.number_input(
            "Mileage (km/l)",
            min_value=1.0,
            max_value=100.0,
            value=20.0,
            step=0.1
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        engine = st.number_input(
            "Engine (CC)",
            min_value=500,
            max_value=5000,
            value=1200,
            step=50
        )

    with col2:
        max_power = st.number_input(
            "Max Power (bhp)",
            min_value=20.0,
            max_value=500.0,
            value=82.0,
            step=1.0
        )

    with col3:
        seats = st.number_input(
            "Number of Seats",
            min_value=2,
            max_value=10,
            value=5,
            step=1
        )

# --------------------------------------------------
# CAR CONDITION
# --------------------------------------------------

st.markdown('<div class="section-header"><h3>📋 Car Condition</h3></div>', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        owner = st.selectbox(
            "Owner Type",
            input_options["owner"]
        )

    with col2:
        transmission = st.selectbox(
            "Transmission",
            input_options["transmission"]
        )

# --------------------------------------------------
# SELLER INFORMATION
# --------------------------------------------------

st.markdown('<div class="section-header"><h3>👤 Seller Information</h3></div>', unsafe_allow_html=True)

with st.container():
    seller_type = st.selectbox(
        "Seller Type",
        input_options["seller_type"]
    )

# --------------------------------------------------
# CAR AGE
# --------------------------------------------------

car_age = 2020 - year

# --------------------------------------------------
# INPUT VALIDATION
# --------------------------------------------------

if year < 1983 or year > 2020:
    st.warning("Please enter a valid manufacturing year.")

if km_driven < 0:
    st.warning("Kilometers driven cannot be negative.")

if mileage <= 0:
    st.warning("Mileage must be greater than 0.")

if engine <= 0:
    st.warning("Engine capacity must be greater than 0.")

if max_power <= 0:
    st.warning("Maximum power must be greater than 0.")

if seats < 2:
    st.warning("Number of seats must be at least 2.")

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button(
    "🔮  Predict Car Price",
    use_container_width=True
):

    # Create input dataframe
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # Numerical values
    input_data["km_driven"] = km_driven
    input_data["mileage"] = mileage
    input_data["engine"] = engine
    input_data["max_power"] = max_power
    input_data["seats"] = seats
    input_data["car_age"] = car_age

    # Categorical values
    categorical_values = {
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner,
        "brand": brand,
        "car_model": car_model
    }

    # Set categorical features
    for column, value in categorical_values.items():

        feature_name = f"{column}_{value}"

        if feature_name in input_data.columns:
            input_data[feature_name] = 1

    # Get prediction
    with st.spinner("Analyzing car details..."):
        prediction = model.predict(input_data)[0]

    # Display prediction
    st.markdown("---")
    st.markdown('<div class="section-header"><h3>💰 Estimated Selling Price</h3></div>', unsafe_allow_html=True)

    st.metric(
        label=f"{brand} {car_model} • {year}",
        value=f"₹{prediction:,.0f}"
    )

    lower_price = prediction * 0.90
    upper_price = prediction * 1.10

    st.caption(
        f"Typical estimated range: ₹{lower_price:,.0f} – ₹{upper_price:,.0f}"
    )

    st.caption(
        "Estimated resale value generated using a Random Forest machine learning model."
    )

# --------------------------------------------------
# RESET
# --------------------------------------------------

st.write("")

if st.button("🔄 Reset"):
    st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.write("")
st.markdown("---")

st.caption(
    "Car Price Prediction • Machine Learning Project"
)
st.caption("Developed by Nishant Dubey")