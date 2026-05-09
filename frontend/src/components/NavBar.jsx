import React from 'react'

function NavBar() {
  return (
    <div className='flex items-center justify-between'>
        <div className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-md border border-zinc-800 bg-zinc-900/50">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-emerald-400">
                <path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z" />
              </svg>
            </div>
            <span className="text-md font-medium tracking-tight text-zinc-100">CyberLabs.</span>
        </div>

        <span className="text-xs text-zinc-800 font-normal px-4 py-1 rounded-2xl bg-green-400">Try Free</span>
    </div>
  )
}

export default NavBar
