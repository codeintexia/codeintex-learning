import { CourseCatalog } from "@codeintex/learning-ui";
import { courseCatalog } from "../src/fixtures/course-catalog";

export default function Home() {
  return <CourseCatalog catalog={courseCatalog} />;
}
