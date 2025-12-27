import express from "express";
import cors from "cors";

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// === Book content ===
const BOOK_CONTENT = `
# Physical AI & Humanoid Robotics

## Book Description
This book is a spec-driven guide for building intelligent humanoid robots.
It covers Physical AI, embodied intelligence, ROS 2, simulation environments,
AI perception, navigation, and vision-language-action systems.

## Chapters
1. Introduction to Physical AI & Embodied Intelligence
2. Systems
3. Tutorial - Basics
4. Simulation
5. Tutorial - Extras
6. AI Perception & Navigation
7. Vision-Language-Action
8. Capstone
`;

// --- Function to answer book-related questions or greetings ---
function getBookAnswer(question) {
  const q = question.toLowerCase().trim();

  // Greetings
  if (q === "hello" || q === "hi" || q === "hey") {
    return "Hello! 😊 How can I help you today?";
  }

  // Book keywords
  const bookKeywords = [
    "book", "chapters", "description", "physical ai", "ros",
    "simulation", "ai perception", "navigation",
    "vision-language-action", "capstone", "tell me about"
  ];

  const isBookQuestion = bookKeywords.some(keyword => q.includes(keyword));
  if (!isBookQuestion) return null;

  if (q.includes("chapters") || q.includes("how many chapters")) {
    const chapterLines = BOOK_CONTENT
      .split("\n")
      .filter(line => line.match(/^\d+\./));
    return "Chapters:\n" + chapterLines.join("\n");
  }

  if (q.includes("description") || q.includes("about this book") || q.includes("tell me about")) {
    const descMatch = BOOK_CONTENT.match(/## Book Description\s+([\s\S]+?)\n##/);
    if (descMatch) return descMatch[1].trim();
    return "This book is about Physical AI & Humanoid Robotics.";
  }

  if (q.includes("physical ai")) return "Physical AI is the study of robots with embodied intelligence interacting with the physical world.";
  if (q.includes("ros 2") || q.includes("ros")) return "ROS 2 is used for robot control, simulation, and integration of AI perception and navigation.";
  if (q.includes("simulation")) return "Simulation environments are discussed for safely testing humanoid robots.";
  if (q.includes("ai perception") || q.includes("navigation")) return "AI Perception & Navigation teaches how robots perceive environments and plan movements.";
  if (q.includes("vision-language-action")) return "Vision-Language-Action integrates visual input with language understanding to guide robot actions.";
  if (q.includes("capstone")) return "The Capstone chapter integrates all concepts into a final humanoid robotics project.";

  return "This book is about Physical AI & Humanoid Robotics.";
}

// --- POST /chat route ---
app.post("/chat", (req, res) => {
  const { message } = req.body;
  if (!message) return res.status(400).json({ reply: "Message is required" });

  const answer = getBookAnswer(message);

  if (answer) {
    res.json({ reply: answer });
  } else {
    res.json({ reply: "I can mostly answer questions about the book." });
  }
});

// --- GET / route (friendly message) ---
app.get("/", (req, res) => {
  res.send("✅ Backend is running. Use POST /chat to interact with the book chatbot.");
});

// --- Start server ---
app.listen(PORT, () => {
  console.log(`✅ Backend running at http://localhost:${PORT}`);
});
