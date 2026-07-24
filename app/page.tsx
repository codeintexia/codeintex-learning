"use client"

import { useState } from 'react'
import Link from 'next/link'

// Course catalog database (FIX 1 & 4)
const courses = [
  {
    id: 1,
    title: "Human-Centered AI — Foundations",
    category: "literacy",
    categoryLabel: "Literacy",
    description: "Merancang sistem AI yang benar-benar bekerja untuk manusia.",
    duration: "6 Jam",
    lessons: "25 Lesson",
    modules: "6 Modul",
    domain: "AI & Kecerdasan Buatan",
    isLive: true,
    href: "/courses/hcai-foundations",
    statusText: "Tersedia Sekarang",
  },
  {
    id: 2,
    title: "AI untuk Proses Data",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia.",
    domain: "AI & Kecerdasan Buatan",
    isLive: false,
    statusText: "Dalam Pengembangan",
  },
  {
    id: 3,
    title: "AI untuk Pengalaman Pelanggan",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia.",
    domain: "AI & Kecerdasan Buatan",
    isLive: false,
    statusText: "Dalam Pengembangan",
  },
  {
    id: 4,
    title: "AI untuk Keamanan Informasi",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia.",
    domain: "AI & Kecerdasan Buatan",
    isLive: false,
    statusText: "Dalam Pengembangan",
  },
  {
    id: 5,
    title: "AI untuk Strategi Metode Pembelajaran",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia.",
    domain: "AI & Kecerdasan Buatan",
    isLive: false,
    statusText: "Dalam Pengembangan",
  },
  {
    id: 6,
    title: "AI untuk Pengelolaan Pelanggan",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia.",
    domain: "AI & Kecerdasan Buatan",
    isLive: false,
    statusText: "Dalam Pengembangan",
  }
]

// Tab buttons metadata (FIX 1)
const tabs = [
  { id: 'all', label: 'Semua', subtitle: 'Semua jalur pembelajaran' },
  { id: 'literacy', label: 'Literacy', subtitle: 'Pemahaman konsep dan lanskap AI' },
  { id: 'competency', label: 'Competency', subtitle: 'Kemampuan terverifikasi dan tersertifikasi' },
  { id: 'specialization', label: 'Specialization', subtitle: 'Keahlian mendalam di domain spesifik' },
]

