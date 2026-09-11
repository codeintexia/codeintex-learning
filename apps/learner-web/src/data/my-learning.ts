import type { MyLearningView } from "@codeintex/learning-ui";
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
      courses: payload.courses.map((course) => ({
        id: course.courseId,
        kicker: course.subject,
        title: course.title,
        summary: course.summary,
        progressPercent: course.progress.progressPercent,
        completedItems: course.progress.completedItems,
        totalItems: course.progress.totalItems,
        currentItemTitle:
          course.current?.itemTitle ?? "Course complete",
        currentModuleTitle:
          course.current?.moduleTitle ?? "Completed",
        resumeHref: `/learn/${course.courseSlug}`,
        detailHref: `/courses/${course.courseSlug}`,
      })),
    },
  };
}
