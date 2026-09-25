"use client";

import { useEffect, useRef, useState } from "react";
import {
  useParams,
  useRouter,
} from "next/navigation";

type CsrfResponse = {
  csrfToken: string;
};

type CheckoutResponse = {
  checkout?: {
    orderId: string;
    paymentId: string;
    redirectUrl: string;
    amountMinor: number;
    currency: string;
    expiresAt: string;
  };
  error?: string;
  detail?: string;
};

export default function CheckoutPage() {
  const { courseSlug } = useParams<{
    courseSlug: string;
  }>();

  const router = useRouter();

  const startedForCourse =
    useRef<string | null>(null);

  const [error, setError] =
    useState<string | null>(null);

  useEffect(() => {
    if (
      startedForCourse.current === courseSlug
    ) {
      return;
    }

    startedForCourse.current = courseSlug;

    async function startCheckout() {
      try {
        const csrfResponse = await fetch(
          "/api/v1/auth/csrf/",
          {
            cache: "no-store",
            credentials: "same-origin",
          },
        );

        if (!csrfResponse.ok) {
          throw new Error(
            "Could not initialize secure checkout.",
          );
        }

        const csrf =
          (await csrfResponse.json()) as CsrfResponse;

        const checkoutResponse = await fetch(
          `/api/v1/commerce/courses/${encodeURIComponent(
            courseSlug,
          )}/checkout/`,
          {
            method: "POST",
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": csrf.csrfToken,
            },
          },
        );

        const payload =
          (await checkoutResponse.json()) as CheckoutResponse;

        if (checkoutResponse.status === 401) {
          router.replace(
            `/login?next=${encodeURIComponent(
              `/checkout/${courseSlug}`,
            )}`,
          );
          return;
        }

        if (
          checkoutResponse.status === 409 &&
          (
            payload.error === "already_entitled" ||
            payload.error ===
              "payment_already_succeeded"
          )
        ) {
          router.replace(
            `/learn/${courseSlug}`,
          );
          return;
        }

        if (
          !checkoutResponse.ok ||
          !payload.checkout?.redirectUrl
        ) {
          setError(
            "Checkout could not be started. Please return to the course page and try again.",
          );
          return;
        }

        const destination = new URL(
          payload.checkout.redirectUrl,
        );

        if (destination.protocol !== "https:") {
          throw new Error(
            "Checkout destination is not secure.",
          );
        }

        window.location.assign(
          destination.toString(),
        );
      } catch {
        setError(
          "Checkout could not be started. Please return to the course page and try again.",
        );
      }
    }

    void startCheckout();
  }, [courseSlug, router]);

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        padding: "2rem",
      }}
    >
      <section
        aria-labelledby="checkout-title"
        style={{
          width: "min(100%, 32rem)",
        }}
      >
        <p>CodeInteX Learning</p>

        <h1 id="checkout-title">
          {error
            ? "Checkout unavailable."
            : "Preparing secure checkout…"}
        </h1>

        {error ? (
          <>
            <p role="alert">{error}</p>
            <p>
              <a
                href={`/courses/${courseSlug}`}
              >
                Return to course
              </a>
            </p>
          </>
        ) : (
          <p>
            You’ll continue to the secure payment page.
          </p>
        )}
      </section>
    </main>
  );
}
