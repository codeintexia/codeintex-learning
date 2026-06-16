'use client'

import { useState } from 'react'

interface QuickCheckProps {
  question: string
}

export default function QuickCheck({ question }: QuickCheckProps) {
  const [checked, setChecked] = useState(false)

  return (
    <div className="my-8 rounded-xl border border-teal-100 bg-teal-50/50 p-6 shadow-sm backdrop-blur-sm transition-all duration-300 hover:border-teal-200">
      <div className="mb-2 flex items-center gap-2">
        <span className="flex h-5 w-5 items-center justify-center rounded-full bg-teal-600 text-[10px] font-bold text-white">
          ?
        </span>
        <p className="text-xs font-semibold uppercase tracking-wider text-teal-700">
          Quick Check
        </p>
      </div>
      <p className="mb-4 text-base text-slate-700 leading-relaxed font-medium">{question}</p>
      {!checked ? (
        <button
          onClick={() => setChecked(true)}
          className="inline-flex items-center justify-center rounded-lg bg-teal-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition-all duration-200 hover:bg-teal-700 hover:shadow-teal-100 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-offset-2 active:scale-95"
        >
          Saya sudah memikirkannya →
        </button>
      ) : (
        <div className="inline-flex items-center gap-2 text-sm font-semibold text-teal-700 bg-teal-100/60 px-4 py-2 rounded-lg border border-teal-200/50 animate-fade-in">
          <span>✓</span>
          <span>Bagus. Lanjutkan ke analisis kasus di bawah.</span>
        </div>
      )}
    </div>
  )
}
