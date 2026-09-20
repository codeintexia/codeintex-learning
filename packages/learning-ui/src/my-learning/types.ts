type MyLearningCourseBaseView = {
  id: string;
  kicker: string;
  title: string;
  summary: string;
  progressPercent: number;
  completedItems: number;
  totalItems: number;
  detailHref: string;
};

export type MyLearningCourseView =
  | (MyLearningCourseBaseView & {
      status: "in-progress";
      currentItemTitle: string;
      currentModuleTitle: string;
      resumeHref: string;
    })
  | (MyLearningCourseBaseView & {
      status: "completed";
    })
  | (MyLearningCourseBaseView & {
      status: "no-content";
    });

export type MyLearningView = {
  courses: MyLearningCourseView[];
};
