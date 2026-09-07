import type { CourseCatalogView } from "@codeintex/learning-ui";
import { backendCourseDetail } from "./backend-engineering-course-detail";

const release = backendCourseDetail.release;
const items = release.modules.flatMap((module) => module.items);

export const courseCatalog: CourseCatalogView = {
  courses: [
    {
      id: release.courseId,
      subject: backendCourseDetail.kicker,
      title: release.title,
      summary: backendCourseDetail.summary,
      level: backendCourseDetail.level,
      moduleCount: release.modules.length,
      lessonCount: items.length,
      durationMinutes: items.reduce(
        (total, item) => total + (item.durationMinutes ?? 0),
        0,
      ),
      href: "/courses/backend-engineering",
    },
  ],
};
