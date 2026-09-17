"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

const COURSE_SLUG = "backend-engineering";
const LEARN_PATH = `/learn/${COURSE_SLUG}`;
const RETURN_PATH = `/checkout/${COURSE_SLUG}/return`;

type ReturnState =
  | "checking"
  | "still-processing"
  | "error";

export default function CheckoutReturnPage() {
  const [state, setState] = useState<ReturnState>("checking");

  useEffect(() => {
    let cancelled = false;
    let attempts = 0;

    const maxAttempts = 20;
    const retryDelayMs = 1500;

    async function checkAccess() {
      if (cancelled) {
        return;
      }

      attempts += 1;

      try {
        const response = await fetch(
          `/api/v1/courses/${COURSE_SLUG}/progress/`,
          {
            credentials: "same-origin",
            cache: "no-store",
          },
        );

        if (response.status === 200) {
          window.location.replace(LEARN_PATH);
          return;
        }

        if (response.status === 401) {
          window.location.replace(
            `/login?next=${encodeURIComponent(RETURN_PATH)}`,
          );
          return;
        }

        if (response.status !== 404) {
          setState("error");
          return;
        }
      } catch {
        setState("error");
        return;
      }

      if (attempts >= maxAttempts) {
        setState("still-processing");
        return;
      }

      window.setTimeout(checkAccess, retryDelayMs);
    }

    void checkAccess();

    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <main
      style={{
        maxWidth: 720,
        margin: "0 auto",
        padding: "96px 24px",
      }}
    >
      {state === "checking" && (
        <>
          <h1>Confirming your access…</h1>
          <p>
            We&apos;re checking the server-authoritative purchase status.
            This usually takes only a few seconds.
          </p>
        </>
      )}

      {state === "still-processing" && (
        <>
          <h1>Your access is still being confirmed.</h1>
          <p>
            The payment provider and CodeInteX may still be synchronizing.
            You can check again without making another payment.
          </p>
          <p>
            <Link href={RETURN_PATH}>Check again</Link>
          </p>
        </>
      )}

      {state === "error" && (
        <>
          <h1>We couldn&apos;t confirm your access yet.</h1>
          <p>
            Do not make another payment. Return here and try again shortly.
          </p>
          <p>
            <Link href={RETURN_PATH}>Try again</Link>
          </p>
        </>
      )}
    </main>
  );
}
