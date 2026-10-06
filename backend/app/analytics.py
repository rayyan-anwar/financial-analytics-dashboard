import numpy as np
def analyze(df):
    if "close" not in df: raise ValueError("close column is required")
    x=df["close"].astype(float).dropna()
    r=x.pct_change().dropna()
    vol=float(r.std()*np.sqrt(252)) if len(r)>1 else 0
    dd=x/x.cummax()-1
    sharpe=float(r.mean()/r.std()*np.sqrt(252)) if r.std() else 0
    return {"latest_close":float(x.iloc[-1]),"annualized_volatility":vol,
            "max_drawdown":float(dd.min()),"sharpe_style_ratio":sharpe,"observations":int(len(x))}
