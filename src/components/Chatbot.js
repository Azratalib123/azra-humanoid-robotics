import React, {
  useState,
  useEffect,
  useRef,
  useImperativeHandle,
  forwardRef
} from 'react';
import styles from './Chatbot.module.css';

/* =========================
   FRIENDLY + CONCISE SYSTEM
========================= */
const SYSTEM_INSTRUCTION = `
You are a friendly, polite, and concise AI assistant.

Tone:
- Sound natural and human-like.
- Be short but warm.
- Do NOT be robotic.
- Avoid long explanations unless the user asks.

Greetings:
- If the user says "hello", "hi", or similar:
  Respond warmly, for example:
  "Hello! 😊 How are you? How can I help you today?"

Book Rules:
- You are the official assistant for the book "Physical AI & Humanoid Robotics".
- When asked about the book, answer briefly and clearly.
- Do NOT over-explain.
- If a topic is not part of the book, reply exactly:
  "This topic is not covered in the current version of the book."

Book Chapters:
1. Introduction to Physical AI & Embodied Intelligence
2. Systems
3. Tutorial - Basics
4. Simulation
5. Tutorial - Extras
6. AI Perception & Navigation
7. Vision-Language-Action
8. Capstone

General Questions:
- Answer simply and politely.
`;

const Chatbot = forwardRef((props, ref) => {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content:
        "Hello! 😊 How can I help you today?"
    }
  ]);

  const messagesEndRef = useRef(null);

  useImperativeHandle(ref, () => ({
    toggleChat: () => setIsOpen(true),
  }));

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userText = input;
    const userMessage = { role: 'user', content: userText };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    try {
      const API_KEY = "AIzaSyCCIWdmzu5OcCmAZ7j1aGtusepVSBd28xc";

      const apiUrl =
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`;

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          systemInstruction: {
            parts: [{ text: SYSTEM_INSTRUCTION }]
          },
          contents: [
            {
              role: 'user',
              parts: [{ text: userText }]
            }
          ]
        })
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error.message);
      }

      const botReply =
        data?.candidates?.[0]?.content?.parts?.[0]?.text ||
        "Sorry 😊 I couldn’t understand that.";

      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: botReply }
      ]);

    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: "⚠️ Sorry, something went wrong. Please try again."
        }
      ]);
    }
  };

  if (!isOpen) return null;

  return (
    <div className={styles.chatWindow}>
      {/* Header */}
      <div className={styles.header}>
        <span className={styles.headerTitle}>Chat Assistant</span>
        <button
          className={styles.closeBtn}
          onClick={() => setIsOpen(false)}
        >
          ✕
        </button>
      </div>

      {/* Chat Body */}
      <div className={styles.chatBody}>
        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.role === 'user' ? styles.userRow : styles.botRow}
          >
            <div className={styles.bubble}>{msg.content}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Footer */}
      <div className={styles.footer}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Type your message..."
        />
        <button className={styles.sendBtn} onClick={sendMessage}>
          ➤
        </button>
      </div>
    </div>
  );
});

export default Chatbot;

