import type { Metadata } from "next";
import { MyLearning } from "@codeintex/learning-ui";
import { backendMyLearning } from "../../src/fixtures/backend-engineering-my-learning";

export const metadata: Metadata = {
  title: "My Learning | CodeInteX Learning",
  description: "Resume your active CodeInteX Learning courses.",
};

export default function MyLearningPage() {
  return <MyLearning learning={backendMyLearning} />;
}
