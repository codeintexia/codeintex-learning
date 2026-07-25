import Link from 'next/link'

interface CourseNavigationProps {
  prevLesson?: { title: string; href: string }
  nextLesson?: { title: string; href: string }
}
export default function CourseNavigation({ prevLesson, nextLesson }: CourseNavigationProps) {
  return (
    <nav className="mt-[80px] pt-[32px] border-t border-[#e2e8f0] grid grid-cols-2 gap-[16px] w-full">
      {prevLesson ? (
        <Link
          href={prevLesson.href}
          className="block border border-[#e2e8f0] rounded-[8px] p-[16px_20px] cursor-pointer transition-all duration-200 ease-in-out hover:border-[#0d9488] hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]"
        >
          <span className="block text-[12px] font-medium text-[#94a3b8] mb-[4px]">
            ← Sebelumnya
          </span>
          <span className="block text-[14px] font-semibold text-[#0f172a] leading-[1.3]">
            {prevLesson.title}
          </span>
        </Link>
      ) : (
        <div />
      )}
      
      {nextLesson ? (
        <Link
          href={nextLesson.href}
          className="block border border-[#e2e8f0] rounded-[8px] p-[16px_20px] cursor-pointer text-right transition-all duration-200 ease-in-out hover:border-[#0d9488] bg-[#f8fafc] hover:-translate-y-[2px] hover:shadow-[0_4px_16px_rgba(0,0,0,0.08)]"
        >
          <span className="block text-[12px] font-medium text-[#0d9488] mb-[4px]">
            Berikutnya →
          </span>
          <span className="block text-[14px] font-semibold text-[#0f172a] leading-[1.3]">
            {nextLesson.title}
          </span>
        </Link>
      ) : (
        <div />
      )}
    </nav>
  )
}
