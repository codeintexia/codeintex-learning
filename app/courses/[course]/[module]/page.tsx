import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getModuleSlugs, getLessonSlugs, getLesson, getCourse, getAllCourseSlugs } from '@/lib/content'

interface PageProps {
  params: Promise<{
    course: string
    module: string
  }>
}

export async function generateStaticParams() {
  const courseSlugs = getAllCourseSlugs()
  const paths = []

  for (const courseSlug of courseSlugs) {
    const moduleSlugs = getModuleSlugs(courseSlug)
    for (const moduleSlug of moduleSlugs) {
      paths.push({
        course: courseSlug,
        module: moduleSlug,
      })
    }
  }

  return paths
}

export const dynamicParams = false

export default async function ModulePage({ params }: PageProps) {
  const resolvedParams = await params
  const courseData = getCourse(resolvedParams.course)
  
  if (!courseData) {
    return notFound()
  }

  // Find module in course metadata
  const currentModule = courseData.modules.find(
    (m) => m.slug === resolvedParams.module || resolvedParams.module.includes(m.slug)
  )

  if (!currentModule) {
    return notFound()
  }

  // Fetch all lessons in this module
  const lessonSlugs = getLessonSlugs(resolvedParams.course, resolvedParams.module)
  const lessons = lessonSlugs.map((lSlug) => {
    const { frontmatter } = getLesson(resolvedParams.course, resolvedParams.module, lSlug)
    return {
      slug: lSlug,
      title: frontmatter.title,
      duration: frontmatter.duration_minutes,
      lessonNumber: frontmatter.lesson,
    }
  }).sort((a, b) => a.lessonNumber - b.lessonNumber)

  const firstLessonUrl = lessons.length > 0 
    ? `/courses/${resolvedParams.course}/${resolvedParams.module}/${lessons[0].slug}`
    : `/courses/${resolvedParams.course}`

  return (
    <div className="bg-[#f8fafc] min-h-screen py-16 sm:py-24">
      <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
        
        {/* Breadcrumb */}
        <nav className="mb-6 flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-slate-400">
          <Link href="/" className="hover:text-[#0d9488] transition-colors duration-150">Home</Link>
          <span>/</span>
          <Link href={`/courses/${resolvedParams.course}`} className="hover:text-[#0d9488] transition-colors duration-150">
            {courseData.title}
          </Link>
          <span>/</span>
          <span className="text-slate-500">Modul {currentModule.number}</span>
        </nav>

        {/* Module Header Card */}
        <div className="rounded-2xl border border-[#e2e8f0] bg-white p-8 shadow-none mb-12">
          <span className="block text-xs font-bold text-[#0d9488] uppercase tracking-widest mb-2">
            Modul 0{currentModule.number}
          </span>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight mb-6">
            {currentModule.title}
          </h1>
          
          <div className="flex flex-wrap items-center gap-4">
            <Link
              href={firstLessonUrl}
              className="inline-flex items-center justify-center rounded-[6px] bg-[#1e3a8a] px-6 py-3 text-sm font-bold text-white shadow-none transition-all duration-200 hover:bg-[#1e3a8a]/90 active:scale-95"
            >
              Mulai Belajar Modul Ini →
            </Link>
          </div>
        </div>

        {/* Lessons List */}
        <h2 className="text-xl font-extrabold text-slate-900 mb-6 tracking-tight">Daftar Lesson</h2>
        
        <div className="space-y-4">
          {lessons.map((lesson) => (
            <Link
              key={lesson.slug}
              href={`/courses/${resolvedParams.course}/${resolvedParams.module}/${lesson.slug}`}
              className="flex items-center justify-between p-6 rounded-2xl border border-[#e2e8f0] bg-white hover:border-[#0d9488] hover:shadow-none transition-all duration-200 group"
            >
              <div className="flex items-start gap-4">
                <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg bg-[#f0fdfa] text-xs font-bold text-[#0d9488] transition-colors group-hover:bg-[#0d9488] group-hover:text-white">
                  {lesson.lessonNumber}
                </span>
                <div>
                  <h3 className="text-sm font-semibold text-slate-800 transition-colors group-hover:text-[#0d9488] leading-snug">
                    {lesson.title}
                  </h3>
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
    </div>
  )
}
