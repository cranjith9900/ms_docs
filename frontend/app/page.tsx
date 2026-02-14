"use client";

import { useState } from "react";

export default function Home() {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  const sendRequest = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/hello/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name }),
    });

    const data = await res.json();
    setMessage(data.message);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>FastAPI + Next.js Demo 🚀</h1>

      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ border: "1px solid gray", padding: 8 }}
      />

      <button onClick={sendRequest} style={{ marginLeft: 10, padding: 8 }}>
        Say Hello
      </button>

      <p style={{ marginTop: 20 }}>{message}</p>
    </div>
  );
}
