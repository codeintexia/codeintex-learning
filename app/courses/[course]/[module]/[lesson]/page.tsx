import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getModuleSlugs, getLessonSlugs, getLesson, getAllLessons } from '@/lib/content'
import LessonRenderer from '@/components/LessonRenderer'
import CourseNavigation from '@/components/CourseNavigation'
import ReadingProgressBar from '@/components/ReadingProgressBar'
import courseData from '@/content/courses/hcai-foundations/_course.json'

interface PageProps {
  params: Promise<{
    course: string
    module: string
    lesson: string
  }>
}

export async function generateStaticParams() {
  const courseSlug = 'hcai-foundations'
  const moduleSlugs = getModuleSlugs(courseSlug)
  const paths = []

  for (const moduleSlug of moduleSlugs) {
    const lessonSlugs = getLessonSlugs(courseSlug, moduleSlug)
    for (const lessonSlug of lessonSlugs) {
      paths.push({
        course: courseSlug,
        module: moduleSlug,
        lesson: lessonSlug,
      })
    }
  }

  return paths
}

export const dynamicParams = false

export default async function LessonPage({ params }: PageProps) {
  const resolvedParams = await params
  
  if (resolvedParams.course !== 'hcai-foundations') {
    return notFound()
  }

  // Fetch all lessons for outline navigation and prev/next calculations
  const allLessons = getAllLessons(resolvedParams.course)
  
  // Find current lesson data
  const currentLessonIndex = allLessons.findIndex(
    (l) => l.moduleSlug === resolvedParams.module && l.slug === resolvedParams.lesson
  )
  
  if (currentLessonIndex === -1) {
    return notFound()
  }

  const currentLesson = allLessons[currentLessonIndex]
  const prevLesson = currentLessonIndex > 0 ? allLessons[currentLessonIndex - 1] : undefined
  const nextLesson = currentLessonIndex < allLessons.length - 1 ? allLessons[currentLessonIndex + 1] : undefined

  // Prepare navigation link props
  const prevLessonProps = prevLesson
    ? {
        title: prevLesson.frontmatter.title,
        href: `/courses/${resolvedParams.course}/${prevLesson.moduleSlug}/${prevLesson.slug}`,
      }
    : undefined

  const nextLessonProps = nextLesson
    ? {
        title: nextLesson.frontmatter.title,
        href: `/courses/${resolvedParams.course}/${nextLesson.moduleSlug}/${nextLesson.slug}`,
      }
    : undefined

  // Construct structured data for sidebar
  const sidebarModules = courseData.modules.map((m) => {
    const mSlug = getModuleSlugs(resolvedParams.course).find((slug) => slug.includes(m.slug)) || m.slug
    const lessonSlugs = getLessonSlugs(resolvedParams.course, mSlug)
    const lessons = lessonSlugs.map((lSlug) => {
      const { frontmatter } = getLesson(resolvedParams.course, mSlug, lSlug)
      return {
        slug: lSlug,
        title: frontmatter.title,
        lessonNumber: frontmatter.lesson,
        isActive: mSlug === resolvedParams.module && lSlug === resolvedParams.lesson,
      }
    })

    return {
      ...m,
      dirSlug: mSlug,
      lessons: lessons.sort((a, b) => a.lessonNumber - b.lessonNumber),
      isCurrentModule: mSlug === resolvedParams.module,
    }
  })

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-10 flex flex-col md:flex-row gap-8 items-start">
      <ReadingProgressBar />
      
      {/* Mobile Breadcrumbs & Navigation Header */}
      <div className="w-full md:hidden mb-4 border-b border-slate-200 pb-4">
        <nav className="mb-2 flex items-center gap-1.5 text-[10px] font-bold uppercase tracking-wider text-slate-400">
          <Link href={`/courses/${resolvedParams.course}`} className="hover:text-teal-600">
            {courseData.title}
          </Link>
          <span>/</span>
          <span className="text-slate-500 line-clamp-1">
            Modul {currentLesson.frontmatter.module}
          </span>
        </nav>
        <h2 className="text-sm font-bold text-slate-800 line-clamp-1">
          Lesson {currentLesson.frontmatter.lesson}: {currentLesson.frontmatter.title}
        </h2>
      </div>

      {/* Desktop Sidebar (Sticky left) */}
      <aside className="hidden md:block w-72 shrink-0 sticky top-20 max-h-[calc(100vh-7rem)] overflow-y-auto border border-slate-200 bg-white rounded-2xl p-4 shadow-sm select-none">
        <div className="border-b border-slate-100 pb-3 mb-4">
          <Link
            href={`/courses/${resolvedParams.course}`}
            className="text-[10px] font-extrabold text-teal-600 uppercase tracking-widest hover:text-teal-700 block mb-1"
          >
            ← Kembali ke Silabus
          </Link>
          <h3 className="text-xs font-black text-slate-900 tracking-tight line-clamp-2 leading-tight">
            {courseData.title}
          </h3>
        </div>
        
        <div className="space-y-6">
          {sidebarModules.map((mod) => (
            <div key={mod.number} className="space-y-2">
              <div className="flex items-center justify-between">
                <h4 className="text-[11px] font-black uppercase tracking-wider text-slate-400">
                  Modul 0{mod.number}
                </h4>
                {mod.isCurrentModule && (
                  <span className="h-1.5 w-1.5 rounded-full bg-teal-500" />
                )}
              </div>
              <ul className="space-y-1 pl-1">
                {mod.lessons.map((les) => (
                  <li key={les.slug}>
                    <Link
                      href={`/courses/${resolvedParams.course}/${mod.dirSlug}/${les.slug}`}
                      className={`block rounded-lg px-3 py-2 text-xs font-semibold leading-relaxed transition-all duration-200 border ${
                        les.isActive
                          ? 'bg-teal-50/70 border-teal-500/20 text-teal-700 shadow-sm shadow-teal-500/[0.02]'
                          : 'border-transparent text-slate-500 hover:bg-slate-50 hover:text-slate-900'
                      }`}
                    >
                      <span className="inline-block w-4 font-bold text-[10px] opacity-65">
                        {les.lessonNumber}.
                      </span>
                      <span className="line-clamp-2 inline-block align-top max-w-[85%]">
                        {les.title}
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </aside>

      {/* Lesson Content Area */}
      <main className="flex-1 w-full max-w-3xl border border-slate-200/60 bg-white rounded-2xl p-6 sm:p-10 shadow-sm min-h-[50vh]">
        {/* Lesson Metadata Header */}
        <div className="border-b border-slate-100 pb-6 mb-8">
          <span className="inline-flex items-center gap-1.5 text-xs font-bold text-teal-600 tracking-wider mb-3">
            Module {String(currentLesson.frontmatter.module).padStart(2, '0')} › Lesson {String(currentLesson.frontmatter.lesson).padStart(2, '0')}
          </span>
          <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight leading-tight mb-4">
            {currentLesson.frontmatter.title}
          </h1>
          <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-xs font-semibold text-slate-400">
            <span className="flex items-center gap-1">
              ⏱️ Waktu baca: {currentLesson.frontmatter.duration_minutes} menit
            </span>
            <span className="hidden sm:inline">•</span>
            <span className="flex items-center gap-1 uppercase">
              🎯 Level: {currentLesson.frontmatter.bloom_level}
            </span>
          </div>
        </div>

        {/* Markdown content */}
        <LessonRenderer content={currentLesson.content} />

        {/* Prev / Next Navigation */}
        <CourseNavigation prevLesson={prevLessonProps} nextLesson={nextLessonProps} />
      </main>

    </div>
  )
}
