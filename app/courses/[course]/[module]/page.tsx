import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getModuleSlugs, getLessonSlugs, getLesson } from '@/lib/content'
import courseData from '@/content/courses/hcai-foundations/_course.json'

interface PageProps {
  params: Promise<{
    course: string
    module: string
  }>
}

export async function generateStaticParams() {
  const courseSlug = 'hcai-foundations'
  const moduleSlugs = getModuleSlugs(courseSlug)
  return moduleSlugs.map((moduleSlug) => ({
    course: courseSlug,
    module: moduleSlug,
  }))
}

export const dynamicParams = false

export default async function ModulePage({ params }: PageProps) {
  const resolvedParams = await params
  
  if (resolvedParams.course !== 'hcai-foundations') {
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
    <div className="bg-slate-50 min-h-screen py-16 sm:py-24">
      <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
        
        {/* Breadcrumb */}
        <nav className="mb-6 flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-slate-400">
          <Link href="/" className="hover:text-teal-600 transition-colors">Home</Link>
          <span>/</span>
          <Link href={`/courses/${resolvedParams.course}`} className="hover:text-teal-600 transition-colors">
            {courseData.title}
          </Link>
          <span>/</span>
          <span className="text-slate-500">Modul {currentModule.number}</span>
        </nav>

        {/* Module Header Card */}
        <div className="rounded-2xl border border-slate-200 bg-white p-8 shadow-sm mb-12">
          <span className="block text-xs font-bold text-teal-600 uppercase tracking-widest mb-2">
            Modul 0{currentModule.number}
          </span>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight mb-6">
            {currentModule.title}
          </h1>
          
          <div className="flex flex-wrap items-center gap-4">
            <Link
              href={firstLessonUrl}
              className="inline-flex items-center justify-center rounded-xl bg-teal-600 px-6 py-3 text-sm font-bold text-white shadow-lg shadow-teal-600/10 transition-all duration-200 hover:bg-teal-700 active:scale-95"
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
              className="flex items-center justify-between p-6 rounded-2xl border border-slate-200 bg-white hover:border-teal-500/30 hover:shadow-sm transition-all duration-200 group"
            >
              <div className="flex items-start gap-4">
                <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg bg-teal-50 text-xs font-bold text-teal-700 transition-colors group-hover:bg-teal-600 group-hover:text-white">
                  {lesson.lessonNumber}
                </span>
                <div>
                  <h3 className="text-sm font-semibold text-slate-800 transition-colors group-hover:text-teal-600 leading-snug">
                    {lesson.title}
                  </h3>
                  <span className="text-[11px] text-slate-400 font-medium uppercase tracking-wider block mt-1">
                    Waktu baca: {lesson.duration} menit
                  </span>
                </div>
              </div>
              <span className="text-slate-300 transition-transform group-hover:translate-x-1 group-hover:text-teal-600 text-sm">
                →
              </span>
            </Link>
          ))}
        </div>

      </div>
    </div>
  )
}
