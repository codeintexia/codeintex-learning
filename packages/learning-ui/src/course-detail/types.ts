export type CourseDetailItemView = {
  id: string;
  kind: "lesson" | "quiz" | "project";
  title: string;
  durationMinutes?: number;
};

export type CourseDetailModuleView = {
  id: string;
  title: string;
  items: CourseDetailItemView[];
};

export type CourseDetailReleaseView = {
  id: string;
  courseId: string;
  release: number;
  title: string;
  modules: CourseDetailModuleView[];
};

export type CourseDetailView = {
  release: CourseDetailReleaseView;
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
