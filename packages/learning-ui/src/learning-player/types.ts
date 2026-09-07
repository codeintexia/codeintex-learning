export type LearningItemKind = "lesson" | "quiz" | "project";

export type CurriculumItemView = {
  id: string;
  kind: LearningItemKind;
  title: string;
  durationMinutes?: number;
  completed: boolean;
  current?: boolean;
};

export type CurriculumModuleView = {
  id: string;
  title: string;
  items: CurriculumItemView[];
};

export type CourseReleaseView = {
  id: string;
  courseId: string;
  release: number;
  title: string;
  modules: CurriculumModuleView[];
};

export type LessonContentView = {
  itemId: string;
  eyebrow: string;
  title: string;
  summary: string;
  sections: Array<{
    heading?: string;
    body: string;
    code?: string;
  }>;
};

export type LearningPlayerState = {
  currentItemId: string;
};
