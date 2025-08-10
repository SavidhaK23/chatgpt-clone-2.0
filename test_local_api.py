#!/usr/bin/env python3
"""
Test script for the local ChatGPT API
This script tests if the local PawanOsman ChatGPT API is running and responding correctly.
"""

import requests
import json
import sys

def test_local_api():
    """Test the local ChatGPT API"""
    
    local_api_url = "http://localhost:3040/v1/chat/completions"
    
    print("🧪 Testing Local ChatGPT API...")
    print(f"📍 API URL: {local_api_url}")
    print()
    
    # Test payload
    test_payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Hello! Please respond with 'Local API is working!' if you can see this message."
            }
        ],
        "temperature": 0.7,
        "max_tokens": 100,
        "stream": False
    }
    
    try:
        print("📤 Sending test request...")
        print(f"📝 Payload: {json.dumps(test_payload, indent=2)}")
        print()
        
        # Send request to local API
        response = requests.post(
            local_api_url,
            json=test_payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        print(f"📡 Response Status: {response.status_code}")
        print(f"📡 Response Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            print("✅ SUCCESS! Local API is working!")
            print()
            
            try:
                response_data = response.json()
                print("📄 Response Data:")
                print(json.dumps(response_data, indent=2))
                print()
                
                if 'choices' in response_data and len(response_data['choices']) > 0:
                    content = response_data['choices'][0]['message']['content']
                    print(f"🤖 AI Response: {content}")
                else:
                    print("⚠️  Response doesn't contain expected 'choices' field")
                    
            except json.JSONDecodeError:
                print("⚠️  Response is not valid JSON")
                print(f"📄 Raw response: {response.text}")
                
        else:
            print(f"❌ FAILED! API returned status {response.status_code}")
            print(f"📄 Error response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR!")
        print("The local ChatGPT API is not running or not accessible.")
        print()
        print("🔧 To fix this:")
        print("1. Make sure you've run the setup script")
        print("2. Start the local API: cd local-api/ChatGPT && npm start")
        print("3. Verify it's running on http://localhost:3040")
        
    except requests.exceptions.Timeout:
        print("❌ TIMEOUT ERROR!")
        print("The API request timed out. The local API might be slow or overloaded.")
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        print("Something unexpected went wrong while testing the API.")

def main():
    """Main function"""
    print("=" * 50)
    print("   Local ChatGPT API Test Script")
    print("=" * 50)
    print()
    
    test_local_api()
    
    print()
    print("=" * 50)
    print("Test completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
