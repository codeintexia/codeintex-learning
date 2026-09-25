import AxeBuilder from "@axe-core/playwright";
import {
  expect,
  test,
  type Page,
  type TestInfo,
} from "@playwright/test";

const WCAG_AA_TAGS = [
  "wcag2a",
  "wcag2aa",
  "wcag21a",
  "wcag21aa",
  "wcag22aa",
];

async function expectNoAutomatedA11yViolations(
  page: Page,
  testInfo: TestInfo,
  label: string,
) {
  const results = await new AxeBuilder({
    page,
  })
    .withTags(WCAG_AA_TAGS)
    .analyze();

  await testInfo.attach(
    `axe-${label}`,
    {
      body: JSON.stringify(results, null, 2),
      contentType: "application/json",
    },
  );

  const violations = results.violations.map(
    (violation) => ({
      id: violation.id,
      impact: violation.impact,
      targets: violation.nodes.map(
        (node) => node.target,
      ),
    }),
  );

  expect(
    violations,
    `Automatically detectable accessibility violations in ${label}`,
  ).toEqual([]);
}

test(
  "learner resumes, navigates curriculum, and advances from authoritative progress",
  async ({ page }, testInfo) => {
    await page.goto("/my-learning");

    await expect(page).toHaveURL(
      /\/my-learning$/,
    );

    await expect(
      page.getByRole("heading", {
        name: "Your learning, at a glance.",
      }),
    ).toBeVisible();

    const courseCard = page
      .getByRole("article")
      .filter({
        has: page.getByRole("heading", {
          name: "Backend Engineering Foundations",
        }),
      });

    await expect(courseCard).toBeVisible();

    await expect(
      courseCard.getByText(
        "0 of 5 lessons complete",
      ),
    ).toBeVisible();

    await expect(
      courseCard.getByText(
        "How HTTP actually moves",
      ),
    ).toBeVisible();

    await expectNoAutomatedA11yViolations(
      page,
      testInfo,
      "my-learning",
    );

    await courseCard
      .getByRole("link", {
        name: "Resume learning →",
      })
      .click();

    await expect(page).toHaveURL(
      /\/learn\/backend-engineering$/,
    );

    const lessonContent =
      page.locator("#lesson-content");

    const lessonHeading =
      page.getByRole("heading", {
        level: 1,
      });

    await expect(lessonHeading).toHaveText(
      "How HTTP actually moves",
    );

    const progress = page.getByRole(
      "progressbar",
      {
        name: "Course progress",
      },
    );

    await expect(progress).toHaveAttribute(
      "aria-valuenow",
      "0",
    );

    const curriculum = page.getByRole(
      "complementary",
      {
        name: "Course curriculum",
      },
    );

    const firstLesson = curriculum.getByRole(
      "button",
      {
        name: /How HTTP actually moves/,
      },
    );

    const secondLesson = curriculum.getByRole(
      "button",
      {
        name: /Designing resource-oriented APIs/,
      },
    );

    await expect(firstLesson).toHaveAttribute(
      "aria-current",
      "step",
    );

    // Verify learner-driven curriculum navigation and
    // the focus-management contract.
    await secondLesson.click();

    await expect(lessonHeading).toHaveText(
      "Designing resource-oriented APIs",
    );

    await expect(lessonContent).toBeFocused();

    await expect(secondLesson).toHaveAttribute(
      "aria-current",
      "step",
    );

    // Return to the authoritative current lesson before
    // exercising persistence.
    await firstLesson.click();

    await expect(lessonHeading).toHaveText(
      "How HTTP actually moves",
    );

    await expect(lessonContent).toBeFocused();

    const completionResponsePromise =
      page.waitForResponse(
        (response) =>
          response.request().method() === "POST" &&
          response
            .url()
            .includes(
              "/api/v1/courses/backend-engineering/lessons/",
            ) &&
          response.url().endsWith("/complete/"),
      );

    await page
      .getByRole("button", {
        name: "Complete & continue →",
      })
      .click();

    const completionResponse =
      await completionResponsePromise;

    expect(
      completionResponse.status(),
    ).toBe(201);

    const completionPayload =
      (await completionResponse.json()) as {
        created: boolean;
        progress: {
          completedItemIds: string[];
          completedItems: number;
          totalItems: number;
          progressPercent: number;
          currentItemId: string | null;
        };
      };

    expect(completionPayload.created).toBe(
      true,
    );
    expect(
      completionPayload.progress.completedItems,
    ).toBe(1);
    expect(
      completionPayload.progress.totalItems,
    ).toBe(5);
    expect(
      completionPayload.progress.progressPercent,
    ).toBe(20);
    expect(
      completionPayload.progress.currentItemId,
    ).not.toBeNull();

    // The player must consume the authoritative response:
    // lesson 2 becomes current instead of calculating
    // progression independently in the browser.
    await expect(lessonHeading).toHaveText(
      "Designing resource-oriented APIs",
    );

    await expect(progress).toHaveAttribute(
      "aria-valuenow",
      "20",
    );

    await expect(secondLesson).toHaveAttribute(
      "aria-current",
      "step",
    );

    await expect(
      firstLesson.getByLabel("Completed"),
    ).toBeVisible();

    await expect(lessonContent).toBeFocused();

    await expectNoAutomatedA11yViolations(
      page,
      testInfo,
      "learning-player-after-completion",
    );
  },
);


test("missing learner session redirects protected routes to login", async ({
  page,
}) => {
  await page.context().clearCookies();

  await page.goto("/my-learning");

  await expect(page).toHaveURL(
    /\/login$/,
  );

  await expect(
    page.getByRole("heading", {
      name: "Continue learning.",
    }),
  ).toBeVisible();

  await page.goto("/learn/backend-engineering");

  await expect(page).toHaveURL(
    /\/login$/,
  );

  await expect(
    page.getByRole("heading", {
      name: "Continue learning.",
    }),
  ).toBeVisible();
});
