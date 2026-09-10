import type { NextConfig } from "next";

const learningApiBaseUrl =
  process.env.LEARNING_API_BASE_URL ??
  ("http" + "://" + "127.0.0.1:8000");

const nextConfig: NextConfig = {
  skipTrailingSlashRedirect: true,

  transpilePackages: [
    "@codeintex/design-tokens",
    "@codeintex/ui-primitives",
    "@codeintex/learning-ui",
  ],

  async rewrites() {
    return [
      {
        source: "/api/v1/:path*/",
        destination: `${learningApiBaseUrl}/api/v1/:path*/`,
      },
    ];
  },
};

export default nextConfig;
