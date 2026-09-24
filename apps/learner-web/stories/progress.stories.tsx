import type {
  Meta,
  StoryObj,
} from "@storybook/nextjs-vite";

import { Progress } from "@codeintex/ui-primitives";

const meta = {
  title: "Foundation/Progress",
  component: Progress,
  args: {
    label: "Course progress",
  },
} satisfies Meta<typeof Progress>;

export default meta;

type Story = StoryObj<typeof meta>;

export const Empty = {
  args: {
    value: 0,
  },
} satisfies Story;

export const InProgress = {
  args: {
    value: 60,
  },
} satisfies Story;

export const Complete = {
  args: {
    value: 100,
  },
} satisfies Story;
