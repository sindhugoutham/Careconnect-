import React, { useState } from 'react';
import { askPolicyQuestion } from '../api/api';

const PolicyAssistant = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError(null);
    setResponse(null);
    
    try {
      const data = await askPolicyQuestion(question);
      if (data.answer.includes("error processing")) {
         setError("Failed to communicate with AI. Please make sure Ollama is running.");
      } else {
         setResponse(data.answer);
      }
    } catch (err) {
      setError("An unexpected error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="section">
      <h3>Policy Assistant</h3>
      <p style={{marginBottom: '1rem', color: '#666'}}>Ask anything about healthcare coverage, co-pays, and procedures.</p>
      <form onSubmit={handleSubmit} className="form-group">
        <input 
          type="text" 
          value={question} 
          onChange={(e) => setQuestion(e.target.value)} 
          placeholder="E.g., What is a co-pay?"
          disabled={loading}
        />
        <button type="submit" disabled={loading || !question.trim()}>
          {loading ? 'Asking AI...' : 'Ask'}
        </button>
      </form>
      {error && (
        <div style={{ padding: '1rem', backgroundColor: '#ffeeba', color: '#856404', borderRadius: '4px', marginTop: '1rem' }}>
          {error}
        </div>
      )}
      {response && (
        <div className="assistant-response" style={{ lineHeight: '1.8' }}>
          <strong>AI Answer:</strong>
          <p style={{ marginTop: '0.5rem' }}>{response}</p>
        </div>
      )}
    </section>
  );
};

export default PolicyAssistant;
