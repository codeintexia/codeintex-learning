import type {
  MyLearningCourseView,
  MyLearningView,
} from "@codeintex/learning-ui";
import { cookies } from "next/headers";

const learningApiBaseUrl =
  process.env.LEARNING_API_BASE_URL ??
  ("http" + "://" + "127.0.0.1:8000");

type MyLearningApiCourse = {
  courseId: string;
  courseSlug: string;
  subject: string;
  releaseId: string;
  release: number;
  title: string;
  summary: string;
  progress: {
    completedItems: number;
    totalItems: number;
    progressPercent: number;
    currentItemId: string | null;
  };
  current: {
    itemId: string;
    itemTitle: string;
    moduleTitle: string;
  } | null;
};

type MyLearningApiResponse = {
  courses: MyLearningApiCourse[];
};

function mapMyLearningCourse(
  course: MyLearningApiCourse,
): MyLearningCourseView {
  const common = {
    id: course.courseId,
    kicker: course.subject,
    title: course.title,
    summary: course.summary,
    progressPercent: course.progress.progressPercent,
    completedItems: course.progress.completedItems,
    totalItems: course.progress.totalItems,
    detailHref: `/courses/${course.courseSlug}`,
  };

  if (course.progress.totalItems === 0) {
    return {
      ...common,
      status: "no-content",
    };
  }

  if (
    course.progress.completedItems ===
    course.progress.totalItems
  ) {
    return {
      ...common,
      status: "completed",
    };
  }

  if (!course.current) {
    throw new Error(
      "My Learning response is missing a current lesson for an incomplete course.",
    );
  }

  return {
    ...common,
    status: "in-progress",
    currentItemTitle: course.current.itemTitle,
    currentModuleTitle: course.current.moduleTitle,
    resumeHref: `/learn/${course.courseSlug}`,
  };
}

export type MyLearningResult =
  | {
      status: "ok";
      learning: MyLearningView;
    }
  | {
      status: "unauthenticated";
    };

export async function getMyLearning(): Promise<MyLearningResult> {
  const cookieStore = await cookies();
  const sessionId = cookieStore.get("sessionid")?.value;

  if (!sessionId) {
    return { status: "unauthenticated" };
  }

  const response = await fetch(
    `${learningApiBaseUrl}/api/v1/my-learning/`,
    {
      cache: "no-store",
      headers: {
        Cookie: `sessionid=${sessionId}`,
      },
    },
  );

  if (response.status === 401) {
    return { status: "unauthenticated" };
  }

  if (!response.ok) {
    throw new Error(
      `My Learning request failed: ${response.status}`,
    );
  }

  const payload =
    (await response.json()) as MyLearningApiResponse;

  return {
    status: "ok",
    learning: {
      courses: payload.courses.map(mapMyLearningCourse),
    },
  };
}
