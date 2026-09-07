import type { Metadata } from "next";
import { CourseDetail } from "@codeintex/learning-ui";
import { backendCourseDetail } from "../../../src/fixtures/backend-engineering-course-detail";

export const metadata: Metadata = {
  title: "Backend Engineering Foundations | CodeInteX Learning",
  description:
    "Learn HTTP, API contracts, authentication, sessions, and production testing through first-principles backend engineering.",
};

export default function BackendEngineeringCoursePage() {
  return <CourseDetail course={backendCourseDetail} />;
}
