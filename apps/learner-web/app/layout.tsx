import type { Metadata } from "next";
import "@codeintex/design-tokens/styles.css";
import "@codeintex/ui-primitives/styles.css";
import "@codeintex/learning-ui/styles.css";
import "./globals.css";

export const metadata: Metadata = {
  title: "CodeInteX Learning",
  description: "Premium technical learning experience by CodeInteX.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
