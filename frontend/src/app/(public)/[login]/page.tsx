"use client";
import { useState } from "react";

export default function SigIn() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = () => {
    // Replace with your login logic
    console.log({ username, password });
  };

  return (
    <div className="w-full flex justify-center center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)] bg-black">
      <div className="flex flex-col gap-4">
        <h2 className="text-2xl text-white">Login</h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="bg-black text-white border border-white p-2 rounded"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="bg-black text-white border border-white p-2 rounded"
        />
        <button
          onClick={login}
          className="bg-white text-black px-4 py-2 rounded hover:bg-gray-300"
        >
          Login
        </button>
      </div>
    </div>
  );
}
