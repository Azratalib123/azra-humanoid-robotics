export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
  const { message } = req.body;

  try {
    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=${GEMINI_API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contents: [{ parts: [{ text: message }] }] }),
      }
    );

    const data = await response.json();

    const reply = data.candidates?.[0]?.content?.[0]?.parts?.[0]?.text || "No response";
    res.status(200).json({ reply });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
}
