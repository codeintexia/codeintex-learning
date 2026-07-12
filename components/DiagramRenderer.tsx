interface DiagramProps {
  title: string
  spec: string
}

export default function DiagramPlaceholder({ title, spec }: DiagramProps) {
  const lines = spec.split('\n').map(line => line.trim()).filter(Boolean);

  return (
    <div className="my-10 bg-[#f8fafc] border-[1.5px] border-dashed border-[#cbd5e1] rounded-[8px] p-[28px] shadow-none">
      <div className="flex items-center gap-2.5 mb-2 text-[#64748b]">
        <svg className="h-5 w-5 text-[#64748b]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        <span className="text-[14px] font-semibold">Blueprint: {title}</span>
      </div>
      
      <div className="rounded-lg bg-slate-900/5 p-4 border border-slate-900/5 mb-2">
        <p className="mb-2 text-xs font-bold text-slate-500 uppercase tracking-wider">Specifications:</p>
        <div className="space-y-1.5 text-[13px] text-[#94a3b8] italic leading-[1.5]">
          {lines.map((line, idx) => (
            <p key={idx}>• {line}</p>
          ))}
        </div>
      </div>
      
      <p className="mt-2 text-[12px] text-[#94a3b8]">
        Note: Interactive SVG/interactive visualization will be rendered here in the next iteration.
      </p>
    </div>
  )
}
