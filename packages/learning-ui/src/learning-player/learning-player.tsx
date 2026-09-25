"use client";

import { useMemo, useRef, useState } from "react";
import { Button, Progress } from "@codeintex/ui-primitives";
import type {
  CourseReleaseView,
  CurriculumItemView,
  LearningPlayerState,
  LearningProgressView,
  LessonContentView,
} from "./types";

type LearningPlayerProps = {
  courseHref: string;
  release: CourseReleaseView;
  initialState: LearningPlayerState;
  initialProgressPercent: number;
  lessonByItemId: Record<string, LessonContentView>;
  onComplete: (
    itemId: string,
  ) => Promise<LearningProgressView>;
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
      <span className="lp-status lp-status--current" aria-label="Current item">
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
  courseHref,
  release,
  initialState,
  initialProgressPercent,
  lessonByItemId,
  onComplete,
}: LearningPlayerProps) {
  const allItems = useMemo(() => flattenItems(release), [release]);
  const [currentItemId, setCurrentItemId] = useState(initialState.currentItemId);
  const [completedIds, setCompletedIds] = useState(
    new Set(allItems.filter((item) => item.completed).map((item) => item.id)),
  );
  const [progressPercent, setProgressPercent] =
    useState(initialProgressPercent);
  const [completionPending, setCompletionPending] = useState(false);
  const [completionError, setCompletionError] = useState<string | null>(null);
  const lessonContentRef = useRef<HTMLElement>(null);
  const mobileCurriculumRef = useRef<HTMLDetailsElement>(null);

  const currentIndex = Math.max(
    0,
    allItems.findIndex((item) => item.id === currentItemId),
  );
  const current = allItems[currentIndex];
  const lesson = lessonByItemId[currentItemId] ?? lessonByItemId[allItems[0].id];

  function selectItem(itemId: string) {
    const itemChanged = itemId !== currentItemId;

    setCurrentItemId(itemId);

    if (mobileCurriculumRef.current?.open) {
      mobileCurriculumRef.current.open = false;
    }

    if (!itemChanged) {
      return;
    }

    const prefersReducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;

    window.requestAnimationFrame(() => {
      lessonContentRef.current?.focus({
        preventScroll: true,
      });

      window.scrollTo({
        top: 0,
        behavior: prefersReducedMotion ? "instant" : "smooth",
      });
    });
  }

  function goTo(index: number) {
    const item = allItems[index];
    if (!item) return;

    selectItem(item.id);
  }

  async function completeAndContinue() {
    if (completionPending) return;

    if (completedIds.has(current.id)) {
      goTo(currentIndex + 1);
      return;
    }

    setCompletionPending(true);
    setCompletionError(null);

    try {
      const progress = await onComplete(currentItemId);

      setCompletedIds(
        new Set(progress.completedItemIds),
      );
      setProgressPercent(progress.progressPercent);

      if (progress.currentItemId) {
        const targetExists = allItems.some(
          (item) => item.id === progress.currentItemId,
        );

        if (targetExists) {
          selectItem(progress.currentItemId);
        }
      }
    } catch {
      setCompletionError("Progress could not be saved. Try again.");
    } finally {
      setCompletionPending(false);
    }
  }

  return (
    <div className="learning-player">
      <header className="lp-header">
        <div className="lp-header__course">
          <a
            className="lp-back"
            href={courseHref}
            aria-label="Back to course details"
          >
            ←
          </a>
          <div>
            <div className="lp-kicker">CODEINTEX LEARNING</div>
            <strong>{release.title}</strong>
          </div>
        </div>

        <div className="lp-header__progress">
          <Progress
            value={progressPercent}
            label={`${release.title} lesson progress`}
          />
        </div>
      </header>

      <details
        ref={mobileCurriculumRef}
        className="lp-mobile-curriculum"
      >
        <summary>
          <span className="lp-mobile-curriculum__title">
            Curriculum
          </span>
          <span className="lp-mobile-curriculum__progress">
            {progressPercent}% of lessons completed
          </span>
        </summary>
        <Curriculum
          release={release}
          currentItemId={currentItemId}
          completedIds={completedIds}
          onSelect={selectItem}
        />
      </details>

      <div className="lp-layout">
        <aside className="lp-sidebar" aria-label="Course curriculum">
          <Curriculum
            release={release}
            currentItemId={currentItemId}
            completedIds={completedIds}
            onSelect={selectItem}
          />
        </aside>

        <main
          ref={lessonContentRef}
          id="lesson-content"
          className="lp-main"
          tabIndex={-1}
        >
          <article
            className="lp-lesson"
            aria-labelledby="lesson-title"
          >
            <div className="lp-lesson__header">
              <div className="lp-lesson__eyebrow">
                {lesson.eyebrow}
              </div>
              <div className="lp-lesson__position">
                {currentIndex + 1} OF {allItems.length}
                {current.durationMinutes
                  ? ` · ${current.durationMinutes} MIN`
                  : ""}
              </div>
            </div>

            <h1 id="lesson-title">{lesson.title}</h1>
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

            <div
              className="lp-footer__position"
              aria-live="polite"
              aria-label={`Item ${currentIndex + 1} of ${allItems.length}`}
            >
              {completionError ? (
                completionError
              ) : (
                <>
                  {String(currentIndex + 1).padStart(2, "0")}
                  <span aria-hidden="true"> / </span>
                  {String(allItems.length).padStart(2, "0")}
                </>
              )}
            </div>

            <Button
              disabled={
                completionPending ||
                (completedIds.has(current.id) &&
                  currentIndex === allItems.length - 1)
              }
              onClick={completeAndContinue}
            >
              {completionPending
                ? "Saving…"
                : completedIds.has(current.id)
                  ? currentIndex === allItems.length - 1
                    ? "Lesson completed"
                    : "Continue →"
                  : currentIndex === allItems.length - 1
                    ? "Complete lesson"
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
                    type="button"
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
