# ChatGPT Clone 2.0

A modern, responsive ChatGPT clone built with **Python (Flask)**, **HTML**, and **CSS**. This application provides a free ChatGPT-like experience using **local AI models** or external APIs.

## ✨ Features

- **Modern UI/UX**: Beautiful, responsive design that works on all devices
- **Real-time Chat**: Instant AI responses with typing indicators
- **Model Selection**: Choose from multiple AI models (GPT-3.5-turbo, GPT-4, etc.)
- **Temperature Control**: Adjust AI creativity and randomness
- **Chat History**: Maintains conversation context during your session
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Keyboard Shortcuts**: Quick access to common functions
- **Error Handling**: Graceful error handling with user-friendly messages
- **🆕 Local AI Models**: Run AI models locally without API keys!

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- **🆕 Node.js v19+** (for local AI models)
- **🆕 Git** (for downloading local AI models)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd chatgpt_clone_2.0
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **🆕 Set up Local AI Models (Recommended)**
   ```bash
   # Windows
   setup_local_api.bat
   
   # Linux/Mac
   chmod +x setup_local_api.sh
   ./setup_local_api.sh
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### 🆕 Local AI Models (No API Keys Required!)

This project now supports **local AI models** using the [PawanOsman/ChatGPT](https://github.com/PawanOsman/ChatGPT) repository:

- **No API keys needed** - runs completely locally
- **Free AI responses** - no rate limits or costs
- **Privacy** - all data stays on your machine
- **Full control** - customize and modify as needed

#### Setting Up Local AI Models

1. **Run the setup script**:
   ```bash
   # Windows
   setup_local_api.bat
   
   # Linux/Mac
   ./setup_local_api.sh
   ```

2. **Start the local AI API**:
   ```bash
   cd local-api/ChatGPT
   npm start
   ```

3. **Start your Flask app** (in another terminal):
   ```bash
   python app.py
   ```

4. **Test the integration**:
   ```bash
   python test_local_api.py
   ```

### Environment Variables (Optional)

Create a `.env` file in the root directory:

```env
# Server Configuration
PORT=5000
NODE_ENV=development

# API Configuration (for external APIs)
API_BASE_URL=http://localhost:3040/v1  # Local AI API
API_KEY=anything  # Local API accepts any key
```

### Default Settings

- **Port**: 5000
- **🆕 API Base URL**: http://localhost:3040/v1 (Local AI API)
- **🆕 API Key**: anything (Local API accepts any key)

## 📱 Usage

### Basic Chat

1. Type your message in the input field
2. Press Enter or click the send button
3. Wait for the AI response
4. Continue the conversation naturally

### Advanced Features

- **Model Selection**: Choose different AI models from the dropdown
- **Temperature Control**: Adjust the slider to control AI creativity (0.0 = focused, 2.0 = creative)
- **Clear Chat**: Use the trash button to start a new conversation
- **Keyboard Shortcuts**:
  - `Ctrl/Cmd + K`: Focus on input field
  - `Ctrl/Cmd + L`: Clear chat history

## 🏗️ Project Structure

```
chatgpt_clone_2.0/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── 🆕 LOCAL_API_SETUP.md # Local AI setup guide
├── 🆕 setup_local_api.bat # Windows setup script
├── 🆕 setup_local_api.ps1 # PowerShell setup script
├── 🆕 test_local_api.py  # Local API test script
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # CSS styles
    └── script.js         # JavaScript functionality
```

## 🌐 API Endpoints

- `GET /` - Main chat interface
- `POST /api/chat` - Send message and get AI response
- `POST /api/clear` - Clear chat history
- `GET /api/models` - Get available AI models
- `GET /health` - Health check endpoint
- `GET /test` - Test endpoint with configuration info

## 🎨 Customization

### Styling

Modify `static/style.css` to customize:
- Colors and themes
- Layout and spacing
- Animations and transitions
- Responsive breakpoints

### Functionality

Edit `static/script.js` to add:
- New features
- Different keyboard shortcuts
- Custom animations
- Additional UI interactions

### Backend

Modify `app.py` to:
- Add new API endpoints
- Change AI model behavior
- Implement user authentication
- Add database integration

### 🆕 Local AI Models

Customize the local AI behavior by editing files in `local-api/ChatGPT/src/`:
- Model parameters (temperature, max tokens, etc.)
- Response formatting
- Rate limiting

## 🔒 Security Notes

- Change the `secret_key` in `app.py` for production use
- Consider implementing rate limiting for production
- Add proper error handling and logging
- Use HTTPS in production environments
- **🆕 Local AI models provide enhanced privacy** - all data stays on your machine

## 🌟 Features in Detail

### Responsive Design
- Mobile-first approach
- Adaptive layouts for all screen sizes
- Touch-friendly interface elements

### Modern UI Elements
- Gradient backgrounds and buttons
- Smooth animations and transitions
- Loading indicators and feedback
- Error modals with clear messaging

### Chat Experience
- Real-time message display
- Auto-scrolling to latest messages
- Message timestamps
- User and AI message differentiation

### 🆕 Local AI Integration
- Seamless fallback between local and external APIs
- Mock responses when all APIs are unavailable
- Comprehensive error handling and logging
- Support for multiple AI providers

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### 🆕 Local AI Models
```bash
# Terminal 1: Start local AI API
cd local-api/ChatGPT
npm start

# Terminal 2: Start Flask app
python app.py
```

### Production Deployment
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- **🆕 Local AI models from [PawanOsman/ChatGPT](https://github.com/PawanOsman/ChatGPT)**
- Uses the [PawanOsman/ChatGPT](https://github.com/PawanOsman/ChatGPT) reverse proxy
- Inspired by the original ChatGPT interface
- Icons from [Font Awesome](https://fontawesome.com/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include your Python version and operating system
4. **🆕 For local AI issues, check [LOCAL_API_SETUP.md](LOCAL_API_SETUP.md)**

## 🔄 Updates

Stay updated with the latest features and improvements by:
- Starring this repository
- Watching for updates
- Checking the releases page

## 🆕 What's New

- **Local AI Models**: Run AI models locally without external API keys
- **Enhanced Fallback System**: Smart fallback between local and external APIs
- **Setup Scripts**: Automated setup for local AI models
- **Comprehensive Testing**: Test scripts to verify local API functionality
- **Better Error Handling**: Improved error messages and fallback responses

---

**Happy Local AI Chatting! 🤖✨**
