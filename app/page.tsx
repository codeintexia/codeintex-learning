import Link from 'next/link'
import courseData from '@/content/courses/hcai-foundations/_course.json'

export default function HomePage() {
  return (
    <div className="flex flex-col items-stretch">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-slate-900 text-white py-24 sm:py-32">
        {/* Background gradient grid effect */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#0f172a_1px,transparent_1px),linear-gradient(to_bottom,#0f172a_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] opacity-20" />
        <div className="absolute inset-0 bg-gradient-to-br from-teal-500/10 via-transparent to-transparent" />
        
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative z-10">
          <div className="max-w-3xl">
            <span className="inline-flex items-center gap-1.5 rounded-full bg-teal-500/10 px-3.5 py-1.5 text-xs font-semibold text-teal-400 border border-teal-500/25 mb-6">
              <span className="h-1.5 w-1.5 rounded-full bg-teal-400 animate-pulse" />
              Kursus Baru Dirilis
            </span>
            <h1 className="text-4xl font-extrabold tracking-tight sm:text-6xl text-white mb-6">
              Human-Centered AI <br />
              <span className="bg-gradient-to-r from-teal-400 to-teal-200 bg-clip-text text-transparent">
                — Foundations
              </span>
            </h1>
            <p className="text-lg sm:text-xl text-slate-300 leading-relaxed mb-8">
              {courseData.subtitle}. Kuasai dasar merancang sistem kecerdasan buatan yang transparan, adil, aman, dan berdaya guna tinggi bagi penggunanya.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <Link
                href="/courses/hcai-foundations"
                className="inline-flex items-center justify-center rounded-xl bg-teal-500 px-6 py-3.5 text-sm font-bold text-slate-950 shadow-lg shadow-teal-500/20 transition-all duration-200 hover:bg-teal-400 active:scale-95"
              >
                Mulai Belajar Sekarang (Gratis) →
              </Link>
              <a
                href="#kurikulum"
                className="inline-flex items-center justify-center rounded-xl border border-slate-700 bg-slate-800/40 px-6 py-3.5 text-sm font-semibold text-slate-200 transition-all duration-200 hover:bg-slate-800 hover:border-slate-600 active:scale-95"
              >
                Lihat Kurikulum
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="border-y border-slate-200 bg-white py-8">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div className="p-4">
              <span className="block text-3xl font-extrabold text-teal-600">6</span>
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 mt-1 block">Modul Pembelajaran</span>
            </div>
            <div className="p-4">
              <span className="block text-3xl font-extrabold text-teal-600">25</span>
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 mt-1 block">Lesson Interaktif</span>
            </div>
            <div className="p-4">
              <span className="block text-3xl font-extrabold text-teal-600">6 Jam</span>
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 mt-1 block">Estimasi Waktu Belajar</span>
            </div>
            <div className="p-4">
              <span className="block text-3xl font-extrabold text-teal-600">100%</span>
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 mt-1 block">Gratis & Terbuka</span>
            </div>
          </div>
        </div>
      </section>

      {/* Curriculum Overview */}
      <section id="kurikulum" className="py-20 sm:py-28 bg-slate-50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-xs font-bold uppercase tracking-widest text-teal-600 mb-3">Struktur Pembelajaran</h2>
            <h3 className="text-3xl font-extrabold tracking-tight sm:text-4xl text-slate-900 mb-4">
              Kurikulum Human-Centered AI
            </h3>
            <p className="text-slate-500 text-sm sm:text-base leading-relaxed">
              Dirancang secara sistematis dari pemahaman filosofis hingga evaluasi praktis. Setiap modul dilengkapi dengan lesson komprehensif, analisis kasus nyata, dan refleksi mandiri.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {courseData.modules.map((module) => (
              <div
                key={module.slug}
                className="group relative flex flex-col justify-between overflow-hidden rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:border-teal-500/30 hover:shadow-md hover:shadow-teal-500/[0.02]"
              >
                <div>
                  <span className="inline-flex h-9 w-9 items-center justify-center rounded-xl bg-slate-50 font-bold text-slate-400 group-hover:bg-teal-50 group-hover:text-teal-600 transition-colors mb-4">
                    0{module.number}
                  </span>
                  <h4 className="text-lg font-bold text-slate-900 group-hover:text-teal-600 transition-colors mb-2">
                    {module.title}
                  </h4>
                  <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold mb-6">
                    {module.lessons} Lessons
                  </p>
                </div>
                <Link
                  href={`/courses/hcai-foundations#modul-${module.number}`}
                  className="mt-4 inline-flex items-center text-xs font-bold text-teal-600 hover:text-teal-700 gap-1"
                >
                  Lihat Outline Modul
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </Link>
              </div>
            ))}
          </div>

          <div className="mt-16 text-center">
            <Link
              href="/courses/hcai-foundations"
              className="inline-flex items-center justify-center rounded-xl bg-teal-600 px-8 py-4 text-base font-bold text-white shadow-lg shadow-teal-600/10 transition-all duration-200 hover:bg-teal-700 active:scale-95"
            >
              Mulai Petualangan Belajarmu →
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
