import ReactMarkdown from 'react-markdown'
import QuickCheck from './QuickCheck'
import DiagramPlaceholder from './DiagramRenderer'

interface LessonRendererProps {
  content: string
}

export default function LessonRenderer({ content }: LessonRendererProps) {
  // Suppress/remove the first H1 element (the lesson title) to fix the double title bug
  const contentWithoutFirstH1 = content.replace(/^#\s+[^\r\n]*\r?\n?/m, '');

  // Regex patterns
  // 1. Matches blockquotes starting with > **Quick Check** — Sebelum melanjutkan...
  // Captures all consecutive lines that start with ">"
  const qcRegex = /> \*\*Quick Check\*\* — Sebelum melanjutkan[^\n]*\r?\n((?:> [^\n]*\r?\n?)+)/g;
  
  // 2. Matches diagram HTML comments <!-- DIAGRAM: [Title] \n [spec] -->
  const diagramRegex = /<!-- DIAGRAM:\s*([^\r\n]*)\r?\n([\s\S]*?)-->/g;

  // Extract all Quick Checks
  const quickChecks: string[] = []
  let processedContent = contentWithoutFirstH1.replace(qcRegex, (match, qGroup) => {
    const questionText = qGroup
      .split('\n')
      .map((line: string) => line.replace(/^>\s*/, '').trim())
      .join(' ')
      .replace(/^\*|\*$/g, '')
      .trim();
    const index = quickChecks.length
    quickChecks.push(questionText)
    return `__QUICK_CHECK_${index}__`
  })

  // Extract all Diagrams
  const diagrams: { title: string; spec: string }[] = []
  processedContent = processedContent.replace(diagramRegex, (match, titleGroup, specGroup) => {
    const title = titleGroup.trim()
    const spec = specGroup.trim()
    const index = diagrams.length
    diagrams.push({ title, spec })
    return `__DIAGRAM_${index}__`
  })

  // Split content by placeholders
  const placeholderRegex = /__(QUICK_CHECK|DIAGRAM)_(\d+)__/g
  const parts = processedContent.split(placeholderRegex)

  const elements: React.ReactNode[] = []

  let i = 0
  while (i < parts.length) {
    const part = parts[i]
    if (part === undefined || part === null) {
      i++
      continue
    }

    if (part === 'QUICK_CHECK') {
      const index = parseInt(parts[i + 1], 10)
      if (!isNaN(index) && quickChecks[index] !== undefined) {
        elements.push(
          <QuickCheck key={`qc-${index}`} question={quickChecks[index]} />
        )
      }
      i += 2
    } else if (part === 'DIAGRAM') {
      const index = parseInt(parts[i + 1], 10)
      if (!isNaN(index) && diagrams[index] !== undefined) {
        elements.push(
          <DiagramPlaceholder
            key={`diag-${index}`}
            title={diagrams[index].title}
            spec={diagrams[index].spec}
          />
        )
      }
      i += 2
    } else {
      if (part.trim()) {
        elements.push(
          <ReactMarkdown
            key={`md-${i}`}
            className="prose prose-teal max-w-none text-[18px] leading-[1.85] text-[#1a1a2e] prose-p:text-[18px] prose-p:leading-[1.85] prose-p:mb-[1.75rem] prose-p:mt-0 prose-p:text-[#1a1a2e] prose-headings:text-[#1a1a2e] prose-blockquote:text-[#1a1a2e] prose-li:text-[18px] prose-li:leading-[1.85] prose-li:text-[#1a1a2e] prose-blockquote:border-teal-500 prose-blockquote:bg-slate-50/50 prose-blockquote:py-1 prose-blockquote:px-4 prose-blockquote:rounded-r-lg"
          >
            {part}
          </ReactMarkdown>
        )
      }
      i++
    }
  }

  return (
    <div className="space-y-6 max-w-[68ch] text-[18px] leading-[1.85] text-[#1a1a2e]">
      {elements}
    </div>
  )
}
