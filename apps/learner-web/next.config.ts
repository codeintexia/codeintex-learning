import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: [
    "@codeintex/design-tokens",
    "@codeintex/ui-primitives",
    "@codeintex/learning-ui"
  ]
};

export default nextConfig;
