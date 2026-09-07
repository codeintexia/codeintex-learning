import type { CourseDetailView } from "@codeintex/learning-ui";
import { backendCourseRelease } from "./backend-engineering-course";

export const backendCourseDetail: CourseDetailView = {
  release: backendCourseRelease,
  kicker: "BACKEND ENGINEERING",
  summary:
    "Learn how reliable backend systems actually behave—from HTTP and API contracts to identity boundaries, sessions, and production testing.",
  level: "Foundation",
  outcomes: [
    "Model HTTP requests, responses, and trust boundaries clearly.",
    "Design APIs around stable product contracts instead of database structure.",
    "Separate authentication, authorization, sessions, and server authority.",
    "Choose session mechanics from failure modes and revocation requirements.",
    "Test observable contracts without coupling tests to implementation details.",
  ],
  audience:
    "Developers who want to move beyond framework recipes and reason confidently about production backend systems.",
  primaryAction: {
    label: "Start course",
    href: "/learn/backend-engineering",
  },
};
