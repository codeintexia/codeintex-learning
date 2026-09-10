import { redirect } from "next/navigation";

import { getLearnerProgress } from "../../../src/data/learner-progress";
import { getPlayerContent } from "../../../src/data/player-content";
import { PersistentLearningPlayer } from "./persistent-learning-player";

export const dynamic = "force-dynamic";

export default async function BackendEngineeringPlayerPage() {
  const courseSlug = "backend-engineering";

  const progressResult =
    await getLearnerProgress(courseSlug);

  if (progressResult.status === "unauthenticated") {
    redirect("/login");
  }

  if (progressResult.status === "not-enrolled") {
    redirect(`/courses/${courseSlug}`);
  }

  const progress = progressResult.progress;

  const player = await getPlayerContent(
    courseSlug,
    progress.releaseId,
  );

  if (player.release.id !== progress.releaseId) {
    throw new Error(
      "Player content release does not match learner enrollment.",
    );
  }

  const completedIds = new Set(
    progress.completedItemIds,
  );

  const release = {
    ...player.release,
    modules: player.release.modules.map((module) => ({
      ...module,
      items: module.items.map((item) => ({
        ...item,
        completed: completedIds.has(item.id),
        current: item.id === progress.currentItemId,
      })),
    })),
  };

  return (
    <PersistentLearningPlayer
      courseSlug={courseSlug}
      release={release}
      initialState={{
        currentItemId:
          progress.currentItemId ??
          player.initialState.currentItemId,
      }}
      lessonByItemId={player.lessonByItemId}
    />
  );
}
