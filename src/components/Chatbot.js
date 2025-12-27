import React, {
  useState,
  useEffect,
  useRef,
  useImperativeHandle,
  forwardRef
} from "react";
import styles from "./Chatbot.module.css";

const Chatbot = forwardRef((props, ref) => {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! 😊 How can I help you today?" }
  ]);

  const messagesEndRef = useRef(null);

  useImperativeHandle(ref, () => ({
    toggleChat: () => setIsOpen(prev => !prev)
  }));

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userText = input;
    setInput("");
    setMessages(prev => [...prev, { role: "user", content: userText }]);

    try {
      // ✅ Make sure URL matches backend port
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
      });

      if (!response.ok) throw new Error("Network response not ok");

      const data = await response.json();

      setMessages(prev => [...prev, { role: "assistant", content: data.reply }]);
    } catch (error) {
      console.error("Chatbot fetch error:", error);
      setMessages(prev => [
        ...prev,
        { role: "assistant", content: "⚠️ Backend not reachable." }
      ]);
    }
  };

  if (!isOpen) return null;

  return (
    <div className={styles.chatWindow}>
      <div className={styles.header}>
        <span className={styles.headerTitle}>Book Chatbot</span>
        <button className={styles.closeBtn} onClick={() => setIsOpen(false)}>✕</button>
      </div>

      <div className={styles.chatBody}>
        {messages.map((msg, index) => (
          <div key={index} className={msg.role === "user" ? styles.userRow : styles.botRow}>
            <div className={styles.bubble}>{msg.content}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className={styles.footer}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
          placeholder="Type your message..."
          autoFocus
        />
        <button className={styles.sendBtn} onClick={sendMessage} disabled={!input.trim()}>➤</button>
      </div>
    </div>
  );
});

export default Chatbot;
