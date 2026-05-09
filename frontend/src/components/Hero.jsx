import React from 'react'
import Input from './Input'
import Results from './Results'

function Hero() {
  return (
    <main className="flex flex-1 flex-col justify-center py-8">
        <div className="mb-10 space-y-4">
            <span className="inline-flex items-center gap-2 rounded-full border border-zinc-800 bg-zinc-900/40 px-3 py-1 text-xs text-zinc-400">
                <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                Real-time URL analysis
            </span>
            <h1 className="text-4xl font-semibold tracking-tight text-zinc-50 sm:text-5xl">
            Smart Phishing URL
            <br />
            <span className="text-zinc-500">Detection System</span>
            </h1>
            <p className="max-w-lg text-sm leading-relaxed text-zinc-400">
            Paste any link below. We run it through ten lexical and structural
            heuristics to flag potential phishing attempts before you click.
            </p>
        </div>

        {/* Input */}
        <Input />
        
        {/* Result */}
        
        {/* <Results /> */}
        
    </main>
  )
}

export default Hero