export default function HomePage() {
  const [activeTab, setActiveTab] = useState('all')

  // Filter courses based on active tab selection (FIX 5)
  const filteredCourses = courses.filter((course) => {
    if (activeTab === 'all') return true
    return course.category === activeTab
  })

  return (
    <div className="flex flex-col items-stretch bg-[#ffffff]">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-[#ffffff] border-b border-[#e2e8f0]">
        <div className="mx-auto max-w-[1200px] px-[40px] py-[80px] pb-[72px] grid grid-cols-1 md:grid-cols-2 gap-[80px] items-center bg-[#ffffff]">
          
          {/* Left column: platform messaging */}
          <div>
            {/* Pill badge (FIX 5) */}
            <span className="inline-block bg-[#f0fdfa] text-[#0d9488] border border-[#99f6e4] text-[12px] font-medium px-[14px] py-[4px] rounded-full mb-6">
              ✦ Kursus Baru &middot; Gratis &amp; Terbuka
            </span>
            
            {/* Heading H1 (FIX 3) */}
            <h1 className="text-[32px] md:text-[38px] font-bold tracking-tight text-[#0f172a] leading-[1.15] mb-5">
              Kuasai AI yang <br />
              Berpusat pada Manusia
            </h1>
            
            {/* Subheading */}
            <p className="text-[17px] text-[#475569] leading-[1.7] max-w-[480px] mb-8">
              Kursus berbasis penelitian akademis untuk profesional yang ingin merancang, mengevaluasi, dan mengaudit sistem AI secara bertanggung jawab.
            </p>
            
            {/* Three proof points (FIX 1) */}
            <div style={{ display: 'flex', flexDirection: 'row', flexWrap: 'wrap', gap: '16px', alignItems: 'center', marginBottom: '28px' }}>
              <span className="flex items-center gap-1.5 text-[13px] text-[#64748b] font-medium">
                ✓ Referensi akademis terverifikasi
              </span>
              <span className="flex items-center gap-1.5 text-[13px] text-[#64748b] font-medium">
                ✓ Metodologi IFRAME eksklusif
              </span>
              <span className="flex items-center gap-1.5 text-[13px] text-[#64748b] font-medium">
                ✓ 100% gratis &amp; terbuka
              </span>
            </div>
            
            {/* CTA Buttons */}
            <div className="flex flex-wrap items-center gap-3">
              <Link
                href="/courses/hcai-foundations"
                className="inline-flex items-center justify-center rounded-[8px] bg-[#1e3a8a] text-white px-[24px] py-[12px] text-[15px] font-semibold transition-colors duration-150 hover:bg-[#1e40af]"
              >
                Mulai Belajar — Gratis
              </Link>
              <button
                onClick={() => document.getElementById('katalog')?.scrollIntoView({ behavior: 'smooth' })}
                className="inline-flex items-center justify-center rounded-[8px] border-[1.5px] border-[#1e3a8a] bg-transparent text-[#1e3a8a] px-[24px] py-[12px] text-[15px] font-semibold cursor-pointer transition-colors duration-150 hover:bg-[#f8fafc]"
              >
                Lihat Semua Kursus
              </button>
            </div>
          </div>
          
          {/* Right column: stacked course cards visual (hidden on mobile < 768px) (FIX 2) */}
          <div className="hidden md:block" style={{ width: '100%' }}>
            <div style={{ position: 'relative', height: '300px', width: '100%' }}>
              
              {/* Card 3: back */}
              <div style={{
                position: 'absolute',
                top: '28px',
                left: '16px',
                right: '-8px',
                height: '200px',
                background: '#e2e8f0',
                borderRadius: '12px',
                transform: 'rotate(3deg)',
                opacity: 0.45,
                zIndex: 1,
              }}></div>

              {/* Card 2: middle */}
              <div style={{
                position: 'absolute',
                top: '14px',
                left: '8px',
                right: '-4px',
                height: '210px',
                background: '#f1f5f9',
                border: '1px solid #e2e8f0',
                borderRadius: '12px',
                transform: 'rotate(1.5deg)',
                opacity: 0.7,
                zIndex: 2,
              }}></div>

              {/* Card 1: front — keep existing card content here */}
              <div style={{
                position: 'absolute',
                top: 0,
                left: 0,
                right: 0,
                zIndex: 3,
                background: 'white',
                border: '1px solid #e2e8f0',
                borderRadius: '12px',
                boxShadow: '0 8px 32px rgba(0,0,0,0.12)',
                overflow: 'hidden',
              }}>
                {/* Top teal bar */}
                <div 
                  className="h-[4px] w-full"
                  style={{
                    background: 'linear-gradient(90deg, #0d9488, #14b8a6)',
                    borderRadius: '12px 12px 0 0'
                  }}
                />
                
                {/* Card content padding container */}
                <div style={{ padding: '20px' }}>
                  {/* Category badge */}
                  <span className="inline-block bg-[#f0fdfa] text-[#0d9488] text-[10px] font-bold tracking-[0.08em] uppercase py-[2px] px-[8px] rounded-full mb-2">
                    Literacy
                  </span>
                  
                  {/* Course title */}
                  <h4 className="text-[14px] font-bold text-[#0f172a] mb-2 leading-tight">
                    Human-Centered AI — Foundations
                  </h4>
                  
                  {/* Metadata row */}
                  <div className="text-[12px] text-[#94a3b8] mb-3 font-medium">
                    6 Modul &middot; 25 Lesson &middot; 6 Jam
                  </div>
                  
                  {/* Three lesson preview items */}
                  <div className="space-y-1.5">
                    {/* Item 1 */}
                    <div className="flex items-center gap-2">
                      <span className="w-[18px] h-[18px] rounded-full bg-[#f0fdfa] text-[#0d9488] border border-[#99f6e4] text-[10px] font-bold flex items-center justify-center shrink-0">
                        1
                      </span>
                      <span className="text-[12px] text-[#475569] leading-[1.3] truncate">
                        Ketika AI Gagal Bukan Karena Bodoh...
                      </span>
                    </div>
                    
                    {/* Item 2 */}
                    <div className="flex items-center gap-2 opacity-60">
                      <span className="w-[18px] h-[18px] rounded-full bg-[#f0fdfa] text-[#0d9488] border border-[#99f6e4] text-[10px] font-bold flex items-center justify-center shrink-0">
                        2
                      </span>
                      <span className="text-[12px] text-[#475569] leading-[1.3] truncate">
                        Dari AI-Centered ke Human-Centered...
                      </span>
                    </div>
                    
                    {/* Item 3 */}
                    <div className="flex items-center gap-2 opacity-40">
                      <span className="w-[18px] h-[18px] rounded-full bg-[#f0fdfa] text-[#0d9488] border border-[#99f6e4] text-[10px] font-bold flex items-center justify-center shrink-0">
                        3
                      </span>
                      <span className="text-[12px] text-[#475569] leading-[1.3] truncate">
                        Dua Sumbu Shneiderman...
                      </span>
                    </div>
                  </div>
                  
                  {/* Status badge at bottom */}
                  <div className="mt-3">
                    <span className="inline-block bg-[#f0fdfa] text-[#0d9488] text-[11px] font-semibold px-[10px] py-[3px] rounded-full">
                      Tersedia Sekarang
                    </span>
                  </div>
                </div>
              </div>

              {/* Label below */}
              <div style={{
                position: 'absolute',
                bottom: '-24px',
                left: 0,
                right: 0,
                textAlign: 'center',
                fontSize: '12px',
                color: '#94a3b8',
              }}>6 kursus tersedia &middot; 5 dalam pengembangan</div>
            </div>
          </div>
          
        </div>
      </section>

      {/* Stats Section */}
      <section className="border-t border-b border-[#e2e8f0] bg-[#f8fafc] py-[40px]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div className="p-4">
              <span className="block text-[32px] font-bold text-[#1e3a8a]">6</span>
              <span className="text-[12px] font-semibold uppercase tracking-[0.08em] text-[#64748b] mt-1 block">Modul Pembelajaran</span>
            </div>
            <div className="p-4">
              <span className="block text-[32px] font-bold text-[#1e3a8a]">25</span>
              <span className="text-[12px] font-semibold uppercase tracking-[0.08em] text-[#64748b] mt-1 block">Lesson Interaktif</span>
            </div>
            <div className="p-4">
              <span className="block text-[32px] font-bold text-[#1e3a8a]">6 Jam</span>
              <span className="text-[12px] font-semibold uppercase tracking-[0.08em] text-[#64748b] mt-1 block">Estimasi Waktu Belajar</span>
            </div>
            <div className="p-4">
              <span className="block text-[32px] font-bold text-[#1e3a8a]">100%</span>
              <span className="text-[12px] font-semibold uppercase tracking-[0.08em] text-[#64748b] mt-1 block">Gratis & Terbuka</span>
            </div>
          </div>
        </div>
      </section>

      {/* Learning Outcomes Section */}
      <section className="bg-[#f8fafc] py-[64px] border-b border-[#e2e8f0]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-10">
            <span className="text-[11px] font-bold uppercase tracking-[0.1em] text-[#0d9488] mb-3 block">
              LEARNING OUTCOMES
            </span>
            <h2 className="text-[28px] font-bold text-[#0f172a] text-center">
              Yang akan kamu kuasai
            </h2>
          </div>
          
          {/* Grid list of outcome items */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
            {/* Outcome Card 1 - hover: translateY(-2px), shadow, 200ms duration (FIX 4) */}
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none transition-all duration-200 ease-in-out hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]">
              <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488] mt-0.5">
                ✓
              </span>
              <div>
                <h4 className="text-[15px] font-semibold text-[#0f172a] mb-1">
                  Evaluasi sistem AI
                </h4>
                <p className="text-[14px] leading-[1.5] text-[#64748b]">
                  Menggunakan kerangka 4 prinsip HCAI untuk menilai kualitas interaksi AI.
                </p>
              </div>
            </div>
            
            {/* Outcome Card 2 */}
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none transition-all duration-200 ease-in-out hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]">
              <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488] mt-0.5">
                ✓
              </span>
              <div>
                <h4 className="text-[15px] font-semibold text-[#0f172a] mb-1">
                  Desain dengan IFRAME
                </h4>
                <p className="text-[14px] leading-[1.5] text-[#64748b]">
                  Mengadopsi metodologi eksklusif CodeinteX dalam merancang antarmuka AI.
                </p>
              </div>
            </div>
            
            {/* Outcome Card 3 */}
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none transition-all duration-200 ease-in-out hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]">
              <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488] mt-0.5">
                ✓
              </span>
              <div>
                <h4 className="text-[15px] font-semibold text-[#0f172a] mb-1">
                  Deteksi dan tangani bias
                </h4>
                <p className="text-[14px] leading-[1.5] text-[#64748b]">
                  Memahami bias data dan algoritma dalam konteks sosial-budaya Asia Tenggara.
                </p>
              </div>
            </div>
            
            {/* Outcome Card 4 */}
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none transition-all duration-200 ease-in-out hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]">
              <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488] mt-0.5">
                ✓
              </span>
              <div>
                <h4 className="text-[15px] font-semibold text-[#0f172a] mb-1">
                  Audit produk AI nyata
                </h4>
                <p className="text-[14px] leading-[1.5] text-[#64748b]">
                  Menggunakan checklist audit praktis yang bisa langsung diimplementasikan pada produk Anda.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Institutional Trust Block Section (FIX 5) */}
      <section className="bg-white py-[20px]">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <div className="bg-[#f8fafc] border border-[#e2e8f0] rounded-[12px] p-6 md:p-[32px_40px] flex flex-col md:flex-row items-center gap-6 md:gap-[40px] my-10 shadow-none">
            {/* Left side — CodeinteX logo mark */}
            <div className="flex-shrink-0 bg-white border border-[#e2e8f0] rounded-[10px] p-[10px] flex items-center justify-center w-[68px] h-[68px]">
              <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-[#1e3a8a] text-white font-black text-xl tracking-wider">
                CX
              </span>
            </div>
            
            {/* Right side — texts and institutional badges */}
            <div className="flex-grow text-center md:text-left">
              <span className="block text-[11px] font-bold uppercase tracking-[0.1em] text-[#0d9488] mb-[6px]">
                TENTANG KURSUS INI
              </span>
              <h3 className="text-[17px] font-bold text-[#0f172a] mb-[8px]">
                Dikembangkan oleh CodeinteX
              </h3>
              <p className="text-[14px] leading-[1.6] text-[#64748b] mb-[16px]">
                Kursus ini dirancang dan diproduksi oleh CodeinteX — sebuah firma pengetahuan dan rekayasa yang berfokus pada sistem AI yang berpusat pada manusia dan dapat dijelaskan. Seluruh konten berbasis penelitian akademis terverifikasi dan metodologi IFRAME eksklusif CodeinteX.
              </p>
              
              {/* Badges row */}
              <div className="flex flex-wrap justify-center md:justify-start gap-2">
                <span className="bg-white border border-[#e2e8f0] text-[#475569] text-[12px] py-[4px] px-[12px] rounded-full font-medium">
                  📚 Referensi akademis terverifikasi
                </span>
                <span className="bg-[#ffffff] border border-[#e2e8f0] text-[#475569] text-[12px] py-[4px] px-[12px] rounded-full font-medium">
                  ⚙️ Metodologi IFRAME eksklusif
                </span>
                <span className="bg-[#ffffff] border border-[#e2e8f0] text-[#475569] text-[12px] py-[4px] px-[12px] rounded-full font-medium">
                  ✓ 100% gratis &amp; terbuka
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Multi-Course Grid Catalog Section (replaces old curriculum modules layout) */}
      <section id="katalog" className="py-20 bg-[#ffffff] border-t border-[#e2e8f0]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          
          {/* COMPONENT 1 — Category Navigation Tabs */}
          <div className="text-center mb-[40px]">
            <span className="text-[11px] font-bold uppercase tracking-[0.1em] text-[#0d9488] mb-[16px] block">
              JALUR PEMBELAJARAN
            </span>
            <h2 className="text-3xl font-extrabold tracking-tight sm:text-4xl text-[#0f172a] mb-[24px]">
              Pilih jalur yang sesuai dengan tujuanmu
            </h2>
            
            {/* Tabs container */}
            <div className="inline-flex flex-wrap justify-center bg-[#f1f5f9] rounded-[12px] p-[4px] gap-[4px] mb-[48px] max-w-full">
              {tabs.map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex flex-col items-center justify-center text-center px-[24px] py-[10px] rounded-[8px] cursor-pointer transition-all duration-150 ease-in-out select-none min-w-[150px] ${
                    activeTab === tab.id
                      ? 'bg-white text-[#0f172a] font-semibold shadow-[0_1px_4px_rgba(0,0,0,0.1)]'
                      : 'bg-transparent text-[#64748b] font-medium hover:text-[#0f172a]'
                  }`}
                >
                  <span className="text-[14px] leading-tight block">{tab.label}</span>
                  <span className={`text-[11px] font-normal mt-0.5 block leading-tight ${
                    activeTab === tab.id ? 'text-[#94a3b8]' : 'text-[#a3b1c2]'
                  }`}>
                    {tab.subtitle}
                  </span>
                </button>
              ))}
            </div>
          </div>

          {/* COMPONENT 2 — Course Grid & COMPONENT 5 — Tab filtering behavior */}
          {activeTab === 'specialization' ? (
            <div className="py-16 text-center max-w-md mx-auto">
              {/* Specialization pending feedback statement */}
              <p className="text-[#64748b] text-[15px] font-medium leading-relaxed">
                Jalur Spesialisasi sedang dalam pengembangan. <br />
                Tersedia setelah kamu menyelesaikan jalur Competency.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-[24px] pb-[64px]">
              {filteredCourses.map((course) => {
                if (course.isLive) {
                  // COMPONENT 3 — Course Card (Live)
                  return (
                    <Link
                      key={course.id}
                      href={course.href || '#'}
                      className="group relative flex flex-col justify-between overflow-hidden rounded-[12px] border border-[#e2e8f0] bg-white transition-all duration-200 ease-in-out hover:border-[#0d9488] hover:shadow-[0_8px_24px_rgba(0,0,0,0.1)] hover:-translate-y-[3px]"
                    >
                      {/* Top color bar */}
                      <div 
                        className="h-[4px] w-full"
                        style={{ background: 'linear-gradient(90deg, #0d9488, #14b8a6)' }}
                      />
                      
                      {/* Card body */}
                      <div className="p-[20px] flex-grow flex flex-col justify-between">
                        <div>
                          {/* Category badge */}
                          <span className="inline-block bg-[#f0fdfa] text-[#0d9488] text-[10px] font-bold tracking-[0.08em] uppercase py-[2px] px-[8px] rounded-full mb-3">
                            {course.categoryLabel}
                          </span>
                          
                          {/* Course title */}
                          <h4 className="text-[16px] font-bold text-[#0f172a] mb-2 leading-[1.3] transition-colors duration-150 group-hover:text-[#0d9488]">
                            {course.title}
                          </h4>
                          
                          {/* Description */}
                          <p className="text-[13px] leading-[1.5] text-[#64748b] mb-4">
                            {course.description}
                          </p>
                          
                          {/* Metadata row */}
                          <div className="flex flex-wrap gap-[12px] mb-4">
                            <span className="text-[12px] text-[#94a3b8] flex items-center gap-1 font-medium">
                              📂 {course.modules}
                            </span>
                            <span className="text-[12px] text-[#94a3b8] flex items-center gap-1 font-medium">
                              📖 {course.lessons}
                            </span>
                            <span className="text-[12px] text-[#94a3b8] flex items-center gap-1 font-medium">
                              ⏱ {course.duration}
                            </span>
                          </div>
                        </div>

                        <div>
                          {/* Domain tag */}
                          <span className="inline-block bg-[#f8fafc] border border-[#e2e8f0] text-[#64748b] text-[11px] py-[2px] px-[8px] rounded-[4px] mb-4 font-medium">
                            {course.domain}
                          </span>
                          
                          {/* Card footer */}
                          <div className="flex items-center justify-between pt-4 border-t border-[#f1f5f9]">
                            <span className="bg-[#f0fdfa] text-[#0d9488] text-[11px] font-semibold py-[3px] px-[10px] rounded-full">
                              {course.statusText}
                            </span>
                            <span className="text-[#0d9488] text-[13px] font-semibold flex items-center gap-0.5">
                              Mulai Belajar <span className="transition-transform duration-150 group-hover:translate-x-1">→</span>
                            </span>
                          </div>
                        </div>
                      </div>
                    </Link>
                  )
                } else {
                  // COMPONENT 4 — Course Card (Placeholder)
                  return (
                    <div
                      key={course.id}
                      className="group relative flex flex-col justify-between overflow-hidden rounded-[12px] border border-[#e2e8f0] bg-[#fafafa] opacity-85 transition-all duration-200 ease-in-out"
                    >
                      {/* Top grey color bar */}
                      <div className="h-[4px] w-full bg-[#e2e8f0]" />
                      
                      {/* Card body */}
                      <div className="p-[20px] flex-grow flex flex-col justify-between">
                        <div>
                          {/* Category badge */}
                          <span className="inline-block bg-[#f1f5f9] text-[#94a3b8] text-[10px] font-bold tracking-[0.08em] uppercase py-[2px] px-[8px] rounded-full mb-3">
                            {course.categoryLabel}
                          </span>
                          
                          {/* Course title */}
                          <h4 className="text-[16px] font-bold text-[#334155] mb-2 leading-[1.3]">
                            {course.title}
                          </h4>
                          
                          {/* Description */}
                          <p className="text-[13px] leading-[1.5] text-[#94a3b8] mb-4">
                            {course.description}
                          </p>
                        </div>

                        <div>
                          {/* Domain tag */}
                          <span className="inline-block bg-[#f8fafc] border border-[#e2e8f0] text-[#64748b] text-[11px] py-[2px] px-[8px] rounded-[4px] mb-4 font-medium">
                            {course.domain}
                          </span>
                          
                          {/* Card footer */}
                          <div className="flex items-center justify-between pt-4 border-t border-[#f1f5f9]">
                            <span className="bg-[#fef9c3] text-[#854d0e] text-[11px] font-semibold py-[3px] px-[10px] rounded-full">
                              {course.statusText}
                            </span>
                            <span className="text-[#94a3b8] text-[13px] font-semibold">
                              Segera Hadir
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                  )
                }
              })}
            </div>
          )}

        </div>
      </section>
    </div>
  )
}
