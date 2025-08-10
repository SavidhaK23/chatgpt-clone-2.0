from flask import Flask, render_template, request, jsonify, session
import requests
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Configuration - Google Gemini API only
API_BASE_URL = 'https://generativelanguage.googleapis.com/v1beta'
API_KEY = 'AIzaSyAOlq2dN66hGoQOWhiZMJ_lRmz4kRk52Sw'  # Working Gemini API key
PORT = int(os.getenv('PORT', 5000))

# Available models - Gemini models only
AVAILABLE_MODELS = [
    'gemini-1.5-flash',  # Working model
    'gemini-pro',
    'gemini-pro-vision'
]

@app.route('/')
def index():
    """Main chat interface"""
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', models=AVAILABLE_MODELS)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat completion requests with Google Gemini"""
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400

        message = data['message']
        model = data.get('model', 'gemini-1.5-flash')

        # Validate model for Gemini
        if model not in AVAILABLE_MODELS:
            model = 'gemini-1.5-flash'

        # Prepare Google Gemini API request
        api_request = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": message}]
                }
            ],
            "generationConfig": {
                "temperature": data.get('temperature', 0.7),
                "maxOutputTokens": data.get('max_tokens', 1000)
            }
        }

        headers = {
            'Content-Type': 'application/json'
        }

        # Google Gemini API uses API key as query parameter, not Bearer token
        endpoint = f"{API_BASE_URL}/models/{model}:generateContent?key={API_KEY}"

        print(f"🌐 Sending to Gemini API: {endpoint}")
        print(f"📝 Payload: {json.dumps(api_request, indent=2)}")

        response = requests.post(endpoint, json=api_request, headers=headers, timeout=30)

        print(f"📡 Gemini API Status: {response.status_code}")
        print(f"📡 Response: {response.text}")

        if response.status_code != 200:
            return jsonify({'error': f'Gemini API Error: {response.status_code}', 'details': response.text}), response.status_code

        api_response = response.json()

        # Extract assistant's reply
        if "candidates" in api_response and len(api_response["candidates"]) > 0:
            assistant_message = api_response["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return jsonify({'error': 'No response from Gemini API'}), 500

        # Save to session chat history
        session.setdefault('chat_history', [])
        session['chat_history'].append({
            'id': str(uuid.uuid4()),
            'role': 'user',
            'content': message,
            'timestamp': datetime.now().isoformat()
        })
        session['chat_history'].append({
            'id': str(uuid.uuid4()),
            'role': 'assistant',
            'content': assistant_message,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({
            'success': True,
            'response': assistant_message,
            'model': model
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Network error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/clear', methods=['POST'])
def clear_chat():
    """Clear chat history"""
    session['chat_history'] = []
    return jsonify({'success': True, 'message': 'Chat history cleared'})

@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available models"""
    models = []
    for model_id in AVAILABLE_MODELS:
        models.append({
            'id': model_id,
            'object': 'model',
            'created': 1677610602,
            'owned_by': 'google'
        })
    
    return jsonify({
        'object': 'list',
        'data': models
    })

@app.route('/test')
def test():
    """Test endpoint to verify the application is working"""
    return jsonify({
        'status': 'OK',
        'message': 'ChatGPT Clone is working correctly with Google Gemini',
        'timestamp': datetime.now().isoformat(),
        'models': AVAILABLE_MODELS,
        'api_base': API_BASE_URL,
        'api_key_set': bool(API_KEY),
        'provider': 'Google Gemini'
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'message': 'ChatGPT Clone is running with Google Gemini',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"🚀 Starting ChatGPT Clone on port {PORT}")
    print(f"📡 API: {API_BASE_URL} (Google Gemini)")
    print(f"🔑 API Key: {'Set' if API_KEY else 'Not set'}")
    print(f"🤖 Models: {', '.join(AVAILABLE_MODELS)}")
    print(f"🌐 Web interface: http://localhost:{PORT}")
    print(f"🔍 Health check: http://localhost:{PORT}/health")
    print(f"🧪 Test endpoint: http://localhost:{PORT}/test")
    
    # Production-ready configuration
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=PORT, debug=debug_mode)
