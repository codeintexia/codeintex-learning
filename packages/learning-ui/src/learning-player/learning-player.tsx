"use client";

import { useMemo, useState } from "react";
import { Button, Progress } from "@codeintex/ui-primitives";
import type {
  CourseReleaseView,
  CurriculumItemView,
  LearningPlayerState,
  LessonContentView,
} from "./types";

type LearningPlayerProps = {
  release: CourseReleaseView;
  initialState: LearningPlayerState;
  lessonByItemId: Record<string, LessonContentView>;
};

function flattenItems(release: CourseReleaseView) {
  return release.modules.flatMap((module) => module.items);
}

function ItemStatus({
  item,
  active,
}: {
  item: CurriculumItemView;
  active: boolean;
}) {
  if (item.completed) {
    return (
      <span className="lp-status lp-status--complete" aria-label="Completed">
        ✓
      </span>
    );
  }

  if (active) {
    return (
      <span className="lp-status lp-status--current" aria-label="Current lesson">
        ●
      </span>
    );
  }

  return (
    <span className="lp-status" aria-hidden="true">
      ○
    </span>
  );
}

export function LearningPlayer({
  release,
  initialState,
  lessonByItemId,
}: LearningPlayerProps) {
  const allItems = useMemo(() => flattenItems(release), [release]);
  const [currentItemId, setCurrentItemId] = useState(initialState.currentItemId);
  const [completedIds, setCompletedIds] = useState(
    new Set(allItems.filter((item) => item.completed).map((item) => item.id)),
  );

  const currentIndex = Math.max(
    0,
    allItems.findIndex((item) => item.id === currentItemId),
  );
  const current = allItems[currentIndex];
  const lesson = lessonByItemId[currentItemId] ?? lessonByItemId[allItems[0].id];

  const progressPercent = Math.round((completedIds.size / allItems.length) * 100);

  function goTo(index: number) {
    const item = allItems[index];
    if (!item) return;

    setCurrentItemId(item.id);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function completeAndContinue() {
    setCompletedIds((previous) => {
      const next = new Set(previous);
      next.add(currentItemId);
      return next;
    });

    if (currentIndex < allItems.length - 1) {
      goTo(currentIndex + 1);
    }
  }

  return (
    <div className="learning-player">
      <header className="lp-header">
        <div className="lp-header__course">
          <a className="lp-back" href="/" aria-label="Back to course">
            ←
          </a>
          <div>
            <div className="lp-kicker">COURSE · RELEASE {release.release}</div>
            <strong>{release.title}</strong>
          </div>
        </div>

        <div className="lp-header__progress">
          <Progress value={progressPercent} label="Course progress" />
        </div>
      </header>

      <details className="lp-mobile-curriculum">
        <summary>
          Curriculum <span>{progressPercent}% complete</span>
        </summary>
        <Curriculum
          release={release}
          currentItemId={currentItemId}
          completedIds={completedIds}
          onSelect={setCurrentItemId}
        />
      </details>

      <div className="lp-layout">
        <aside className="lp-sidebar" aria-label="Course curriculum">
          <Curriculum
            release={release}
            currentItemId={currentItemId}
            completedIds={completedIds}
            onSelect={setCurrentItemId}
          />
        </aside>

        <main className="lp-main">
          <article className="lp-lesson">
            <div className="lp-lesson__eyebrow">{lesson.eyebrow}</div>
            <h1>{lesson.title}</h1>
            <p className="lp-lesson__summary">{lesson.summary}</p>

            <div className="lp-divider" />

            {lesson.sections.map((section, index) => (
              <section
                className="lp-content-section"
                key={`${section.heading ?? "section"}-${index}`}
              >
                {section.heading ? <h2>{section.heading}</h2> : null}
                <p>{section.body}</p>
                {section.code ? (
                  <pre className="lp-code">
                    <code>{section.code}</code>
                  </pre>
                ) : null}
              </section>
            ))}
          </article>

          <footer className="lp-footer">
            <Button
              variant="secondary"
              disabled={currentIndex === 0}
              onClick={() => goTo(currentIndex - 1)}
            >
              ← Previous
            </Button>

            <div className="lp-footer__position">
              {currentIndex + 1} of {allItems.length}
            </div>

            <Button onClick={completeAndContinue}>
              {currentIndex === allItems.length - 1
                ? "Complete lesson"
                : completedIds.has(current.id)
                  ? "Continue →"
                  : "Complete & continue →"}
            </Button>
          </footer>
        </main>
      </div>
    </div>
  );
}

function Curriculum({
  release,
  currentItemId,
  completedIds,
  onSelect,
}: {
  release: CourseReleaseView;
  currentItemId: string;
  completedIds: Set<string>;
  onSelect: (id: string) => void;
}) {
  return (
    <nav className="lp-curriculum">
      {release.modules.map((module, moduleIndex) => (
        <section className="lp-module" key={module.id}>
          <div className="lp-module__label">
            MODULE {String(moduleIndex + 1).padStart(2, "0")}
          </div>
          <h2>{module.title}</h2>

          <ol>
            {module.items.map((item) => {
              const active = item.id === currentItemId;
              const completedItem = {
                ...item,
                completed: completedIds.has(item.id),
              };

              return (
                <li key={item.id}>
                  <button
                    aria-current={active ? "step" : undefined}
                    className={`lp-item ${active ? "lp-item--active" : ""}`}
                    onClick={() => onSelect(item.id)}
                  >
                    <ItemStatus item={completedItem} active={active} />
                    <span className="lp-item__body">
                      <span className="lp-item__title">{item.title}</span>
                      <span className="lp-item__meta">
                        {item.kind}
                        {item.durationMinutes ? ` · ${item.durationMinutes} min` : ""}
                      </span>
                    </span>
                  </button>
                </li>
              );
            })}
          </ol>
        </section>
      ))}
    </nav>
  );
}
