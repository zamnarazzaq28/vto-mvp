#!/bin/bash

# Zamna Boutique - Virtual Try-On Launch Script

echo "👗 Starting Zamna Boutique VTO Suite..."

# 1. Start FastAPI Backend in background
echo "📦 Initializing AI Backend (FastAPI)..."
./fashn-env/bin/python3.10 api.py &
BACKEND_PID=$!

# 2. Wait for backend to potentially start loading models
sleep 2

# 3. Start Frontend Dev Server
echo "🎨 Launching Boutique UI (Next.js)..."
cd frontend
npm run dev

# Cleanup background process on exit
kill $BACKEND_PID
echo "👋 Boutique closed successfully."
