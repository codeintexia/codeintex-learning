import type {
  Meta,
  StoryObj,
} from "@storybook/nextjs-vite";

import {
  LearningPlayer,
} from "@codeintex/learning-ui";

import type {
  CourseReleaseView,
  LearningProgressView,
  LessonContentView,
} from "@codeintex/learning-ui";

const release = {
  id: "release-backend-engineering-1",
  courseId: "backend-engineering",
  release: 1,
  title: "Backend Engineering",
  modules: [
    {
      id: "module-runtime",
      title: "Application Runtime",
      items: [
        {
          id: "lesson-runtime-boundaries",
          kind: "lesson",
          title: "Designing Runtime Boundaries",
          durationMinutes: 12,
          completed: false,
          current: true,
        },
        {
          id: "lesson-durable-state",
          kind: "lesson",
          title: "Durable Application State",
          durationMinutes: 15,
          completed: false,
        },
      ],
    },
  ],
} satisfies CourseReleaseView;

const partiallyCompletedRelease = {
  ...release,
  modules: [
    {
      ...release.modules[0],
      items: [
        {
          ...release.modules[0].items[0],
          completed: true,
          current: false,
        },
        {
          ...release.modules[0].items[1],
          completed: false,
          current: true,
        },
      ],
    },
  ],
} satisfies CourseReleaseView;

const lessonByItemId = {
  "lesson-runtime-boundaries": {
    itemId: "lesson-runtime-boundaries",
    eyebrow: "Lesson 1",
    title: "Designing Runtime Boundaries",
    summary:
      "Separate domain authority from runtime presentation so each layer can evolve without duplicating business semantics.",
    sections: [
      {
        heading: "Define the boundary",
        body:
          "A runtime boundary should make ownership explicit. Domain state belongs to the authoritative backend; the learner client consumes a stable contract.",
      },
      {
        heading: "Prefer explicit contracts",
        body:
          "Avoid allowing implementation-specific structures to leak into learner-facing components.",
        code:
          "domain → API contract → adapter → learner UI",
      },
    ],
  },
  "lesson-durable-state": {
    itemId: "lesson-durable-state",
    eyebrow: "Lesson 2",
    title: "Durable Application State",
    summary:
      "Persist consequential learner state on the server and treat browser state as presentation context.",
    sections: [
      {
        heading: "Durability first",
        body:
          "Completion and progression must survive refreshes, new sessions, and different client devices.",
      },
    ],
  },
} satisfies Record<string, LessonContentView>;

const meta = {
  title: "Learning/Learning Player",
  component: LearningPlayer,
  parameters: {
    layout: "fullscreen",
  },
} satisfies Meta<typeof LearningPlayer>;

export default meta;

type Story = StoryObj<typeof meta>;

const noOpCompletion = async (
  itemId: string,
): Promise<LearningProgressView> => ({
  completedItemIds: [],
  progressPercent: 0,
  currentItemId: itemId,
});

export const Initial = {
  args: {
    courseHref: "/courses/backend-engineering",
    release,
    initialState: {
      currentItemId: "lesson-runtime-boundaries",
    },
    initialProgressPercent: 0,
    lessonByItemId,
    onComplete: noOpCompletion,
  },
} satisfies Story;

export const PartiallyCompleted = {
  args: {
    courseHref: "/courses/backend-engineering",
    release: partiallyCompletedRelease,
    initialState: {
      currentItemId: "lesson-durable-state",
    },
    initialProgressPercent: 50,
    lessonByItemId,
    onComplete: async (): Promise<LearningProgressView> => ({
      completedItemIds: [
        "lesson-runtime-boundaries",
        "lesson-durable-state",
      ],
      progressPercent: 100,
      currentItemId: "lesson-durable-state",
    }),
  },
} satisfies Story;

export const CompletionTransition = {
  args: {
    courseHref: "/courses/backend-engineering",
    release,
    initialState: {
      currentItemId: "lesson-runtime-boundaries",
    },
    initialProgressPercent: 0,
    lessonByItemId,
    onComplete: async (): Promise<LearningProgressView> => ({
      completedItemIds: [
        "lesson-runtime-boundaries",
      ],
      progressPercent: 50,
      currentItemId: "lesson-durable-state",
    }),
  },
} satisfies Story;
