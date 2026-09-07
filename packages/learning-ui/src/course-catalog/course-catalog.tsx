import type { CourseCatalogView } from "./types";

type CourseCatalogProps = {
  catalog: CourseCatalogView;
};

function formatDuration(totalMinutes: number) {
  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;

  if (hours === 0) return `${minutes} min`;
  if (minutes === 0) return `${hours} hr`;

  return `${hours} hr ${minutes} min`;
}

export function CourseCatalog({ catalog }: CourseCatalogProps) {
  return (
    <div className="catalog">
      <header className="catalog-topbar">
        <a className="catalog-brand" href="/">
          <span className="catalog-brand__mark" aria-hidden="true">
            CI
          </span>
          <span>CodeInteX Learning</span>
        </a>

        <a className="catalog-nav-link" href="/my-learning">
          My Learning →
        </a>
      </header>

      <main className="catalog-shell">
        <section className="catalog-hero" aria-labelledby="catalog-title">
          <div className="catalog-kicker">CODEINTEX LEARNING</div>

          <h1 id="catalog-title">
            Learn systems.
            <br />
            Not recipes.
          </h1>

          <p>
            Technical learning built around the mental models, contracts, and
            failure modes behind production software.
          </p>
        </section>

        <section
          className="catalog-courses"
          aria-labelledby="available-courses-title"
        >
          <header className="catalog-section-heading">
            <h2 id="available-courses-title">Available courses</h2>

            <span>
              {catalog.courses.length}{" "}
              {catalog.courses.length === 1 ? "course" : "courses"}
            </span>
          </header>

          <div className="catalog-list">
            {catalog.courses.map((course, index) => (
              <a
                className="catalog-course"
                href={course.href}
                key={course.id}
              >
                <div className="catalog-course__index" aria-hidden="true">
                  {String(index + 1).padStart(2, "0")}
                </div>

                <div className="catalog-course__content">
                  <div className="catalog-kicker">{course.subject}</div>

                  <h3>{course.title}</h3>

                  <p>{course.summary}</p>

                  <dl className="catalog-course__meta">
                    <div>
                      <dt>Level</dt>
                      <dd>{course.level}</dd>
                    </div>

                    <div>
                      <dt>Modules</dt>
                      <dd>{course.moduleCount}</dd>
                    </div>

                    <div>
                      <dt>Lessons</dt>
                      <dd>{course.lessonCount}</dd>
                    </div>

                    <div>
                      <dt>Time</dt>
                      <dd>{formatDuration(course.durationMinutes)}</dd>
                    </div>
                  </dl>
                </div>

                <div className="catalog-course__action" aria-hidden="true">
                  Explore
                  <span>→</span>
                </div>
              </a>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
