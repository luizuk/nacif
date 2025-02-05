"use client";
export default function Home() {
  const logout = () => {};

  return (
    <div className="w-full flex justify-center center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)] bg-black">
      <div className="flex flex-col gap-4">
        <h2 className="text-2xl text-white">Authenticated</h2>
        <button
          onClick={logout}
          className="bg-white text-black px-4 py-2 rounded hover:bg-gray-300"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
