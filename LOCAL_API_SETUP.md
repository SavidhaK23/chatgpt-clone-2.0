# 🚀 Local ChatGPT API Setup Guide

This guide will help you set up the **PawanOsman/ChatGPT** local API to run your ChatGPT Clone without requiring external API keys!

## ✨ What This Gives You

- **No API keys required** - runs completely locally
- **Free AI responses** - no rate limits or costs
- **Privacy** - all data stays on your machine
- **Full control** - customize and modify as needed

## 📋 Prerequisites

Before starting, make sure you have:

- **Node.js v19+** - [Download here](https://nodejs.org/)
- **Git** - [Download here](https://git-scm.com/)
- **Python 3.7+** (already installed for your Flask app)

## 🚀 Quick Setup (Windows)

### Option 1: Automated Setup (Recommended)
1. **Double-click** `setup_local_api.bat` in your project folder
2. **Follow the prompts** - the script will handle everything automatically
3. **Wait for completion** - this may take a few minutes

### Option 2: Manual Setup
1. **Open PowerShell** as Administrator
2. **Run the setup script**:
   ```powershell
   .\setup_local_api.ps1
   ```

## 🚀 Quick Setup (Linux/Mac)

1. **Open terminal** in your project folder
2. **Make the script executable**:
   ```bash
   chmod +x setup_local_api.sh
   ```
3. **Run the setup script**:
   ```bash
   ./setup_local_api.sh
   ```

## 🔧 Manual Setup Steps

If you prefer to do it manually:

### 1. Clone the Repository
```bash
mkdir local-api
cd local-api
git clone https://github.com/PawanOsman/ChatGPT.git
cd ChatGPT
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start the Local API
```bash
npm start
```

The API will be available at: **http://localhost:3040**

## 🎯 Running Your ChatGPT Clone

### Step 1: Start the Local API
1. **Open a new terminal/command prompt**
2. **Navigate to the local API**:
   ```bash
   cd local-api/ChatGPT
   ```
3. **Start the API**:
   ```bash
   npm start
   ```
4. **Keep this terminal open** - the API needs to keep running

### Step 2: Start Your Flask App
1. **Open another terminal/command prompt**
2. **Navigate to your ChatGPT Clone project**:
   ```bash
   cd chatgpt_clone_2.0
   ```
3. **Start the Flask app**:
   ```bash
   python app.py
   ```

### Step 3: Test the Integration
1. **Open your browser** to `http://localhost:5000`
2. **Send a message** - it should now use the local AI model!
3. **Check the terminal** - you should see successful API calls to `localhost:3040`

## 🔍 Troubleshooting

### Common Issues

#### ❌ "npm start" not working
- Make sure you're in the `local-api/ChatGPT` directory
- Try running `npm install` again
- Check if Node.js version is 19 or higher

#### ❌ Port 3040 already in use
- Close any other applications using port 3040
- Or change the port in the ChatGPT API configuration

#### ❌ API not responding
- Make sure the local API is running (check terminal for errors)
- Verify the API is accessible at `http://localhost:3040`
- Check if your firewall is blocking the connection

#### ❌ Still getting mock responses
- Verify the local API is running on port 3040
- Check the Flask app logs for API connection errors
- Make sure both services are running simultaneously

### Getting Help

1. **Check the terminal output** for error messages
2. **Verify both services are running**:
   - Local API: `http://localhost:3040`
   - Flask App: `http://localhost:5000`
3. **Check the [PawanOsman/ChatGPT issues](https://github.com/PawanOsman/ChatGPT/issues)** for known problems

## 🌟 Advanced Configuration

### Customizing the Local API

You can modify the local API behavior by editing files in `local-api/ChatGPT/src/`:

- **Model parameters** - adjust temperature, max tokens, etc.
- **Response formatting** - customize how responses are generated
- **Rate limiting** - add your own rate limiting if needed

### Environment Variables

Create a `.env` file in `local-api/ChatGPT/` to customize:

```env
PORT=3040
NODE_ENV=development
# Add other configuration options as needed
```

## 🔄 Updating the Local API

To get the latest features and bug fixes:

1. **Navigate to the local API directory**:
   ```bash
   cd local-api/ChatGPT
   ```
2. **Pull the latest changes**:
   ```bash
   git pull
   ```
3. **Reinstall dependencies** (if needed):
   ```bash
   npm install
   ```
4. **Restart the API**:
   ```bash
   npm start
   ```

## 🎉 Success!

Once everything is working, you'll have:

- ✅ **Local AI model** running on your machine
- ✅ **No API costs** or rate limits
- ✅ **Full privacy** - all data stays local
- ✅ **Customizable** AI behavior
- ✅ **Always available** - works offline

Your ChatGPT Clone will now provide real AI responses using the local model instead of mock responses!

## 📚 Additional Resources

- **[PawanOsman/ChatGPT Repository](https://github.com/PawanOsman/ChatGPT)** - Official repository
- **[Discord Community](https://discord.pawan.krd)** - Get help and support
- **[Node.js Documentation](https://nodejs.org/docs/)** - Learn more about Node.js

---

**Happy Local AI Chatting! 🤖✨**
