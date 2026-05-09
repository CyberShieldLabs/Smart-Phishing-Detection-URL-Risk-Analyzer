import React from 'react'

function Results() {
  return (
    <div>
      {/* {result && (
              <div className="mt-10 space-y-6 rounded-xl border border-zinc-800 bg-zinc-900/30 p-6 backdrop-blur">
                <div className="flex items-center justify-between gap-4">
                  <div className="min-w-0">
                    <p className="truncate text-xs text-zinc-500">{result.url}</p>
                    <p className="mt-1 text-2xl font-semibold text-zinc-50">
                      {result.score}
                      <span className="text-sm font-normal text-zinc-500"> / 100 trust score</span>
                    </p>
                  </div>
                  <span
                    className={`rounded-full border px-3 py-1 text-xs font-medium uppercase tracking-wider ${verdictColor}`}
                  >
                    {result.verdict}
                  </span>
                </div>

                <div className="h-1 w-full overflow-hidden rounded-full bg-zinc-800">
                  <div
                    className={`h-full transition-all duration-700 ${
                      result.verdict === "safe"
                        ? "bg-emerald-400"
                        : result.verdict === "suspicious"
                        ? "bg-amber-400"
                        : "bg-rose-400"
                    }`}
                    style={{ width: `${result.score}%` }}
                  />
                </div>

                <div className="grid gap-2 sm:grid-cols-2">
                  {result.signals.map((s) => (
                    <div
                      key={s.label}
                      className="flex items-center gap-2 rounded-md border border-zinc-800/60 bg-zinc-900/40 px-3 py-2 text-xs"
                    >
                      <span
                        className={`flex h-4 w-4 items-center justify-center rounded-full ${
                          s.hit ? "bg-emerald-400/15 text-emerald-400" : "bg-rose-400/15 text-rose-400"
                        }`}
                      >
                        {s.hit ? "✓" : "✕"}
                      </span>
                      <span className={s.hit ? "text-zinc-300" : "text-zinc-500"}>{s.label}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {!result && (
              <div className="mt-10 grid grid-cols-3 gap-3 text-center">
                {[
                  { k: "10", v: "Heuristics" },
                  { k: "<1s", v: "Detection" },
                  { k: "100%", v: "Client-side" },
                ].map((s) => (
                  <div key={s.v} className="rounded-lg border border-zinc-800/60 bg-zinc-900/30 p-4">
                    <p className="text-lg font-semibold text-zinc-100">{s.k}</p>
                    <p className="text-xs text-zinc-500">{s.v}</p>
                  </div>
                ))}
              </div>
            )} */}
    </div>
  )
}

export default Results
