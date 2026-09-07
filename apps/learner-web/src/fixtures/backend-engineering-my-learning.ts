import type { MyLearningView } from "@codeintex/learning-ui";
import {
  backendCourseRelease,
  backendInitialState,
} from "./backend-engineering-course";

const items = backendCourseRelease.modules.flatMap((module) =>
  module.items.map((item) => ({
    ...item,
    moduleTitle: module.title,
  })),
);

const completedItems = items.filter((item) => item.completed).length;

const currentItem =
  items.find((item) => item.id === backendInitialState.currentItemId) ??
  items[0];

export const backendMyLearning: MyLearningView = {
  courses: [
    {
      id: backendCourseRelease.courseId,
      kicker: "BACKEND ENGINEERING",
      title: backendCourseRelease.title,
      summary:
        "Build clear mental models for HTTP, API contracts, identity boundaries, sessions, and production testing.",
      progressPercent: Math.round(
        (completedItems / items.length) * 100,
      ),
      completedItems,
      totalItems: items.length,
      currentItemTitle: currentItem.title,
      currentModuleTitle: currentItem.moduleTitle,
      resumeHref: "/learn/backend-engineering",
      detailHref: "/courses/backend-engineering",
    },
  ],
};
