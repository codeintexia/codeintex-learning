export type CatalogCourseView = {
  id: string;
  subject: string;
  title: string;
  summary: string;
  level: string;
  moduleCount: number;
  lessonCount: number;
  durationMinutes: number;
  href: string;
};

export type CourseCatalogView = {
  courses: CatalogCourseView[];
};
