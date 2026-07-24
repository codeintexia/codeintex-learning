import ReactMarkdown from 'react-markdown'
import QuickCheck from './QuickCheck'
import DiagramPlaceholder from './DiagramRenderer'

interface LessonRendererProps {
  content: string
}

interface QuickCheckItem {
  question: string
  answer?: string
}

export default function LessonRenderer({ content }: LessonRendererProps) {
  // Suppress/remove the first H1 element (the lesson title) to fix the double title bug
  // This matches the first line starting with '# ' and strips it along with its trailing newline.
  const contentWithoutFirstH1 = content.replace(/^#\s+.+\n?/m, '').trimStart();

  const quickChecks: QuickCheckItem[] = []

  // 1. Matches HTML details format in Kursus 2: ## Quick Check ... **Question** ... <details><summary>...</summary> Answer </details>
  const detailsQcRegex = /## Quick Check[\s\S]*?\n\n\*\*([^\*]+?)\*\*[\s\S]*?<details>[\s\S]*?<summary>[^<]*<\/summary>([\s\S]*?)<\/details>/gi;
  let processedContent = contentWithoutFirstH1.replace(detailsQcRegex, (match: string, qGroup: string, aGroup: string) => {
    const index = quickChecks.length
    quickChecks.push({
      question: qGroup.trim(),
      answer: aGroup.trim(),
    })
    return `__QUICK_CHECK_${index}__`
  })

  // 2. Matches blockquotes starting with > **Quick Check** — Sebelum melanjutkan... (HCAI format)
  const qcRegex = /> \*\*Quick Check\*\* — Sebelum melanjutkan[^\n]*\r?\n((?:> [^\n]*\r?\n?)+)/g;
  processedContent = processedContent.replace(qcRegex, (match: string, qGroup: string) => {
    const questionText = qGroup
      .split('\n')
      .map((line: string) => line.replace(/^>\s*/, '').trim())
      .join(' ')
      .replace(/^\*|\*$/g, '')
      .trim();
    const index = quickChecks.length
    quickChecks.push({ question: questionText })
    return `__QUICK_CHECK_${index}__`
  })

  // 3. Matches diagram HTML comments <!-- DIAGRAM: [Title] \n [spec] --> or <!-- VISUAL PLACEHOLDER: [spec] -->
  const diagrams: { title: string; spec: string }[] = []
  const diagramRegex = /<!--\s*(DIAGRAM|VISUAL PLACEHOLDER):\s*([\s\S]*?)-->/gi;
  processedContent = processedContent.replace(diagramRegex, (match: string, typeGroup: string, bodyGroup: string) => {
    let title = "Visual Blueprint"
    let spec = bodyGroup.trim()

    if (typeGroup.toUpperCase() === 'DIAGRAM') {
      const lines = bodyGroup.trim().split(/\r?\n/)
      title = lines[0]?.trim() || "Diagram Blueprint"
      spec = lines.slice(1).join('\n').trim() || spec
    }

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
          <QuickCheck
            key={`qc-${index}`}
            question={quickChecks[index].question}
            answer={quickChecks[index].answer}
          />
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
            className="prose prose-teal max-w-none"
          >
            {part}
          </ReactMarkdown>
        )
      }
      i++
    }
  }

  return (
    <div className="space-y-6 max-w-[68ch]">
      {elements}
    </div>
  )
}
