import { Progress } from "@codeintex/ui-primitives";
import type {
  MyLearningCourseView,
  MyLearningView,
} from "./types";

type MyLearningProps = {
  learning: MyLearningView;
};

type CourseSectionProps = {
  id: string;
  title: string;
  courses: MyLearningCourseView[];
};

function CourseCard({
  course,
}: {
  course: MyLearningCourseView;
}) {
  return (
    <article className="ml-course">
      <div className="ml-course__main">
        <div className="ml-kicker">{course.kicker}</div>
        <h3>{course.title}</h3>
        <p className="ml-course__summary">
          {course.summary}
        </p>

        <div className="ml-course__progress">
          <Progress
            value={course.progressPercent}
            label="Course progress"
          />
          <span className="ml-course__progress-meta">
            {course.completedItems} of {course.totalItems} lessons complete
          </span>
        </div>
      </div>

      <div className="ml-course__resume">
        {course.status === "in-progress" ? (
          <>
            <div className="ml-resume-label">
              CURRENT LESSON
            </div>
            <strong>{course.currentItemTitle}</strong>
            <span className="ml-resume-module">
              {course.currentModuleTitle}
            </span>
          </>
        ) : course.status === "completed" ? (
          <>
            <div className="ml-resume-label">
              STATUS
            </div>
            <strong>Course complete</strong>
            <span className="ml-resume-module">
              All lessons completed
            </span>
          </>
        ) : (
          <>
            <div className="ml-resume-label">
              STATUS
            </div>
            <strong>No lessons available</strong>
            <span className="ml-resume-module">
              This course does not currently contain lessons.
            </span>
          </>
        )}

        <div className="ml-actions">
          {course.status === "in-progress" ? (
            <a
              className="ml-action ml-action--primary"
              href={course.resumeHref}
            >
              Resume learning →
            </a>
          ) : null}

          <a
            className="ml-action ml-action--secondary"
            href={course.detailHref}
          >
            Course details
          </a>
        </div>
      </div>
    </article>
  );
}

function CourseSection({
  id,
  title,
  courses,
}: CourseSectionProps) {
  return (
    <section
      className="ml-section"
      aria-labelledby={id}
    >
      <div className="ml-section__heading">
        <h2 id={id}>{title}</h2>
        <span>
          {courses.length}{" "}
          {courses.length === 1 ? "course" : "courses"}
        </span>
      </div>

      <div className="ml-course-list">
        {courses.map((course) => (
          <CourseCard
            course={course}
            key={course.id}
          />
        ))}
      </div>
    </section>
  );
}

export function MyLearning({
  learning,
}: MyLearningProps) {
  const inProgressCourses = learning.courses.filter(
    (course) => course.status === "in-progress",
  );
  const completedCourses = learning.courses.filter(
    (course) => course.status === "completed",
  );
  const noContentCourses = learning.courses.filter(
    (course) => course.status === "no-content",
  );

  return (
    <div className="my-learning">
      <header className="ml-topbar">
        <a className="ml-brand" href="/">
          <span
            className="ml-brand__mark"
            aria-hidden="true"
          >
            CI
          </span>
          <span>CodeInteX Learning</span>
        </a>
        <span className="ml-topbar__context">
          My Learning
        </span>
      </header>

      <main className="ml-shell">
        <header className="ml-intro">
          <div className="ml-kicker">
            LEARNER HOME
          </div>
          <h1>Your learning, at a glance.</h1>
          <p>
            Your courses, progress, and next action.
          </p>
        </header>

        {inProgressCourses.length > 0 ||
        learning.courses.length === 0 ? (
          <CourseSection
            id="in-progress-title"
            title="In progress"
            courses={inProgressCourses}
          />
        ) : null}

        {completedCourses.length > 0 ? (
          <CourseSection
            id="completed-title"
            title="Completed"
            courses={completedCourses}
          />
        ) : null}

        {noContentCourses.length > 0 ? (
          <CourseSection
            id="no-content-title"
            title="No lessons"
            courses={noContentCourses}
          />
        ) : null}
      </main>
    </div>
  );
}
