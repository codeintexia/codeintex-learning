import type {
  CourseReleaseView,
  LearningPlayerState,
  LessonContentView,
} from "@codeintex/learning-ui";

type PlayerContentItem = {
  id: string;
  kind: "lesson";
  title: string;
  durationMinutes?: number;
};

type PlayerContentModule = {
  id: string;
  title: string;
  items: PlayerContentItem[];
};

type PlayerContentPayload = {
  release: {
    id: string;
    courseId: string;
    release: number;
    title: string;
    modules: PlayerContentModule[];
  };
  lessons: Record<string, LessonContentView>;
};

type LearningPlayerData = {
  release: CourseReleaseView;
  initialState: LearningPlayerState;
  lessonByItemId: Record<string, LessonContentView>;
};

const DEFAULT_API_BASE_URL =
  "http" + "://" + "127.0.0.1:8000";

export async function getPlayerContent(
  slug: string,
  releaseId?: string,
): Promise<LearningPlayerData> {
  const apiBaseUrl =
    process.env.LEARNING_API_BASE_URL ?? DEFAULT_API_BASE_URL;

  const releaseQuery = releaseId
    ? `?releaseId=${encodeURIComponent(releaseId)}`
    : "";

  const response = await fetch(
    `${apiBaseUrl}/api/v1/courses/${slug}/player/${releaseQuery}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      `Learning API player request failed: ${response.status}`,
    );
  }

  const data: unknown = await response.json();

  if (
    !data ||
    typeof data !== "object" ||
    !("release" in data) ||
    !("lessons" in data)
  ) {
    throw new Error(
      "Learning API returned an invalid player payload.",
    );
  }

  const payload = data as PlayerContentPayload;

  const release: CourseReleaseView = {
    ...payload.release,
    modules: payload.release.modules.map((module) => ({
      ...module,
      items: module.items.map((item) => ({
        ...item,
        completed: false,
      })),
    })),
  };

  const firstItem = release.modules
    .flatMap((module) => module.items)
    .at(0);

  if (!firstItem) {
    throw new Error(
      "Learning API returned a course with no playable items.",
    );
  }

  return {
    release,
    initialState: {
      currentItemId: firstItem.id,
    },
    lessonByItemId: payload.lessons,
  };
}
