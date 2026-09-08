import type { CourseDetailView } from "@codeintex/learning-ui";

const DEFAULT_API_BASE_URL =
  "http" + "://" + "127.0.0.1:8000";

export async function getCourseDetail(
  slug: string,
): Promise<CourseDetailView> {
  const apiBaseUrl =
    process.env.LEARNING_API_BASE_URL ?? DEFAULT_API_BASE_URL;

  const response = await fetch(
    `${apiBaseUrl}/api/v1/courses/${slug}/`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      `Learning API course request failed: ${response.status}`,
    );
  }

  const data: unknown = await response.json();

  if (
    !data ||
    typeof data !== "object" ||
    !("release" in data) ||
    !("outcomes" in data) ||
    !Array.isArray(data.outcomes)
  ) {
    throw new Error(
      "Learning API returned an invalid course payload.",
    );
  }

  return data as CourseDetailView;
}
