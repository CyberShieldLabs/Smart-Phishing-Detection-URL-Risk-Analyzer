import React from 'react'

function AmbBg() {
  return (
    <div>
      <div className="pointer-events-none fixed inset-0 overflow-hidden">
        <div className="absolute -top-40 -left-40 h-[500px] w-[500px] rounded-full bg-emerald-500/10 blur-[120px]" />
        <div className="absolute -bottom-40 -right-40 h-[500px] w-[500px] rounded-full bg-sky-500/5 blur-[120px]" />
      </div>
    </div>
  )
}

export default AmbBg
