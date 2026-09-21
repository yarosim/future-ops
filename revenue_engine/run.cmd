@echo off
rem Revenue Engine hourly runner (launched by Task Scheduler "RevenueEngine").
cd /d "C:\Users\YAROS\.openclaw\workspace"
uv run python revenue_engine\run_revenue_engine.py >> revenue_engine\engine.log 2>&1