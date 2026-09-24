import type {
  Meta,
  StoryObj,
} from "@storybook/nextjs-vite";

import {
  MyLearning,
} from "@codeintex/learning-ui";

import type {
  MyLearningCourseView,
  MyLearningView,
} from "@codeintex/learning-ui";

const inProgressCourse = {
  id: "backend-engineering",
  status: "in-progress",
  kicker: "Software Engineering",
  title: "Backend Engineering",
  summary:
    "Build reliable backend systems with explicit contracts, durable state, and production-oriented engineering practices.",
  progressPercent: 40,
  completedItems: 2,
  totalItems: 5,
  currentItemTitle: "Designing Runtime Boundaries",
  currentModuleTitle: "Module 2 · Application Runtime",
  resumeHref: "/learn/backend-engineering",
  detailHref: "/courses/backend-engineering",
} satisfies MyLearningCourseView;

const completedCourse = {
  id: "backend-engineering-completed",
  status: "completed",
  kicker: "Software Engineering",
  title: "Backend Engineering",
  summary:
    "Build reliable backend systems with explicit contracts, durable state, and production-oriented engineering practices.",
  progressPercent: 100,
  completedItems: 5,
  totalItems: 5,
  detailHref: "/courses/backend-engineering",
} satisfies MyLearningCourseView;

const noContentCourse = {
  id: "systems-foundations",
  status: "no-content",
  kicker: "Computer Science",
  title: "Systems Foundations",
  summary:
    "A future course whose learner-visible release does not currently contain lessons.",
  progressPercent: 0,
  completedItems: 0,
  totalItems: 0,
  detailHref: "/courses/systems-foundations",
} satisfies MyLearningCourseView;

const meta = {
  title: "Learning/My Learning",
  component: MyLearning,
} satisfies Meta<typeof MyLearning>;

export default meta;

type Story = StoryObj<typeof meta>;

function view(
  courses: MyLearningCourseView[],
): MyLearningView {
  return { courses };
}

export const InProgress = {
  args: {
    learning: view([inProgressCourse]),
  },
} satisfies Story;

export const Completed = {
  args: {
    learning: view([completedCourse]),
  },
} satisfies Story;

export const Mixed = {
  args: {
    learning: view([
      inProgressCourse,
      completedCourse,
      noContentCourse,
    ]),
  },
} satisfies Story;

export const NoContent = {
  args: {
    learning: view([noContentCourse]),
  },
} satisfies Story;
