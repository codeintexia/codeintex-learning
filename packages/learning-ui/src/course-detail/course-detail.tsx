import type { CourseDetailView } from "./types";

type CourseDetailProps = {
  course: CourseDetailView;
};

function formatDuration(totalMinutes: number) {
  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;

  if (hours === 0) {
    return `${minutes} min`;
  }

  if (minutes === 0) {
    return `${hours} hr`;
  }

  return `${hours} hr ${minutes} min`;
}

export function CourseDetail({ course }: CourseDetailProps) {
  const items = course.release.modules.flatMap((module) => module.items);

  const totalMinutes = items.reduce(
    (total, item) => total + (item.durationMinutes ?? 0),
    0,
  );

  return (
    <div className="course-detail">
      <header className="cd-topbar">
        <a className="cd-brand" href="/">
          <span className="cd-brand__mark" aria-hidden="true">
            CI
          </span>
          <span>CodeInteX Learning</span>
        </a>

        <a className="cd-topbar__player" href={course.primaryAction.href}>
          Learning Player →
        </a>
      </header>

      <main className="cd-shell">
        <section className="cd-hero" aria-labelledby="course-title">
          <div className="cd-hero__content">
            <div className="cd-kicker">{course.kicker}</div>

            <h1 id="course-title">{course.release.title}</h1>

            <p className="cd-summary">{course.summary}</p>

            <dl className="cd-meta" aria-label="Course details">
              <div>
                <dt>Level</dt>
                <dd>{course.level}</dd>
              </div>

              <div>
                <dt>Modules</dt>
                <dd>{course.release.modules.length}</dd>
              </div>

              <div>
                <dt>Lessons</dt>
                <dd>{items.length}</dd>
              </div>

              <div>
                <dt>Time</dt>
                <dd>{formatDuration(totalMinutes)}</dd>
              </div>
            </dl>

            <div className="cd-actions">
              <a
                className="cd-action cd-action--primary"
                href={course.primaryAction.href}
              >
                {course.primaryAction.label} →
              </a>

              <a className="cd-action cd-action--secondary" href="#curriculum">
                View curriculum
              </a>
            </div>
          </div>

          <aside className="cd-outcomes" aria-labelledby="outcomes-title">
            <div className="cd-panel-label">WHAT YOU'LL LEARN</div>

            <h2 id="outcomes-title">
              Build the mental models behind production backends.
            </h2>

            <ul>
              {course.outcomes.map((outcome) => (
                <li key={outcome}>{outcome}</li>
              ))}
            </ul>
          </aside>
        </section>

        <section
          id="curriculum"
          className="cd-section cd-curriculum"
          aria-labelledby="curriculum-title"
        >
          <div className="cd-section__heading">
            <div>
              <div className="cd-kicker">CURRICULUM</div>
              <h2 id="curriculum-title">From protocol to production discipline.</h2>
            </div>

            <p>
              {course.release.modules.length} modules · {items.length} lessons ·{" "}
              {formatDuration(totalMinutes)}
            </p>
          </div>

          <div className="cd-modules">
            {course.release.modules.map((module, moduleIndex) => (
              <article className="cd-module" key={module.id}>
                <div className="cd-module__header">
                  <span className="cd-module__number">
                    {String(moduleIndex + 1).padStart(2, "0")}
                  </span>

                  <div>
                    <div className="cd-panel-label">MODULE</div>
                    <h3>{module.title}</h3>
                  </div>
                </div>

                <ol>
                  {module.items.map((item, itemIndex) => (
                    <li key={item.id}>
                      <span className="cd-lesson__number">
                        {String(itemIndex + 1).padStart(2, "0")}
                      </span>

                      <span className="cd-lesson__title">{item.title}</span>

                      {item.durationMinutes ? (
                        <span className="cd-lesson__duration">
                          {item.durationMinutes} min
                        </span>
                      ) : null}
                    </li>
                  ))}
                </ol>
              </article>
            ))}
          </div>
        </section>

        <section className="cd-fit" aria-labelledby="fit-title">
          <div className="cd-kicker">WHO THIS IS FOR</div>
          <h2 id="fit-title">{course.audience}</h2>
        </section>
      </main>
    </div>
  );
}
