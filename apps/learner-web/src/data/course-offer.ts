const DEFAULT_API_BASE_URL =
  "http" + "://" + "127.0.0.1:8000";

export type CourseOfferView = {
  amountMinor: number;
  currency: string;
};

export async function getCourseOffer(
  slug: string,
): Promise<CourseOfferView> {
  const apiBaseUrl =
    process.env.LEARNING_API_BASE_URL ?? DEFAULT_API_BASE_URL;

  const response = await fetch(
    `${apiBaseUrl}/api/v1/commerce/courses/${encodeURIComponent(
      slug,
    )}/offer/`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      `Commerce offer request failed: ${response.status}`,
    );
  }

  const payload: unknown = await response.json();

  if (
    !payload ||
    typeof payload !== "object" ||
    !("offer" in payload) ||
    !payload.offer ||
    typeof payload.offer !== "object" ||
    !("amountMinor" in payload.offer) ||
    typeof payload.offer.amountMinor !== "number" ||
    !("currency" in payload.offer) ||
    typeof payload.offer.currency !== "string"
  ) {
    throw new Error(
      "Commerce API returned an invalid offer payload.",
    );
  }

  return {
    amountMinor: payload.offer.amountMinor,
    currency: payload.offer.currency,
  };
}
