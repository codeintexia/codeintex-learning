import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const contentDir = path.join(process.cwd(), 'content/courses')

export interface LessonFrontmatter {
  course: string
  module: number
  module_title: string
  lesson: number
  title: string
  duration_minutes: number
  bloom_level: string
  keywords: string[]
  is_free: boolean
  status: string
  slug?: string
}

export interface LessonData {
  frontmatter: LessonFrontmatter
  content: string
  slug: string
  moduleSlug: string
  courseSlug: string
}

export function getLessonSlugs(courseSlug: string, moduleSlug: string): string[] {
  const moduleDir = path.join(contentDir, courseSlug, moduleSlug)
  return fs
    .readdirSync(moduleDir)
    .filter((f) => f.endsWith('.md') && !f.startsWith('_'))
    .map((f) => f.replace('.md', ''))
    .sort()
}

export function getLesson(
  courseSlug: string,
  moduleSlug: string,
  lessonSlug: string
): LessonData {
  const filePath = path.join(contentDir, courseSlug, moduleSlug, `${lessonSlug}.md`)
  const raw = fs.readFileSync(filePath, 'utf-8')
  const { data, content } = matter(raw)

  return {
    frontmatter: data as LessonFrontmatter,
    content,
    slug: lessonSlug,
    moduleSlug,
    courseSlug,
  }
}

export function getModuleSlugs(courseSlug: string): string[] {
  const courseDir = path.join(contentDir, courseSlug)
  return fs
    .readdirSync(courseDir)
    .filter((f) => {
      const fullPath = path.join(courseDir, f)
      return fs.statSync(fullPath).isDirectory() && f.startsWith('m')
    })
    .sort()
}

export function getAllLessons(courseSlug: string): LessonData[] {
  const lessons: LessonData[] = []
  const moduleSlugs = getModuleSlugs(courseSlug)

  for (const moduleSlug of moduleSlugs) {
    const lessonSlugs = getLessonSlugs(courseSlug, moduleSlug)
    for (const lessonSlug of lessonSlugs) {
      lessons.push(getLesson(courseSlug, moduleSlug, lessonSlug))
    }
  }

  return lessons
}

export function getAllCourseSlugs(): string[] {
  if (!fs.existsSync(contentDir)) return []
  return fs
    .readdirSync(contentDir)
    .filter((f) => {
      const fullPath = path.join(contentDir, f)
      return fs.statSync(fullPath).isDirectory() && fs.existsSync(path.join(fullPath, '_course.json'))
    })
    .sort()
}

export interface CourseModule {
  number: number
  slug: string
  title: string
  lessons: number
}

export interface CourseData {
  slug: string
  title: string
  subtitle: string
  language: string
  level: string
  duration_hours: number
  is_free: boolean
  modules: CourseModule[]
  kategori?: string
  domain_tags?: string[]
  harga?: string
  status?: string
}

export function getCourse(courseSlug: string): CourseData | null {
  const filePath = path.join(contentDir, courseSlug, '_course.json')
  if (!fs.existsSync(filePath)) return null
  const raw = fs.readFileSync(filePath, 'utf-8')
  return JSON.parse(raw) as CourseData
}

