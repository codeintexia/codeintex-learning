import Link from 'next/link'
import courseData from '@/content/courses/hcai-foundations/_course.json'

export default function HomePage() {
  return (
    <div className="flex flex-col items-stretch bg-[#ffffff]">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-[#ffffff] py-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative z-10">
          {/* Two-column grid layout to balance text and floating visual elements (FIX 1) */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-[64px] items-center">
            
            {/* Left column: course highlights and CTA links */}
            <div className="lg:col-span-7">
              <span className="inline-flex items-center gap-1.5 rounded-full bg-[#f0fdfa] px-[12px] py-[4px] text-[12px] font-semibold text-[#0d9488] border border-[#99f6e4] mb-6">
                <span className="h-1.5 w-1.5 rounded-full bg-[#0d9488] animate-pulse" />
                Kursus Baru Dirilis
              </span>
              <h1 className="text-[48px] font-bold tracking-tight text-[#0f172a] leading-[1.15] mb-6">
                Human-Centered AI <br />
                <span className="text-[#0d9488]">
                  — Foundations
                </span>
              </h1>
              <p className="text-[18px] text-[#475569] leading-[1.7] max-w-[560px] mb-8">
                {courseData.subtitle}. Kuasai dasar merancang sistem kecerdasan buatan yang transparan, adil, aman, dan berdaya guna tinggi bagi penggunanya.
              </p>
              <div className="flex flex-wrap items-center gap-4">
                <Link
                  href="/courses/hcai-foundations"
                  className="inline-flex items-center justify-center rounded-[6px] bg-[#1e3a8a] px-[24px] py-[12px] text-sm font-semibold text-white transition-all duration-200 hover:bg-[#1e3a8a]/90 active:scale-95"
                >
                  Mulai Belajar Sekarang (Gratis) →
                </Link>
                <a
                  href="#kurikulum"
                  className="inline-flex items-center justify-center rounded-[6px] border-[1.5px] border-[#1e3a8a] bg-transparent px-[24px] py-[12px] text-sm font-semibold text-[#1e3a8a] transition-all duration-200 hover:bg-[#f8fafc] active:scale-95"
                >
                  Lihat Kurikulum
                </a>
              </div>
            </div>
            
            {/* Right column: floating stylized course preview card (FIX 1) */}
            <div className="lg:col-span-5 flex justify-center lg:justify-end">
              <div 
                className="bg-white border border-[#e2e8f0] rounded-[16px] shadow-[0_8px_32px_rgba(0,0,0,0.12)] w-full max-w-[340px] transition-transform duration-300 hover:scale-[1.02] overflow-hidden relative"
                style={{ transform: 'rotate(1.5deg)' }}
              >
                {/* Premium gradient stripe at the top (FIX 3) */}
                <div 
                  className="h-[4px] w-full"
                  style={{
                    background: 'linear-gradient(90deg, #0d9488, #14b8a6)',
                    borderRadius: '16px 16px 0 0'
                  }}
                />
                
                {/* Visual card content padding container (FIX 3) */}
                <div className="p-[24px]">
                  {/* Visual card category tag */}
                  <div className="text-[11px] font-bold text-[#0d9488] uppercase tracking-wider mb-2">
                    Human-Centered AI
                  </div>
                  {/* Course outline title */}
                  <h4 className="text-[16px] font-bold text-[#0f172a] mb-4">
                    HCAI Foundations
                  </h4>
                  
                  {/* Progress bar showing 0% progress initially */}
                  <div className="w-full bg-[#f1f5f9] h-[4px] rounded-full overflow-hidden mb-2">
                    <div className="bg-[#0d9488] h-full" style={{ width: '0%' }} />
                  </div>
                  
                  {/* Lesson metric label */}
                  <div className="text-[12px] text-[#94a3b8] mb-6 font-medium">
                    6 Modul &middot; 25 Lesson &middot; 6 Jam
                  </div>
                  
                  {/* Previews of the first three lessons */}
                  <div className="space-y-4">
                    {/* Lesson 1 info block */}
                    <div className="flex items-start gap-3">
                      <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488]">
                        1
                      </span>
                      <span className="text-[13px] text-[#475569] font-medium leading-tight">
                        Ketika AI Gagal Bukan Karena Bodoh...
                      </span>
                    </div>
                    
                    {/* Lesson 2 info block - Dimmed overlay */}
                    <div className="flex items-start gap-3 opacity-60">
                      <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488]">
                        2
                      </span>
                      <span className="text-[13px] text-[#475569] font-medium leading-tight">
                        Dari AI-Centered ke Human-Centered...
                      </span>
                    </div>
                    
                    {/* Lesson 3 info block - Dimmed overlay */}
                    <div className="flex items-start gap-3 opacity-30">
                      <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#f0fdfa] border border-[#99f6e4] text-[10px] font-bold text-[#0d9488]">
                        3
                      </span>
                      <span className="text-[13px] text-[#475569] font-medium leading-tight">
                        Dua Sumbu Shneiderman...
                      </span>
                    </div>
                  </div>
                </div>
              </div>
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

      {/* Learning Outcomes Section (FIX 2) */}
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
            {/* Outcome Card 1 */}
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none">
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
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none">
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
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none">
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
            <div className="bg-white border border-[#e2e8f0] rounded-[8px] p-[20px_24px] flex items-start gap-3 shadow-none">
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

      {/* Curriculum Overview */}
      <section id="kurikulum" className="py-20 bg-[#ffffff]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.1em] text-[#0d9488] mb-3">STRUKTUR PEMBELAJARAN</h2>
            <h3 className="text-3xl font-extrabold tracking-tight sm:text-4xl text-[#0f172a] mb-4">
              Kurikulum Human-Centered AI
            </h3>
            <p className="text-[#475569] text-sm sm:text-base leading-relaxed">
              Dirancang secara sistematis dari pemahaman filosofis hingga evaluasi praktis. Setiap modul dilengkapi dengan lesson komprehensif, analisis kasus nyata, dan refleksi mandiri.
            </p>
          </div>

          {/* Upgraded grid showing premium cards that are fully clickable (FIX 3) */}
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {courseData.modules.map((module) => {
              // Determine Bloom's level gray pill tag text based on module numbers
              let bloomLevel = '';
              if (module.number === 1 || module.number === 2) {
                bloomLevel = 'Remember · Understand';
              } else if (module.number === 3) {
                bloomLevel = 'Understand';
              } else if (module.number === 4) {
                bloomLevel = 'Analyze';
              } else if (module.number === 5) {
                bloomLevel = 'Apply';
              } else if (module.number === 6) {
                bloomLevel = 'Evaluate';
              }

              return (
                <Link
                  key={module.slug}
                  href={`/courses/hcai-foundations/${module.slug}`}
                  className="group relative flex flex-col justify-between overflow-hidden rounded-[8px] border border-[#e2e8f0] bg-[#ffffff] p-[24px] shadow-none cursor-pointer transition-all duration-200 hover:border-[#0d9488] hover:shadow-[0_4px_12px_rgba(13,148,136,0.1)] hover:-translate-y-[2px]"
                >
                  <div>
                    <span className="inline-flex text-[12px] font-medium text-[#94a3b8] mb-4">
                      0{module.number}
                    </span>
                    <h4 className="text-[17px] font-semibold text-[#0f172a] mb-2">
                      {module.title}
                    </h4>
                    <p className="text-[12px] text-[#64748b] uppercase tracking-[0.06em] font-semibold">
                      {module.lessons} Lessons
                    </p>
                  </div>
                  
                  {/* Bloom's level gray pill badge */}
                  {bloomLevel && (
                    <div className="mt-3">
                      <span className="inline-flex items-center bg-[#f1f5f9] text-[#64748b] text-[10px] px-2 py-0.5 rounded-full font-medium">
                        {bloomLevel}
                      </span>
                    </div>
                  )}
                </Link>
              )
            })}
          </div>

          <div className="mt-16 text-center">
            <Link
              href="/courses/hcai-foundations"
              className="inline-flex items-center justify-center rounded-[6px] bg-[#1e3a8a] px-6 py-3 text-sm font-semibold text-white transition-all duration-200 hover:bg-[#1e3a8a]/90 active:scale-95"
            >
              Mulai Petualangan Belajarmu →
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
