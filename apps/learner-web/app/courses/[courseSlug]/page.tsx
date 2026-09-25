import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { CourseDetail } from "@codeintex/learning-ui";

import {
  CourseNotFoundError,
  getCourseDetail,
} from "../../../src/data/course-detail";
import { getCourseOffer } from "../../../src/data/course-offer";
import { getLearnerProgress } from "../../../src/data/learner-progress";

export const dynamic = "force-dynamic";

type CoursePageProps = {
  params: Promise<{
    courseSlug: string;
  }>;
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

async function getCourseOrNotFound(
  courseSlug: string,
) {
  try {
    return await getCourseDetail(courseSlug);
  } catch (error) {
    if (error instanceof CourseNotFoundError) {
      notFound();
    }

    throw error;
  }
}

export async function generateMetadata({
  params,
}: CoursePageProps): Promise<Metadata> {
  const { courseSlug } = await params;
  const course = await getCourseOrNotFound(
    courseSlug,
  );

  return {
    title: `${course.release.title} | CodeInteX Learning`,
    description: course.summary,
  };
}

export default async function CoursePage({
  params,
}: CoursePageProps) {
  const { courseSlug } = await params;

  const [course, progressResult] = await Promise.all([
    getCourseOrNotFound(courseSlug),
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

  const offerResult =
    await getCourseOffer(courseSlug);

  if (offerResult.status === "unavailable") {
    return (
      <CourseDetail
        course={{
          ...course,
          primaryAction: undefined,
          availabilityMessage:
            "Enrollment is not currently available.",
        }}
      />
    );
  }

  const offer = offerResult.offer;
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
