import type { CourseCatalogView } from "@codeintex/learning-ui";

const DEFAULT_API_BASE_URL = "http://127.0.0.1:8000";

export async function getCourseCatalog(): Promise<CourseCatalogView> {
  const apiBaseUrl =
    process.env.LEARNING_API_BASE_URL ?? DEFAULT_API_BASE_URL;

  const response = await fetch(
    `${apiBaseUrl}/api/v1/catalog/`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      `Learning API catalog request failed: ${response.status}`,
    );
  }

  const data: unknown = await response.json();

  if (
    !data ||
    typeof data !== "object" ||
    !("courses" in data) ||
    !Array.isArray(data.courses)
  ) {
    throw new Error("Learning API returned an invalid catalog payload.");
  }

  return data as CourseCatalogView;
}
