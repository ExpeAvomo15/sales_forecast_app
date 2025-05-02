
import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.set_page_config(page_title="📈 Sales Forecast App", layout="centered")

st.title("📊 Sales Forecast with Prophet")
st.markdown("Upload your sales data and get a forecast using Facebook Prophet.")
st.markdown("The file must include two columns: `date` and `sales`.")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("✅ File uploaded successfully!")

        if 'date' not in df.columns or 'sales' not in df.columns:
            st.error("❌ The file must contain 'date' and 'sales' columns.")
        else:
            df['date'] = pd.to_datetime(df['date'])
            df = df[['date', 'sales']].rename(columns={"date": "ds", "sales": "y"})

            st.subheader("📈 Uploaded Data")
            st.dataframe(df.tail())

            periods_input = st.number_input("How many days do you want to forecast?", min_value=1, max_value=365, value=30)

            if st.button("🔮 Generate Forecast"):
                model = Prophet()
                model.fit(df)

                future = model.make_future_dataframe(periods=periods_input)
                forecast = model.predict(future)

                st.subheader("📉 Forecast Results")
                fig1 = plot_plotly(model, forecast)
                st.plotly_chart(fig1)

                st.subheader("🔍 Forecast Data")
                st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    except Exception as e:
        st.error(f"❌ Error: {e}")
