import type { Preview } from "@storybook/nextjs-vite";

import "@codeintex/design-tokens/styles.css";
import "@codeintex/ui-primitives/styles.css";
import "@codeintex/learning-ui/styles.css";
import "../app/globals.css";

const preview: Preview = {
  parameters: {
    nextjs: {
      appDirectory: true,
    },
  },
};

export default preview;
