import Link from 'next/link'

interface CourseNavigationProps {
  prevLesson?: { title: string; href: string }
  nextLesson?: { title: string; href: string }
}

export default function CourseNavigation({ prevLesson, nextLesson }: CourseNavigationProps) {
  return (
    <nav className="mt-12 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 border-t border-slate-100 pt-8">
      {prevLesson ? (
        <Link
          href={prevLesson.href}
          className="group flex flex-1 items-center gap-4 rounded-xl border border-slate-200 p-4 transition-all duration-200 hover:border-teal-500/30 hover:bg-teal-50/10 active:scale-[0.99]"
        >
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-500 transition-colors group-hover:bg-teal-50 group-hover:text-teal-600">
            ←
          </span>
          <div className="text-left">
            <span className="block text-[10px] font-bold uppercase tracking-wider text-slate-400">Lesson Sebelumnya</span>
            <span className="block text-sm font-semibold text-slate-700 transition-colors group-hover:text-teal-600 line-clamp-1">
              {prevLesson.title}
            </span>
          </div>
        </Link>
      ) : (
        <div className="flex-1 hidden sm:block" />
      )}
      
      {nextLesson ? (
        <Link
          href={nextLesson.href}
          className="group flex flex-1 items-center justify-between gap-4 rounded-xl border border-teal-600 bg-teal-600 p-4 transition-all duration-200 hover:bg-teal-700 hover:border-teal-700 shadow-sm shadow-teal-600/10 active:scale-[0.99] text-white"
        >
          <div className="text-left">
            <span className="block text-[10px] font-bold uppercase tracking-wider text-teal-200">Lesson Berikutnya</span>
            <span className="block text-sm font-bold transition-colors line-clamp-1">
              {nextLesson.title}
            </span>
          </div>
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-teal-500/50 text-white transition-transform group-hover:translate-x-1">
            →
          </span>
        </Link>
      ) : (
        <div className="flex-1 hidden sm:block" />
      )}
    </nav>
  )
}
