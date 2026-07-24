import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getModuleSlugs, getLessonSlugs, getLesson, getCourse, getAllCourseSlugs } from '@/lib/content'

interface PageProps {
  params: Promise<{
    course: string
  }>
}

export async function generateStaticParams() {
  const courseSlugs = getAllCourseSlugs()
  return courseSlugs.map((slug) => ({
    course: slug,
  }))
}

export const dynamicParams = false

export default async function CoursePage({ params }: PageProps) {
  const resolvedParams = await params
  const courseData = getCourse(resolvedParams.course)
  
  if (!courseData) {
    return notFound()
  }

  // Load modules and lessons dynamically
  const moduleSlugs = getModuleSlugs(resolvedParams.course)
  const modulesWithLessons = courseData.modules.map((m) => {
    // Find matching module directory
    const mSlug = moduleSlugs.find((slug) => slug.includes(m.slug)) || m.slug
    const lessonSlugs = getLessonSlugs(resolvedParams.course, mSlug)
    const lessons = lessonSlugs.map((lSlug) => {
      const { frontmatter } = getLesson(resolvedParams.course, mSlug, lSlug)
      return {
        slug: lSlug,
        title: frontmatter.title,
        duration: frontmatter.duration_minutes,
        lessonNumber: frontmatter.lesson,
      }
    })

    return {
      ...m,
      dirSlug: mSlug,
      lessons: lessons.sort((a, b) => a.lessonNumber - b.lessonNumber),
    }
  })

  return (
    <div className="bg-[#f8fafc] min-h-screen py-16 sm:py-24">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        
        {/* Breadcrumb */}
        <nav className="mb-6 flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-slate-400">
          <Link href="/" className="hover:text-[#0d9488] transition-colors">Home</Link>
          <span>/</span>
          <span className="text-slate-500">Kursus</span>
        </nav>

        {/* Course Header Card */}
        <div className="rounded-2xl border border-[#e2e8f0] bg-white p-8 shadow-none mb-12">
          <span className="inline-flex items-center gap-1.5 rounded-full bg-[#f0fdfa] px-2.5 py-1 text-xs font-bold text-[#0d9488] border border-[#99f6e4] mb-4 uppercase tracking-wider">
            {courseData.level}
          </span>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">
            {courseData.title}
          </h1>
          {/* Subtle one-line attribution for institutional framing (FIX 7) */}
          <div className="text-[#64748b] text-[13px] mt-2 mb-4 font-normal">
            Diproduksi oleh CodeinteX &middot; Bahasa Indonesia &middot; Tersedia gratis
          </div>
          <p className="text-slate-600 leading-relaxed mb-6">
            {courseData.subtitle}. Kursus ini dirancang untuk mendemistifikasi kecerdasan buatan dari sudut pandang interaksi manusia-komputer dan etika pengembangan produk.
          </p>
          
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 border-t border-slate-100 pt-6 text-sm">
            <div>
              <span className="block text-slate-400 font-medium text-xs uppercase tracking-wider">Durasi</span>
              <span className="font-bold text-slate-800">{courseData.duration_hours} Jam</span>
            </div>
            <div>
              <span className="block text-slate-400 font-medium text-xs uppercase tracking-wider">Bahasa</span>
              <span className="font-bold text-slate-800">Bahasa Indonesia ({courseData.language.toUpperCase()})</span>
            </div>
            <div>
              <span className="block text-slate-400 font-medium text-xs uppercase tracking-wider">Biaya</span>
              <span className="font-bold text-[#0d9488]">{courseData.is_free ? 'Gratis' : 'Berbayar'}</span>
            </div>
          </div>
        </div>

        {/* Modules List */}
        <h2 className="text-xl font-extrabold text-slate-900 mb-6 tracking-tight">Kurikulum & Silabus</h2>
        
        <div className="space-y-8">
          {modulesWithLessons.map((mod) => (
            <div
              key={mod.number}
              id={`modul-${mod.number}`}
              className="rounded-2xl border border-[#e2e8f0] bg-white shadow-none overflow-hidden scroll-mt-20"
            >
              {/* Module header */}
              <div className="border-b border-[#e2e8f0] bg-[#f8fafc] p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                  <span className="block text-xs font-bold text-[#0d9488] uppercase tracking-widest mb-1">
                    Modul 0{mod.number}
                  </span>
                  <h3 className="text-lg font-bold text-slate-900 tracking-tight">
                    {mod.title}
                  </h3>
                </div>
                <span className="shrink-0 rounded-full bg-slate-200/60 px-3 py-1 text-xs font-semibold text-slate-600">
                  {mod.lessons.length} Lessons
                </span>
              </div>

              {/* Lessons List */}
              <div className="divide-y divide-[#e2e8f0]">
                {mod.lessons.map((lesson) => (
                  <Link
                    key={lesson.slug}
                    href={`/courses/${resolvedParams.course}/${mod.dirSlug}/${lesson.slug}`}
                    className="flex items-center justify-between p-6 hover:bg-[#f8fafc] transition-colors group"
                  >
                    <div className="flex items-start gap-4">
                      <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg bg-[#f0fdfa] text-xs font-bold text-[#0d9488] transition-colors group-hover:bg-[#0d9488] group-hover:text-white">
                        {lesson.lessonNumber}
                      </span>
                      <div>
                        <h4 className="text-sm font-semibold text-slate-800 transition-colors group-hover:text-[#0d9488] leading-snug">
                          {lesson.title}
                        </h4>
                        <span className="text-[11px] text-slate-400 font-medium uppercase tracking-wider block mt-1">
                          Waktu baca: {lesson.duration} menit
                        </span>
                      </div>
                    </div>
                    <span className="text-slate-300 transition-transform group-hover:translate-x-1 group-hover:text-[#0d9488] text-sm">
                      →
                    </span>
                  </Link>
                ))}
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  )
}
