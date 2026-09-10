"use client";

import { LearningPlayer } from "@codeintex/learning-ui";
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
  }

  return (
    <LearningPlayer
      {...playerProps}
      onComplete={completeLesson}
    />
  );
}
