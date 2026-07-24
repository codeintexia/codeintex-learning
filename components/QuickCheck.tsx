'use client'

import { useState } from 'react'

interface QuickCheckProps {
  question: string
  answer?: string
}

export default function QuickCheck({ question, answer }: QuickCheckProps) {
  const [checked, setChecked] = useState(false)

  return (
    <div className="my-[48px] bg-gradient-to-br from-[#f0fdfa] to-[#e6fffa] border-[1.5px] border-[#5eead4] rounded-[12px] p-[28px] relative overflow-hidden shadow-none">
      {/* Decorative shape in the top-right corner */}
      <div className="absolute -top-[20px] -right-[20px] w-[80px] h-[80px] bg-[radial-gradient(circle,rgba(13,148,136,0.08)_0%,transparent_70%)] rounded-full pointer-events-none" />
      
      {/* Quick Check Label with lightning bolt emoji */}
      <div className="flex items-center gap-2 mb-3">
        <span className="text-[14px]">⚡</span>
        <p className="text-[11px] font-bold uppercase tracking-[0.1em] text-[#0d9488]">
          Quick Check
        </p>
      </div>
      
      {/* Question Text */}
      <p className="text-[16px] leading-[1.65] font-medium text-[#0f172a] mb-5">{question}</p>
      
      {!checked ? (
        <button
          onClick={() => setChecked(true)}
          className="inline-flex items-center justify-center rounded-[8px] bg-[#0d9488] text-white px-5 py-2.5 text-[14px] font-semibold border-none cursor-pointer transition-colors duration-150 hover:bg-[#0f766e] focus:outline-none"
        >
          Lihat Jawaban →
        </button>
      ) : (
        /* Checked State Message & Answer Reveal */
        <div className="space-y-3">
          <div className="flex items-center gap-2 text-[14px] font-semibold text-[#0f766e]">
            <span>✓</span>
            <span>{answer ? 'Jawaban & Pembahasan:' : 'Bagus — lanjutkan ke analisis kasus.'}</span>
          </div>
          {answer && (
            <div className="bg-white/80 border border-[#99f6e4] rounded-[8px] p-4 text-[14px] leading-[1.65] text-[#334155] whitespace-pre-line">
              {answer}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
