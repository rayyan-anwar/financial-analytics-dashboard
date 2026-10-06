import streamlit as st
import pandas as pd
from backend.app.analytics import analyze
st.set_page_config(page_title="Rayyan Anwar | Financial Analytics",layout="wide")
st.title("Financial Analytics Dashboard")
st.caption("Designed by Rayyan Anwar — AI/ML · Data Analytics · Technology Management")
f=st.file_uploader("Upload CSV with a close column",type=["csv"])
if f:
    df=pd.read_csv(f); st.dataframe(df.tail(20),use_container_width=True)
    try:
        m=analyze(df); c=st.columns(4)
        c[0].metric("Latest close",f"{m['latest_close']:.2f}")
        c[1].metric("Annualized volatility",f"{m['annualized_volatility']:.2%}")
        c[2].metric("Max drawdown",f"{m['max_drawdown']:.2%}")
        c[3].metric("Sharpe-style ratio",f"{m['sharpe_style_ratio']:.2f}")
        st.line_chart(df[["close"]].dropna())
        st.info("Historical analytics only — not financial advice.")
    except ValueError as e: st.error(str(e))
