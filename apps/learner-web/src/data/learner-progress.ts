import { cookies } from "next/headers";

const learningApiBaseUrl =
  process.env.LEARNING_API_BASE_URL ??
  ("http" + "://" + "127.0.0.1:8000");

export type LearnerProgress = {
  enrollmentId: string;
  releaseId: string;
  release: number;
  completedItemIds: string[];
  completedItems: number;
  totalItems: number;
  progressPercent: number;
  currentItemId: string | null;
};

export type LearnerProgressResult =
  | {
      status: "ok";
      progress: LearnerProgress;
    }
  | {
      status: "unauthenticated";
    }
  | {
      status: "not-enrolled";
    };

export async function getLearnerProgress(
  courseSlug: string,
): Promise<LearnerProgressResult> {
  const cookieStore = await cookies();
  const sessionId = cookieStore.get("sessionid")?.value;

  if (!sessionId) {
    return { status: "unauthenticated" };
  }

  const response = await fetch(
    `${learningApiBaseUrl}/api/v1/courses/${encodeURIComponent(
      courseSlug,
    )}/progress/`,
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

  if (response.status === 404) {
    return { status: "not-enrolled" };
  }

  if (!response.ok) {
    throw new Error(
      `Learning progress request failed: ${response.status}`,
    );
  }

  const payload = (await response.json()) as {
    progress: LearnerProgress;
  };

  return {
    status: "ok",
    progress: payload.progress,
  };
}
