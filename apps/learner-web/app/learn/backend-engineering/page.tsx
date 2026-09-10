import { LearningPlayer } from "@codeintex/learning-ui";

import { getPlayerContent } from "../../../src/data/player-content";

export const dynamic = "force-dynamic";

export default async function BackendEngineeringPlayerPage() {
  const player = await getPlayerContent("backend-engineering");

  return (
    <LearningPlayer
      release={player.release}
      initialState={player.initialState}
      lessonByItemId={player.lessonByItemId}
    />
  );
}
