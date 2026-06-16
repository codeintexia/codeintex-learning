interface DiagramProps {
  title: string
  spec: string
}

export default function DiagramPlaceholder({ title, spec }: DiagramProps) {
  const lines = spec.split('\n').map(line => line.trim()).filter(Boolean);

  return (
    <div className="my-8 overflow-hidden rounded-xl border border-slate-200 bg-slate-50/30 p-6 shadow-sm backdrop-blur-sm transition-all duration-300 hover:border-slate-300">
      <div className="mb-4 flex items-center justify-between border-b border-slate-100 pb-3">
        <div className="flex items-center gap-2.5">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-teal-50 text-teal-600">
            <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <div>
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Interactive Blueprint</span>
            <h4 className="text-sm font-bold text-slate-800">{title}</h4>
          </div>
        </div>
        <span className="rounded-full bg-slate-100 px-2.5 py-1 text-[10px] font-medium text-slate-600 border border-slate-200/50">
          Coming Soon
        </span>
      </div>
      
      <div className="rounded-lg bg-slate-900/5 p-4 border border-slate-900/5">
        <p className="mb-2 text-xs font-bold text-slate-500 uppercase tracking-wider">Specifications:</p>
        <ul className="space-y-1.5">
          {lines.map((line, idx) => (
            <li key={idx} className="flex items-start gap-2 text-xs text-slate-600">
              <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-teal-500/80" />
              <span>{line}</span>
            </li>
          ))}
        </ul>
      </div>
      
      <p className="mt-3 text-center text-[10px] font-medium italic text-slate-400">
        Note: Interactive SVG/interactive visualization will be rendered here in the next iteration.
      </p>
    </div>
  )
}
