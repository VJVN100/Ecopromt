document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prompt-form');
    const input = document.getElementById('prompt-input');
    const engineSelect = document.getElementById('engine-select');
    const loadingIndicator = document.getElementById('loading-indicator');
    const errorToast = document.getElementById('error-toast');
    const errorMessage = document.getElementById('error-message');
    const resultContainer = document.getElementById('result-container');
    
    // Result elements
    const engineName = document.getElementById('engine-name');
    const responseContent = document.getElementById('response-content');
    const esifValue = document.getElementById('esif-value');
    const esifDelta = document.getElementById('esif-delta');
    const co2Value = document.getElementById('co2-value');
    const co2Delta = document.getElementById('co2-delta');
    const timeValue = document.getElementById('time-value');
    const tokenDelta = document.getElementById('token-delta');
    const complexityCaption = document.getElementById('complexity-caption');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const promptText = input.value.trim();
        if (!promptText) return;
        
        // UI Reset
        errorToast.classList.add('hidden');
        resultContainer.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        
        try {
            const response = await fetch('/api/route', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    prompt: promptText,
                    engine: engineSelect.value
                })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.detail || 'An unknown error occurred');
            }
            
            // Render Success
            renderResult(data);
            
            // Check for fallback warning
            if (data.fallback_triggered) {
                showError('Local Engine failed. Auto-falling back to Cloud! 🚀', true);
            }
            
        } catch (err) {
            showError(err.message);
        } finally {
            loadingIndicator.classList.add('hidden');
        }
    });
    
    function renderResult(data) {
        // Engine
        engineName.textContent = `Response (via ${data.engine})`;
        
        // Markdown parsing for response
        responseContent.innerHTML = marked.parse(data.response);
        
        // Metrics
        esifValue.textContent = `${data.esif}/100`;
        if (data.esif > 70) {
            esifDelta.textContent = 'Eco-Friendly 🌱';
            esifDelta.className = 'metric-delta positive';
        } else {
            esifDelta.textContent = 'Resource Intensive ⚠️';
            esifDelta.className = 'metric-delta negative';
        }
        
        co2Value.textContent = `${data.co2}g`;
        co2Delta.textContent = data.co2 > 0 ? `${data.co2}g saved` : '0g saved';
        co2Delta.className = data.co2 > 0 ? 'metric-delta positive' : 'metric-delta neutral';
        
        timeValue.textContent = `${data.time}s`;
        tokenDelta.textContent = `${data.tokens} Tokens`;
        
        complexityCaption.innerHTML = `*Prompt optimized before routing. Complexity Score was strictly <strong>${data.complexity_score}</strong>.*`;
        
        resultContainer.classList.remove('hidden');
    }
    
    function showError(msg, isWarning = false) {
        errorMessage.textContent = msg;
        errorToast.classList.remove('hidden');
        
        if (isWarning) {
            errorToast.style.borderColor = 'rgba(245, 158, 11, 0.3)';
            errorToast.style.background = 'rgba(245, 158, 11, 0.1)';
            errorToast.style.color = '#FCD34D';
        } else {
            errorToast.style.borderColor = 'rgba(239, 68, 68, 0.3)';
            errorToast.style.background = 'rgba(239, 68, 68, 0.1)';
            errorToast.style.color = '#FCA5A5';
        }
        
        // Auto-hide toast after 5s
        setTimeout(() => {
            errorToast.classList.add('hidden');
        }, 5000);
    }
});
