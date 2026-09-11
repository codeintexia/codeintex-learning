import { MyLearning } from "@codeintex/learning-ui";
import { redirect } from "next/navigation";

import { getMyLearning } from "../../src/data/my-learning";

export const dynamic = "force-dynamic";

export default async function MyLearningPage() {
  const result = await getMyLearning();

  if (result.status === "unauthenticated") {
    redirect("/login");
  }

  return <MyLearning learning={result.learning} />;
}
