import { redirect } from "next/navigation";

import { getLearnerProgress } from "../../../src/data/learner-progress";
import { getPlayerContent } from "../../../src/data/player-content";
import { PersistentLearningPlayer } from "./persistent-learning-player";

export const dynamic = "force-dynamic";

type LearningPageProps = {
  params: Promise<{
    courseSlug: string;
  }>;
};

export default async function LearningPage({
  params,
}: LearningPageProps) {
  const { courseSlug } = await params;

  const progressResult =
    await getLearnerProgress(courseSlug);

  if (
    progressResult.status ===
    "unauthenticated"
  ) {
    redirect(
      `/login?next=${encodeURIComponent(
        `/learn/${courseSlug}`,
      )}`,
    );
  }

  if (
    progressResult.status ===
    "not-enrolled"
  ) {
    redirect(
      `/courses/${courseSlug}`,
    );
  }

  const progress =
    progressResult.progress;

  const player =
    await getPlayerContent(
      courseSlug,
      progress.releaseId,
    );

  if (
    player.release.id !==
    progress.releaseId
  ) {
    throw new Error(
      "Player content release does not match learner enrollment.",
    );
  }

  const completedIds = new Set(
    progress.completedItemIds,
  );

  const release = {
    ...player.release,
    modules: player.release.modules.map(
      (module) => ({
        ...module,
        items: module.items.map(
          (item) => ({
            ...item,
            completed:
              completedIds.has(item.id),
            current:
              item.id ===
              progress.currentItemId,
          }),
        ),
      }),
    ),
  };

  return (
    <PersistentLearningPlayer
      courseSlug={courseSlug}
      courseHref={`/courses/${courseSlug}`}
      release={release}
      initialState={{
        currentItemId:
          progress.currentItemId ??
          player.initialState.currentItemId,
      }}
      initialProgressPercent={
        progress.progressPercent
      }
      lessonByItemId={
        player.lessonByItemId
      }
    />
  );
}
