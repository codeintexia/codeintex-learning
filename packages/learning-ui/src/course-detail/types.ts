import type { CourseReleaseView } from "../learning-player/types";

export type CourseDetailView = {
  release: CourseReleaseView;
  kicker: string;
  summary: string;
  level: string;
  outcomes: string[];
  audience: string;
  primaryAction: {
    label: string;
    href: string;
  };
};
