export type MyLearningCourseView = {
  id: string;
  kicker: string;
  title: string;
  summary: string;
  progressPercent: number;
  completedItems: number;
  totalItems: number;
  currentItemTitle: string;
  currentModuleTitle: string;
  resumeHref: string;
  detailHref: string;
};

export type MyLearningView = {
  courses: MyLearningCourseView[];
};
