import {
  defineConfig,
  devices,
} from "@playwright/test";
import path from "node:path";

const backendDirectory = path.resolve(
  __dirname,
  "../learning-backend",
);

export default defineConfig({
  testDir: "./e2e",
  outputDir: "./test-results",

  fullyParallel: false,
  workers: 1,

  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,

  reporter: "list",

  use: {
    baseURL: "http://127.0.0.1:3000",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },

  projects: [
    {
      name: "setup",
      testMatch: /.*\.setup\.ts/,
    },
    {
      name: "chromium",
      use: {
        ...devices["Desktop Chrome"],
        storageState:
          "test-results/.auth/learner.json",
      },
      dependencies: ["setup"],
    },
  ],

  webServer: [
    {
      name: "Django",
      command:
        "../../.venv-backend/bin/python manage.py runserver 127.0.0.1:8000",
      cwd: backendDirectory,
      url: "http://127.0.0.1:8000/api/v1/auth/session/",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
      stdout: "ignore",
      stderr: "pipe",
    },
    {
      name: "Next.js",
      command: "npm run dev",
      cwd: __dirname,
      url: "http://127.0.0.1:3000/login",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
      stdout: "ignore",
      stderr: "pipe",
    },
  ],
});
