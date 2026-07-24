import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getModuleSlugs, getLessonSlugs, getLesson, getAllLessons, getCourse, getAllCourseSlugs } from '@/lib/content'
import LessonRenderer from '@/components/LessonRenderer'
import CourseNavigation from '@/components/CourseNavigation'
// Import the client-side ReadingProgress component for tracking page scroll
import { ReadingProgress } from '@/components/ReadingProgressBar'

interface PageProps {
  params: Promise<{
    course: string
    module: string
    lesson: string
  }>
}

export async function generateStaticParams() {
  const courseSlugs = getAllCourseSlugs()
  const paths = []

  for (const courseSlug of courseSlugs) {
    const moduleSlugs = getModuleSlugs(courseSlug)
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
  }

  return paths
}

export const dynamicParams = false

export default async function LessonPage({ params }: PageProps) {
  const resolvedParams = await params
  const courseData = getCourse(resolvedParams.course)
  
  if (!courseData) {
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

  // Calculate the total number of lessons in the current module to show position badges (FIX 1)
  const currentModuleLessons = allLessons.filter((l) => l.moduleSlug === resolvedParams.module)
  const totalLessonsInModule = currentModuleLessons.length

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
    <div className="w-full bg-[#ffffff] flex min-h-screen relative">
      {/* Scroll indicator bar at the top of the viewport */}
      <ReadingProgress />
      
      {/* Mobile Breadcrumbs & Navigation Header */}
      <div className="w-full md:hidden mb-4 border-b border-[#e2e8f0] pb-4 px-4">
        <nav className="mb-2 flex items-center gap-1.5 text-[11px] text-[#94a3b8]">
          <Link href={`/courses/${resolvedParams.course}`} className="hover:text-[#0f172a] transition-colors">
            Module {String(currentLesson.frontmatter.module).padStart(2, '0')}
          </Link>
          <span>›</span>
          <span className="text-[#0f172a] font-medium line-clamp-1">
            Lesson {String(currentLesson.frontmatter.lesson).padStart(2, '0')}
          </span>
        </nav>
        <h2 className="text-sm font-bold text-[#0f172a] line-clamp-1">
          Lesson {currentLesson.frontmatter.lesson}: {currentLesson.frontmatter.title}
        </h2>
      </div>

      {/* Desktop Sidebar (Sticky left) - Width: 300px, Padding: 20px 0 */}
      <aside className="hidden md:block w-[300px] shrink-0 sticky top-16 h-[calc(100vh-64px)] overflow-y-auto border-r border-[#e2e8f0] bg-[#f8fafc] py-5 select-none">
        {/* Course title at the top of the sidebar with a teal dot prefix */}
        <div className="px-[16px] pt-0 pb-[16px] border-b border-[#e2e8f0]">
          <Link
            href={`/courses/${resolvedParams.course}`}
            className="text-[10px] font-extrabold text-[#0d9488] uppercase tracking-widest hover:text-[#0f766e] block mb-2"
          >
            ← Kembali ke Silabus
          </Link>
          <div className="flex items-center gap-[8px]">
            <span className="w-[6px] h-[6px] bg-[#0d9488] rounded-full shrink-0" />
            <h3 className="text-[13px] font-bold text-[#0f172a]">
              HCAI Foundations
            </h3>
          </div>
        </div>
        
        {/* Sidebar list items */}
        <div className="space-y-6">
          {sidebarModules.map((mod) => (
            <div key={mod.number} className="space-y-2">
              {/* Module header group label */}
              <div className="flex items-center justify-between pt-[16px] px-[16px] pb-[6px]">
                <h4 className="text-[11px] font-bold uppercase tracking-[0.08em] text-[#94a3b8]">
                  Modul 0{mod.number}
                </h4>
              </div>
              <ul className="space-y-1">
                {mod.lessons.map((les) => (
                  <li key={les.slug}>
                    <Link
                      href={`/courses/${resolvedParams.course}/${mod.dirSlug}/${les.slug}`}
                      className={`block text-[13px] leading-[1.4] py-[7px] pr-[16px] border-l-[3px] cursor-pointer transition-all duration-150 ${
                        les.isActive
                          ? 'bg-[#f0fdfa] text-[#0d9488] font-bold border-l-[#0d9488] pl-[13px]'
                          : 'border-l-transparent pl-[13px] text-[#64748b] hover:bg-[#f8fafc] hover:text-[#334155] hover:border-l-[#e2e8f0]'
                      }`}
                    >
                      <span className="inline-block w-4 font-bold text-[10px] opacity-65">
                        {les.lessonNumber}.
                      </span>
                      <span className="line-clamp-2 inline-block align-top max-w-[85%]">
                        {/* Render a small teal dot before the active lesson title (FIX 2) */}
                        {les.isActive && (
                          <span className="inline-block w-[6px] h-[6px] bg-[#0d9488] rounded-full mr-[8px] align-middle mb-[2px]" />
                        )}
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

      {/* Lesson Content Area - Max width: 720px, responsive padding */}
      <main className="flex-1 py-[24px] px-[20px] md:py-[48px] md:px-[64px] max-w-[720px] mx-auto min-h-[50vh] w-full">
        {/* Lesson Breadcrumb */}
        <nav className="flex items-center gap-2 text-[13px] text-[#94a3b8] pb-[24px] border-b border-[#e2e8f0] mb-[32px]">
          <Link href={`/courses/${resolvedParams.course}`} className="hover:text-[#0f172a] transition-colors duration-150">
            Module {String(currentLesson.frontmatter.module).padStart(2, '0')}
          </Link>
          <span>›</span>
          <span className="text-[#0f172a] font-medium">
            Lesson {String(currentLesson.frontmatter.lesson).padStart(2, '0')}
          </span>
        </nav>

        {/* Lesson Header */}
        <div className="mb-8">
          <h1 className="text-[32px] font-bold text-[#0f172a] leading-[1.25] mb-[16px]">
            {currentLesson.frontmatter.title}
          </h1>
          
          {/* Individual styled chips/badges for lesson metadata (FIX 1) */}
          <div className="flex flex-wrap gap-[8px] mb-[32px]">
            <span className="bg-[#f1f5f9] text-[#475569] text-[12px] py-[3px] px-[12px] rounded-full font-medium">
              Modul {currentLesson.frontmatter.module} &middot; {currentLesson.frontmatter.module_title}
            </span>
            <span className="bg-[#f1f5f9] text-[#475569] text-[12px] py-[3px] px-[12px] rounded-full font-medium">
              Lesson {currentLesson.frontmatter.lesson} dari {totalLessonsInModule}
            </span>
            <span className="bg-[#f1f5f9] text-[#475569] text-[12px] py-[3px] px-[12px] rounded-full font-medium">
              ⏱ {currentLesson.frontmatter.duration_minutes} menit
            </span>
            <span className="bg-[#f1f5f9] text-[#475569] text-[12px] py-[3px] px-[12px] rounded-full font-medium">
              Foundational
            </span>
            <span className="bg-[#f1f5f9] text-[#475569] text-[12px] py-[3px] px-[12px] rounded-full font-medium capitalize">
              {currentLesson.frontmatter.bloom_level}
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
