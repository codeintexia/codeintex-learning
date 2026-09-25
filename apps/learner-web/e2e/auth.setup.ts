import {
  expect,
  test as setup,
} from "@playwright/test";
import { execFileSync } from "node:child_process";
import { randomBytes } from "node:crypto";
import {
  dirname,
  resolve,
} from "node:path";
import { mkdirSync } from "node:fs";

const authFile = resolve(
  __dirname,
  "../test-results/.auth/learner.json",
);

const backendDirectory = resolve(
  __dirname,
  "../../learning-backend",
);

const backendPython = resolve(
  __dirname,
  "../../../.venv-backend/bin/python",
);

setup("prepare authenticated learner", async ({
  request,
}) => {
  const password =
    process.env.CODEINTEX_E2E_PASSWORD ??
    randomBytes(32).toString("base64url");

  execFileSync(
    backendPython,
    [
      "manage.py",
      "prepare_e2e_learner",
    ],
    {
      cwd: backendDirectory,
      env: {
        ...process.env,
        CODEINTEX_E2E_FIXTURES: "1",
        CODEINTEX_E2E_PASSWORD: password,
      },
      stdio: "inherit",
    },
  );

  const csrfResponse = await request.get(
    "/api/v1/auth/csrf/",
  );

  expect(csrfResponse.status()).toBe(200);

  const csrfPayload = (await csrfResponse.json()) as {
    csrfToken: string;
  };

  const loginResponse = await request.post(
    "/api/v1/auth/login/",
    {
      headers: {
        "X-CSRFToken": csrfPayload.csrfToken,
      },
      data: {
        username: "codeintex-e2e",
        password,
      },
    },
  );

  expect(loginResponse.status()).toBe(200);

  const loginPayload = (await loginResponse.json()) as {
    authenticated: boolean;
    user: {
      username: string;
    } | null;
  };

  expect(loginPayload.authenticated).toBe(true);
  expect(loginPayload.user?.username).toBe(
    "codeintex-e2e",
  );

  mkdirSync(dirname(authFile), {
    recursive: true,
  });

  await request.storageState({
    path: authFile,
  });
});
