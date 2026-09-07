import type {
  CourseReleaseView,
  LearningPlayerState,
  LessonContentView,
} from "@codeintex/learning-ui";

export const backendCourseRelease: CourseReleaseView = {
  id: "release_backend_001",
  courseId: "course_backend_engineering",
  release: 1,
  title: "Backend Engineering Foundations",
  modules: [
    {
      id: "module_01",
      title: "Web & API Foundations",
      items: [
        {
          id: "lesson_http",
          kind: "lesson",
          title: "How HTTP actually moves",
          durationMinutes: 12,
          completed: true,
        },
        {
          id: "lesson_rest",
          kind: "lesson",
          title: "Designing resource-oriented APIs",
          durationMinutes: 16,
          completed: true,
        },
      ],
    },
    {
      id: "module_02",
      title: "Trust Boundaries",
      items: [
        {
          id: "lesson_auth",
          kind: "lesson",
          title: "Authentication & authorization",
          durationMinutes: 18,
          completed: false,
          current: true,
        },
        {
          id: "lesson_sessions",
          kind: "lesson",
          title: "Sessions, tokens, and revocation",
          durationMinutes: 15,
          completed: false,
        },
        {
          id: "quiz_auth",
          kind: "quiz",
          title: "Trust boundary checkpoint",
          durationMinutes: 8,
          completed: false,
        },
      ],
    },
    {
      id: "module_03",
      title: "Production Discipline",
      items: [
        {
          id: "lesson_testing",
          kind: "lesson",
          title: "Testing contracts, not implementation",
          durationMinutes: 20,
          completed: false,
        },
        {
          id: "project_api",
          kind: "project",
          title: "Production API capstone",
          completed: false,
        },
      ],
    },
  ],
};

export const backendInitialState: LearningPlayerState = {
  currentItemId: "lesson_auth",
};

const fallbackSections: LessonContentView["sections"] = [
  {
    heading: "Why this matters",
    body:
      "The fixture layer exists only at the data boundary. Product components consume a release-shaped contract so a real Django API can replace fixtures without rewriting the learner experience.",
  },
];

export const backendLessons: Record<string, LessonContentView> = {
  lesson_http: {
    itemId: "lesson_http",
    eyebrow: "MODULE 01 · LESSON 01",
    title: "How HTTP actually moves",
    summary:
      "Build a concrete mental model for requests, responses, intermediaries, and failure before designing an API.",
    sections: [
      {
        heading: "Start with the boundary",
        body:
          "A browser does not call your database. It crosses a sequence of trust and transport boundaries. Good backend design begins by identifying those boundaries explicitly.",
      },
      {
        heading: "Request as a contract",
        body:
          "Treat method, target, headers, and body as a contract between independently evolving systems.",
        code:
          "GET /v1/courses/backend-engineering\nAccept: application/json",
      },
    ],
  },
  lesson_rest: {
    itemId: "lesson_rest",
    eyebrow: "MODULE 01 · LESSON 02",
    title: "Designing resource-oriented APIs",
    summary:
      "Turn product language into stable resources and operations without leaking database structure.",
    sections: [
      {
        heading: "Domain language first",
        body:
          "An API contract should speak in learner and product concepts, not table names or framework internals.",
      },
    ],
  },
  lesson_auth: {
    itemId: "lesson_auth",
    eyebrow: "MODULE 02 · LESSON 01",
    title: "Authentication & authorization",
    summary:
      "Separate identity from permission so security rules remain clear as the platform grows.",
    sections: [
      {
        heading: "Authentication answers one question",
        body:
          "Authentication establishes who is making the request. It should not silently decide everything that identity is allowed to do.",
      },
      {
        heading: "Authorization is contextual",
        body:
          "The same identity may be a learner in Learning, an author in Research, and a client in Services. Each product owns its authorization policy.",
        code:
          'identity = authenticate(request)\nauthorize(identity, action="course:learn", resource=course)',
      },
      {
        heading: "Make the server authoritative",
        body:
          "The browser can request a privileged action, but the server validates identity, entitlement, ownership, and policy before changing canonical state.",
      },
    ],
  },
  lesson_sessions: {
    itemId: "lesson_sessions",
    eyebrow: "MODULE 02 · LESSON 02",
    title: "Sessions, tokens, and revocation",
    summary:
      "Choose session mechanics based on trust boundaries rather than framework fashion.",
    sections: [
      {
        heading: "Start from failure modes",
        body:
          "Ask how credentials expire, how a compromised session is revoked, and which system is authoritative before choosing a token format.",
      },
    ],
  },
  quiz_auth: {
    itemId: "quiz_auth",
    eyebrow: "MODULE 02 · CHECKPOINT",
    title: "Trust boundary checkpoint",
    summary:
      "Validate the distinction between identity, authorization, session state, and server authority.",
    sections: fallbackSections,
  },
  lesson_testing: {
    itemId: "lesson_testing",
    eyebrow: "MODULE 03 · LESSON 01",
    title: "Testing contracts, not implementation",
    summary:
      "Protect behavior that matters to users and integrations while keeping implementation replaceable.",
    sections: [
      {
        heading: "Test the promise",
        body:
          "A durable test asserts observable behavior and domain invariants, not every internal function call.",
      },
    ],
  },
  project_api: {
    itemId: "project_api",
    eyebrow: "MODULE 03 · PROJECT",
    title: "Production API capstone",
    summary:
      "Apply the release contract, authorization boundary, and test discipline in one production-oriented project.",
    sections: fallbackSections,
  },
};
