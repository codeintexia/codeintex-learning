import type { Metadata } from "next";
import { CourseDetail } from "@codeintex/learning-ui";
import { getCourseDetail } from "../../../src/data/course-detail";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Backend Engineering Foundations | CodeInteX Learning",
  description:
    "Learn HTTP, API contracts, authentication, sessions, and production testing through first-principles backend engineering.",
};

export default async function BackendEngineeringCoursePage() {
  const course = await getCourseDetail("backend-engineering");

  return <CourseDetail course={course} />;
}
