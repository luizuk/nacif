"use client";
import { useState } from "react";
import axios from "axios";
import Cookies from "js-cookie";
import { useRouter } from "next/navigation";

export default function SigIn() {
  const [username, setUsername] = useState("nacif");
  const [password, setPassword] = useState("nacif123");
  const router = useRouter(); // Use useRouter from next/navigation

  const login = async () => {
    try {
      const response = await axios.post("http://localhost:8000/token", {
        username,
        password,
      });

      console.log("response", response);

      if (response.data.access_token) {
        Cookies.set("auth_token", response.data.access_token);
        router.push("/"); // Redirect to the home page
      } else {
        alert("Login failed!");
      }
    } catch (error) {
      console.error("Error logging in:", error);
      alert("An error occurred during login.");
    }
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
