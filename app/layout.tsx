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
      <body className="font-sans min-h-screen flex flex-col bg-slate-50 text-slate-900 selection:bg-teal-500/10 selection:text-teal-900">
        <header className="sticky top-0 z-40 w-full border-b border-slate-200/60 bg-white/85 backdrop-blur-md">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 flex h-16 items-center justify-between">
            <div className="flex items-center gap-6">
              <a href="/" className="flex items-center gap-2.5 transition-opacity hover:opacity-90">
                <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-teal-600 text-white font-black text-lg tracking-wider shadow-sm shadow-teal-600/20">
                  CX
                </span>
                <div>
                  <span className="block text-sm font-bold text-slate-900 tracking-tight leading-none">CodeinteX</span>
                  <span className="block text-[10px] font-bold text-slate-400 uppercase tracking-widest mt-1">Learning</span>
                </div>
              </a>
            </div>
            
            <nav className="flex items-center gap-4">
              <a
                href="/courses/hcai-foundations"
                className="text-xs font-bold uppercase tracking-wider text-slate-600 hover:text-teal-600 transition-colors"
              >
                Mulai Belajar
              </a>
              <span className="h-4 w-px bg-slate-200" />
              <span className="rounded-full bg-teal-50/60 px-3 py-1 text-xs font-semibold text-teal-700 border border-teal-100">
                Phase 1: Local MD
              </span>
            </nav>
          </div>
        </header>

        <main className="flex-grow">
          {children}
        </main>

        <footer className="border-t border-slate-200/60 bg-white/50 py-8 text-center text-xs text-slate-400">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <p>© {new Date().getFullYear()} CodeinteX. Hak Cipta Dilindungi. Kursus gratis untuk peningkatan kompetensi AI.</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
