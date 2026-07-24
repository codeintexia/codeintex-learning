import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export const metadata: Metadata = {
  title: 'CodeinteX Learning Platform',
  description: 'Platform kursus online terdepan untuk Human-Centered AI dan rekayasa teknologi modern.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="id" className={`${inter.variable} scroll-smooth`}>
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
      </head>
      <body className="font-sans min-h-screen flex flex-col bg-[#ffffff] text-[#0f172a] selection:bg-teal-500/10 selection:text-teal-900">
        <header className="sticky top-0 z-50 w-full border-b border-[#e2e8f0] bg-[#ffffff] h-16 flex items-center">
          <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8 flex h-full items-center justify-between">
            <div className="flex items-center gap-6">
              <a href="/" className="flex items-center gap-2.5 transition-opacity hover:opacity-90">
                <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#1e3a8a] text-white font-black text-lg tracking-wider shadow-sm shadow-[#1e3a8a]/20">
                  CX
                </span>
                <div>
                  <span className="block text-sm font-bold text-[#0f172a] tracking-tight leading-none">CodeinteX</span>
                  <span className="block text-[10px] font-bold text-[#475569] uppercase tracking-widest mt-1">Learning</span>
                </div>
              </a>
            </div>
            
            <nav className="flex items-center gap-6">
              <a
                href="/courses/hcai-foundations"
                className="text-sm font-medium text-[#475569] hover:text-[#0f172a] transition-colors duration-150"
              >
                Kursus
              </a>
              <a
                href="/courses/hcai-foundations"
                className="inline-flex items-center justify-center rounded-[6px] bg-[#1e3a8a] text-white text-xs font-semibold px-4 py-2 hover:bg-[#1e3a8a]/90 active:scale-[0.98] transition-all duration-150 hover:scale-[1.01]"
              >
                Mulai Belajar
              </a>
            </nav>
          </div>
        </header>

        <main className="flex-grow">
          {children}
        </main>

        <footer className="border-t border-[#e2e8f0] bg-[#f8fafc] py-8 text-center text-[13px] text-[#64748b]">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
            {/* Attribution copyright line updated to institutional trust styling (FIX 6) */}
            <p>© 2026 CodeinteX. Kursus ini diproduksi sebagai bagian dari inisiatif pendidikan AI CodeinteX.</p>
            <div className="flex gap-4">
              <a href="/courses/hcai-foundations" className="text-[#64748b] hover:text-[#0f172a] transition-colors duration-150">Kursus</a>
              <a href="/" className="text-[#64748b] hover:text-[#0f172a] transition-colors duration-150">Beranda</a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  )
}
