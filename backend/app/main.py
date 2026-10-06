from fastapi import FastAPI
app=FastAPI(title="Rayyan Anwar | Financial Analytics API",
 description="Financial analytics service by Rayyan Anwar.")
@app.get("/health")
def health():
    return {"status":"ok","author":"Rayyan Anwar","service":"financial-analytics-dashboard"}
