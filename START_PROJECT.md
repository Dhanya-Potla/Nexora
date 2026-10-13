# 🚀 How to Start the SupplyWise Project

## ⚠️ Current Issue:
Neo4j database is not running. The server tried to start but is stuck waiting for Neo4j.

---

## ✅ Solution - Start in This Order:

### **Step 1: Start Neo4j Database** 🗄️

1. Open **Neo4j Desktop** application
2. Find your database in the Projects section
3. Click the **▶ START** button
4. Wait until status shows **"Active"** (green)
5. Should take 10-15 seconds

**Verify Neo4j is running:**
```powershell
curl http://localhost:7474
```
Should return HTTP 200.

---

### **Step 2: Start the SupplyWise Server** 🌐

Open a terminal in the project folder and run:

```powershell
# Activate virtual environment
.venv\Scripts\activate

# Start the server
python -m uvicorn app.app:app --host 127.0.0.1 --port 8000 --reload
```

**You should see:**
```
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
[AerospaceHelper] Graph Store connected
Embeddings model loaded successfully.
```

---

### **Step 3: Open in Browser** 🌐

Once you see "Application startup complete", open:

- **SupplyWise Dashboard**: http://127.0.0.1:8000/supplywise
- **Analytics**: http://127.0.0.1:8000/analytics
- **Query API Test**: http://127.0.0.1:8000/supplywise/dashboard

---

## 🔧 Alternative: Run WITHOUT Neo4j

If you don't want to start Neo4j, the system will run in **basic mode**:

✅ **What Works:**
- Vector search (FAISS)
- Supplier data queries
- Risk calculations
- API endpoints

❌ **What's Limited:**
- No graph-based queries
- No entity relationship lookups
- Validation layer disabled

**To run in basic mode:**
Just start the server (Step 2) without Neo4j. It will show warnings but still work.

---

## 📋 Quick Command Reference:

### Check if Neo4j is running:
```powershell
curl http://localhost:7474
```

### Check if server is running:
```powershell
curl http://127.0.0.1:8000/supplywise/dashboard
```

### Start server with auto-reload:
```powershell
.venv\Scripts\activate
python -m uvicorn app.app:app --host 127.0.0.1 --port 8000 --reload
```

### Stop server:
Press `Ctrl+C` in the terminal

---

## 🐛 Troubleshooting:

### "Port 8000 already in use"
```powershell
# Find process on port 8000
netstat -ano | findstr :8000

# Kill it (replace PID with actual number)
taskkill /PID <PID> /F
```

### "Neo4j connection failed"
- Make sure Neo4j Desktop is open
- Click START on your database instance
- Wait for "Active" status
- Restart the server

### "Module not found"
```powershell
# Make sure virtual environment is activated
.venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

---

## ✅ Current Project Status:

- ✅ Python environment ready
- ✅ All dependencies installed
- ✅ Ollama running with llama3 model
- ✅ Embeddings model cached
- ✅ Supplier data populated (30 suppliers)
- ⚠️ **Neo4j needs to be started**
- ⚠️ **Server stopped (waiting for Neo4j)**

---

## 🎯 What To Do Now:

**Option 1: Full Features (Recommended)**
1. Start Neo4j Desktop → Start Database
2. Run: `python -m uvicorn app.app:app --host 127.0.0.1 --port 8000 --reload`
3. Open: http://127.0.0.1:8000/supplywise

**Option 2: Quick Start (Without Graph)**
1. Run: `python -m uvicorn app.app:app --host 127.0.0.1 --port 8000 --reload`
2. Ignore Neo4j warnings
3. Open: http://127.0.0.1:8000/supplywise

---

Would you like me to try starting the server in basic mode (without Neo4j)?
