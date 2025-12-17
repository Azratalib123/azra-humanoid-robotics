import React, { useState, useEffect, useRef, useImperativeHandle, forwardRef } from 'react';
import styles from './Chatbot.module.css';

const Chatbot = forwardRef((props, ref) => {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { role: 'assistant', content: "Hello.. I'm listening! Go on.." }
  ]);
  const messagesEndRef = useRef(null);

  useImperativeHandle(ref, () => ({
    toggleChat: () => setIsOpen(true)
  }));

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');

    try {
      
      const MY_KEY = "AIzaSyDSE5qVk9uSSF76kEdDnF7fi7Wn6gbk8_g"; 
      
     
      const api_url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${MY_KEY}`;

      const response = await fetch(api_url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: input }] }]
        }),
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error.message);
      }

      if (data.candidates && data.candidates[0].content) {
        const botReply = data.candidates[0].content.parts[0].text;
        setMessages(prev => [...prev, { role: 'assistant', content: botReply }]);
      }

    } catch (err) {
      console.error("Chat Error:", err);
      setMessages(prev => [...prev, { role: 'assistant', content: "System: " + err.message }]);
    }
  };

  if (!isOpen) return null;

  return (
    <div className={styles.chatWindow}>
      <div className={styles.header}>
        <span className={styles.headerTitle}>Chatbot!</span>
        <button onClick={() => setIsOpen(false)} className={styles.closeBtn}>✕</button>
      </div>
      
      <div className={styles.chatBody}>
        {messages.map((msg, i) => (
          <div key={i} className={msg.role === 'user' ? styles.userRow : styles.botRow}>
            <div className={styles.bubble}>{msg.content}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className={styles.footer}>
        <input 
          value={input} 
          onChange={(e) => setInput(e.target.value)} 
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Type a message" 
        />
        <button onClick={sendMessage} className={styles.sendBtn}>➤</button>
      </div>
    </div>
  );
});

export default Chatbot;