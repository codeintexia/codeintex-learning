import { LearningPlayer } from "@codeintex/learning-ui";
import {
  backendCourseRelease,
  backendInitialState,
  backendLessons,
} from "../../../src/fixtures/backend-engineering-course";

export default function BackendEngineeringPlayerPage() {
  return (
    <LearningPlayer
      release={backendCourseRelease}
      initialState={backendInitialState}
      lessonByItemId={backendLessons}
    />
  );
}
