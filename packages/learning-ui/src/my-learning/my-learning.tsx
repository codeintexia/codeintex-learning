import { Progress } from "@codeintex/ui-primitives";
import type { MyLearningView } from "./types";

type MyLearningProps = {
  learning: MyLearningView;
};

export function MyLearning({ learning }: MyLearningProps) {
  return (
    <div className="my-learning">
      <header className="ml-topbar">
        <a className="ml-brand" href="/">
          <span className="ml-brand__mark" aria-hidden="true">
            CI
          </span>
          <span>CodeInteX Learning</span>
        </a>

        <span className="ml-topbar__context">My Learning</span>
      </header>

      <main className="ml-shell">
        <header className="ml-intro">
          <div className="ml-kicker">LEARNER HOME</div>
          <h1>Continue where you left off.</h1>
          <p>
            Your active courses, current position, and next action—without
            dashboard noise.
          </p>
        </header>

        <section className="ml-section" aria-labelledby="in-progress-title">
          <div className="ml-section__heading">
            <h2 id="in-progress-title">In progress</h2>
            <span>
              {learning.courses.length}{" "}
              {learning.courses.length === 1 ? "course" : "courses"}
            </span>
          </div>

          <div className="ml-course-list">
            {learning.courses.map((course) => (
              <article className="ml-course" key={course.id}>
                <div className="ml-course__main">
                  <div className="ml-kicker">{course.kicker}</div>

                  <h3>{course.title}</h3>

                  <p className="ml-course__summary">{course.summary}</p>

                  <div className="ml-course__progress">
                    <Progress
                      value={course.progressPercent}
                      label="Course progress"
                    />

                    <span className="ml-course__progress-meta">
                      {course.completedItems} of {course.totalItems} lessons
                      complete
                    </span>
                  </div>
                </div>

                <div className="ml-course__resume">
                  <div className="ml-resume-label">CURRENT LESSON</div>

                  <strong>{course.currentItemTitle}</strong>

                  <span className="ml-resume-module">
                    {course.currentModuleTitle}
                  </span>

                  <div className="ml-actions">
                    <a
                      className="ml-action ml-action--primary"
                      href={course.resumeHref}
                    >
                      Resume learning →
                    </a>

                    <a
                      className="ml-action ml-action--secondary"
                      href={course.detailHref}
                    >
                      Course details
                    </a>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
