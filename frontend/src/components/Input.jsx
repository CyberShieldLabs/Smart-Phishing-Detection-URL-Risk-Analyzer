import React from 'react'

function Input() {
  return (
    <div>
      <div className="flex flex-col gap-3 sm:flex-row">
        <input
        type="text"
        // value={input}
        // onChange={(e) => setInput(e.target.value)}
        // onKeyDown={(e) => e.key === "Enter" && handleScan()}
        placeholder="https://example.com/login"
        className="flex-1 md:max-w-[50%] rounded-lg border border-zinc-800 bg-zinc-900/40 px-4 py-3 text-sm text-zinc-100 placeholder:text-zinc-600 outline-none transition focus:border-zinc-600 focus:bg-zinc-900/70"
        />
        <button
        // onClick={handleScan}
        // disabled={loading || !input.trim()}
        className="rounded-lg bg-zinc-100 px-5 py-3 text-sm font-medium cursor-pointer text-zinc-900 transition hover:bg-white disabled:cursor-not-allowed disabled:bg-zinc-800 disabled:text-zinc-500"
        >
        {/* {loading ? "Scanning…" : "Analyze URL"} */}Analyze URL
        </button>
        </div>
    </div>
  )
}

export default Input
