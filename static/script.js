// ChatGPT Clone - JavaScript functionality
class ChatApp {
    constructor() {
        this.initializeElements();
        this.bindEvents();
        this.setupAutoResize();
        this.updateCharCount();
    }

    initializeElements() {
        this.messageInput = document.getElementById('message-input');
        this.sendButton = document.getElementById('send-button');
        this.chatMessages = document.getElementById('chat-messages');
        this.modelSelect = document.getElementById('model-select');
        this.temperatureSlider = document.getElementById('temperature');
        this.tempValue = document.getElementById('temp-value');
        this.clearButton = document.getElementById('clear-chat');
        this.loading = document.getElementById('loading');
        this.errorModal = document.getElementById('error-modal');
        this.errorMessage = document.getElementById('error-message');
        
        // Check if all required elements exist
        if (!this.messageInput || !this.sendButton || !this.chatMessages) {
            console.error('Required elements not found');
            return;
        }
    }

    bindEvents() {
        // Send message events
        if (this.sendButton) {
            this.sendButton.addEventListener('click', () => this.sendMessage());
        }
        
        if (this.messageInput) {
            this.messageInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    this.sendMessage();
                }
            });

            // Input events
            this.messageInput.addEventListener('input', () => {
                this.updateCharCount();
                this.updateSendButton();
            });
        }

        // Temperature control
        if (this.temperatureSlider) {
            this.temperatureSlider.addEventListener('input', (e) => {
                if (this.tempValue) {
                    this.tempValue.textContent = e.target.value;
                }
            });
        }

        // Clear chat
        if (this.clearButton) {
            this.clearButton.addEventListener('click', () => this.clearChat());
        }

        // Close modal
        const closeModal = document.querySelector('.close-modal');
        if (closeModal && this.errorModal) {
            closeModal.addEventListener('click', () => {
                this.closeErrorModal();
            });

            // Close modal when clicking outside
            this.errorModal.addEventListener('click', (e) => {
                if (e.target === this.errorModal) {
                    this.closeErrorModal();
                }
            });
        }
    }

    setupAutoResize() {
        if (this.messageInput) {
            this.messageInput.addEventListener('input', () => {
                this.messageInput.style.height = 'auto';
                this.messageInput.style.height = Math.min(this.messageInput.scrollHeight, 120) + 'px';
            });
        }
    }

    updateCharCount() {
        if (this.messageInput) {
            const count = this.messageInput.value.length;
            document.querySelector('.char-count').textContent = `${count}/4000`;
        }
    }

    updateSendButton() {
        if (this.sendButton) {
            const hasText = this.messageInput.value.trim().length > 0;
            this.sendButton.disabled = !hasText;
        }
    }

    async sendMessage() {
        if (!this.messageInput) return;

        const message = this.messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        this.addMessage(message, 'user');
        this.messageInput.value = '';
        this.updateCharCount();
        this.updateSendButton();
        this.setupAutoResize();

        // Show loading
        this.showLoading();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    model: this.modelSelect ? this.modelSelect.value : 'gpt-4', // Default to gpt-4 if modelSelect is missing
                    temperature: this.temperatureSlider ? parseFloat(this.temperatureSlider.value) : 0.7, // Default to 0.7 if slider is missing
                    max_tokens: 1000
                })
            });

            const data = await response.json();

            if (data.success) {
                // Add assistant response to chat
                this.addMessage(data.response, 'assistant');
            } else {
                this.showError(data.error || 'Failed to get response from AI');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            this.showError('Network error. Please try again.');
        } finally {
            this.hideLoading();
        }
    }

    addMessage(content, role) {
        if (!this.chatMessages) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;
        
        const timestamp = new Date().toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit'
        });

        const avatarIcon = role === 'user' ? 'fas fa-user' : 'fas fa-robot';
        
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="${avatarIcon}"></i>
            </div>
            <div class="message-content">
                <div class="message-text">${this.escapeHtml(content)}</div>
                <div class="message-timestamp">${timestamp}</div>
            </div>
        `;

        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    scrollToBottom() {
        if (this.chatMessages) {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }
    }

    async clearChat() {
        if (!this.chatMessages) return;

        try {
            const response = await fetch('/api/clear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const data = await response.json();
            
            if (data.success) {
                // Keep only the welcome message
                const welcomeMessage = this.chatMessages.querySelector('.assistant-message');
                this.chatMessages.innerHTML = '';
                if (welcomeMessage) {
                    this.chatMessages.appendChild(welcomeMessage);
                }
            }
        } catch (error) {
            console.error('Error clearing chat:', error);
        }
    }

    showLoading() {
        if (this.loading) {
            this.loading.classList.remove('hidden');
        }
    }

    hideLoading() {
        if (this.loading) {
            this.loading.classList.add('hidden');
        }
    }

    showError(message) {
        if (this.errorMessage) {
            this.errorMessage.textContent = message;
        }
        if (this.errorModal) {
            this.errorModal.classList.remove('hidden');
        }
    }

    closeErrorModal() {
        if (this.errorModal) {
            this.errorModal.classList.add('hidden');
        }
    }

    // Utility method to format code blocks
    formatCodeBlocks(text) {
        return text.replace(/```(\w+)?\n([\s\S]*?)```/g, (match, lang, code) => {
            const language = lang || 'text';
            return `<pre><code class="language-${language}">${this.escapeHtml(code.trim())}</code></pre>`;
        });
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
    
    // Add some helpful keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + K to focus input
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            document.getElementById('message-input').focus();
        }
        
        // Ctrl/Cmd + L to clear chat
        if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
            e.preventDefault();
            document.getElementById('clear-chat').click();
        }
    });
});

// Add some visual feedback for better UX
document.addEventListener('DOMContentLoaded', () => {
    // Add typing indicator
    let typingTimeout;
    
    document.getElementById('message-input').addEventListener('input', () => {
        clearTimeout(typingTimeout);
        
        // Show typing indicator after 1 second of no input
        typingTimeout = setTimeout(() => {
            // You could add a typing indicator here if needed
        }, 1000);
    });
    
    // Add smooth scrolling
    const chatMessages = document.querySelector('.chat-messages');
    chatMessages.style.scrollBehavior = 'smooth';
    
    // Add hover effects for messages
    document.addEventListener('mouseover', (e) => {
        if (e.target.closest('.message')) {
            e.target.closest('.message').style.transform = 'translateX(5px)';
            e.target.closest('.message').style.transition = 'transform 0.2s ease';
        }
    });
    
    document.addEventListener('mouseout', (e) => {
        if (e.target.closest('.message')) {
            e.target.closest('.message').style.transform = 'translateX(0)';
        }
    });
});
