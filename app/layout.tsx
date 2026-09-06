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
      <body className="font-sans min-h-screen flex flex-col bg-[#ffffff] text-[#0A0E17]">
        <header className="sticky top-0 z-50 w-full bg-[#02040B] h-16 flex items-center">
          <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8 flex h-full items-center justify-between">
            <div className="flex items-center gap-8">
              <a href="/" className="flex items-center gap-2.5">
                <span className="flex h-8 w-8 items-center justify-center rounded-[4px] bg-[#02B3E4] text-[#02040B] font-black text-sm tracking-wider">
                  CX
                </span>
                <span className="text-white font-bold text-[15px] tracking-tight">CodeinteX</span>
              </a>
              <nav className="hidden md:flex items-center gap-6">
                <a href="/#programs" className="text-[13px] font-medium text-[#B5BAC6] hover:text-white transition-colors">Program</a>
                <a href="/#partners" className="text-[13px] font-medium text-[#B5BAC6] hover:text-white transition-colors">Untuk Bisnis</a>
              </nav>
            </div>

            <div className="flex items-center gap-4">
              <a href="#login" className="hidden sm:block text-[13px] font-medium text-[#B5BAC6] hover:text-white transition-colors">
                Masuk
              </a>
              <a
                href="/courses/hcai-foundations"
                className="inline-flex items-center justify-center rounded-[4px] bg-[#02B3E4] text-[#02040B] text-[13px] font-bold px-5 py-2.5 hover:bg-[#3ac4ec] transition-colors"
              >
                Mulai Belajar
              </a>
            </div>
          </div>
        </header>

        <main className="flex-grow">
          {children}
        </main>

        <footer className="bg-[#02040B] pt-16 pb-10 text-[#8890A0]">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 pb-12 border-b border-white/10">
              <div className="col-span-2 md:col-span-1">
                <span className="flex h-8 w-8 items-center justify-center rounded-[4px] bg-[#02B3E4] text-[#02040B] font-black text-sm mb-4">
                  CX
                </span>
                <p className="text-[13px] leading-relaxed max-w-[220px]">
                  Otomasi riset & rekayasa AI untuk profesional dan peneliti.
                </p>
              </div>
              <div>
                <h4 className="text-white text-[13px] font-semibold mb-3">Program</h4>
                <ul className="space-y-2 text-[13px]">
                  <li><a href="/courses/hcai-foundations" className="hover:text-white transition-colors">Human-Centered AI</a></li>
                  <li><a href="/#programs" className="hover:text-white transition-colors">Semua program</a></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white text-[13px] font-semibold mb-3">Perusahaan</h4>
                <ul className="space-y-2 text-[13px]">
                  <li><a href="/#partners" className="hover:text-white transition-colors">Untuk Bisnis</a></li>
                  <li><a href="#booking" className="hover:text-white transition-colors">Konsultasi</a></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white text-[13px] font-semibold mb-3">Kontak</h4>
                <ul className="space-y-2 text-[13px]">
                  <li><a href="mailto:hello@codeintex.com" className="hover:text-white transition-colors">hello@codeintex.com</a></li>
                </ul>
              </div>
            </div>
            <p className="text-[12px] pt-6">© 2026 CodeinteX. Seluruh hak cipta dilindungi.</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
