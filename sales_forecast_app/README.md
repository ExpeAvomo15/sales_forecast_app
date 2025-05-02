
# 🧠 Sales Forecast App (Prophet + Streamlit)

This project allows businesses to upload their historical sales data (CSV or Excel) and receive future sales forecasts using Facebook Prophet.

## 🔧 How It Works

- Upload a file with `date` and `sales` columns.
- Get automatic future sales predictions.
- Visualize trends, seasonality, and forecast curve.

## 🚀 Run Locally

```bash
git clone https://github.com/yourusername/sales-predictor
cd sales-predictor
pip install -r requirements.txt
streamlit run main.py
```

## 🐳 Run with Docker

```bash
docker build -t sales-predictor .
docker run -p 8501:8501 sales-predictor
```

Then open [http://localhost:8501](http://localhost:8501)

## 📁 Example File Format

| date       | sales |
|------------|-------|
| 2023-01-01 |  100  |
| 2023-01-02 |  150  |

## 👤 Author

Expe Avomo – AI & Blockchain Engineer
