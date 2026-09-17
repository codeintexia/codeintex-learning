import type { Metadata } from "next";
import { CourseDetail } from "@codeintex/learning-ui";

import { getCourseDetail } from "../../../src/data/course-detail";
import { getCourseOffer } from "../../../src/data/course-offer";
import { getLearnerProgress } from "../../../src/data/learner-progress";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Backend Engineering Foundations | CodeInteX Learning",
  description:
    "Learn HTTP, API contracts, authentication, sessions, and production testing through first-principles backend engineering.",
};

function formatPrice(
  amountMinor: number,
  currency: string,
) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency,
    maximumFractionDigits: 0,
  }).format(amountMinor);
}

export default async function BackendEngineeringCoursePage() {
  const courseSlug = "backend-engineering";

  const [course, progressResult] = await Promise.all([
    getCourseDetail(courseSlug),
    getLearnerProgress(courseSlug),
  ]);

  if (progressResult.status === "ok") {
    return (
      <CourseDetail
        course={{
          ...course,
          primaryAction: {
            label: "Resume course",
            href: `/learn/${courseSlug}`,
          },
        }}
      />
    );
  }

  const offer = await getCourseOffer(courseSlug);
  const checkoutPath = `/checkout/${courseSlug}`;

  const primaryAction =
    progressResult.status === "unauthenticated"
      ? {
          label: `Buy course · ${formatPrice(
            offer.amountMinor,
            offer.currency,
          )}`,
          href: `/login?next=${encodeURIComponent(
            checkoutPath,
          )}`,
        }
      : {
          label: `Buy course · ${formatPrice(
            offer.amountMinor,
            offer.currency,
          )}`,
          href: checkoutPath,
        };

  return (
    <CourseDetail
      course={{
        ...course,
        primaryAction,
      }}
    />
  );
}
