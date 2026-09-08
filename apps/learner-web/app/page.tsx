import { CourseCatalog } from "@codeintex/learning-ui";
import { getCourseCatalog } from "../src/data/course-catalog";

export const dynamic = "force-dynamic";

export default async function Home() {
  const catalog = await getCourseCatalog();

  return <CourseCatalog catalog={catalog} />;
}
