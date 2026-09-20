"use client";

import { LearningPlayer } from "@codeintex/learning-ui";
import type { LearningProgressView } from "@codeintex/learning-ui";
import type { ComponentProps } from "react";

type LearningPlayerProps = ComponentProps<typeof LearningPlayer>;

type PersistentLearningPlayerProps = Omit<
  LearningPlayerProps,
  "onComplete"
> & {
  courseSlug: string;
};

type CsrfResponse = {
  csrfToken: string;
};

function isRecord(
  value: unknown,
): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function parseCompletionProgress(
  payload: unknown,
): LearningProgressView {
  if (!isRecord(payload) || !isRecord(payload.progress)) {
    throw new Error(
      "Progress update returned an invalid response.",
    );
  }

  const progress = payload.progress;
  const completedItemIds = progress.completedItemIds;
  const progressPercent = progress.progressPercent;
  const currentItemId = progress.currentItemId;

  if (
    !Array.isArray(completedItemIds) ||
    !completedItemIds.every(
      (itemId) => typeof itemId === "string",
    ) ||
    typeof progressPercent !== "number" ||
    !Number.isFinite(progressPercent) ||
    progressPercent < 0 ||
    progressPercent > 100 ||
    (
      currentItemId !== null &&
      typeof currentItemId !== "string"
    )
  ) {
    throw new Error(
      "Progress update returned an invalid response.",
    );
  }

  return {
    completedItemIds,
    progressPercent,
    currentItemId,
  };
}

export function PersistentLearningPlayer({
  courseSlug,
  ...playerProps
}: PersistentLearningPlayerProps) {
  async function completeLesson(itemId: string) {
    const csrfResponse = await fetch("/api/v1/auth/csrf/", {
      cache: "no-store",
      credentials: "same-origin",
    });

    if (!csrfResponse.ok) {
      throw new Error("Could not initialize progress update.");
    }

    const { csrfToken } =
      (await csrfResponse.json()) as CsrfResponse;

    const response = await fetch(
      `/api/v1/courses/${courseSlug}/lessons/${itemId}/complete/`,
      {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "X-CSRFToken": csrfToken,
        },
      },
    );

    if (response.status === 401) {
      window.location.assign("/login");
      throw new Error("Authentication required.");
    }

    if (!response.ok) {
      throw new Error(
        `Progress update failed: ${response.status}`,
      );
    }

    const payload: unknown = await response.json();

    return parseCompletionProgress(payload);
  }

  return (
    <LearningPlayer
      {...playerProps}
      onComplete={completeLesson}
    />
  );
}
