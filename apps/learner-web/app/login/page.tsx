"use client";

import { Button } from "@codeintex/ui-primitives";
import { useRouter } from "next/navigation";
import { type FormEvent, useState } from "react";
import styles from "./login.module.css";

type CsrfResponse = {
  csrfToken: string;
};

type LoginResponse = {
  authenticated: boolean;
  user: {
    id: string;
    username: string;
  } | null;
  csrfToken?: string;
  detail?: string;
};

export default function LoginPage() {
  const router = useRouter();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (pending) return;

    setPending(true);
    setError(null);

    try {
      const csrfResponse = await fetch("/api/v1/auth/csrf/", {
        cache: "no-store",
        credentials: "same-origin",
      });

      if (!csrfResponse.ok) {
        throw new Error("Could not initialize secure sign-in.");
      }

      const csrf = (await csrfResponse.json()) as CsrfResponse;

      const loginResponse = await fetch("/api/v1/auth/login/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrf.csrfToken,
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      const payload = (await loginResponse.json()) as LoginResponse;

      if (!loginResponse.ok || !payload.authenticated) {
        setError(payload.detail ?? "Username or password is incorrect.");
        return;
      }

      router.replace("/learn/backend-engineering");
      router.refresh();
    } catch {
      setError("Sign-in could not be completed. Try again.");
    } finally {
      setPending(false);
    }
  }

  return (
    <main className={styles.shell}>
      <section
        className={styles.card}
        aria-labelledby="login-title"
      >
        <div className={styles.header}>
          <p className={styles.eyebrow}>CodeInteX Learning</p>

          <h1 id="login-title" className={styles.title}>
            Continue learning.
          </h1>

          <p className={styles.description}>
            Sign in to resume your course and keep your progress
            synchronized.
          </p>
        </div>

        <form className={styles.form} onSubmit={handleSubmit}>
          <label className={styles.field}>
            <span className={styles.label}>Username</span>
            <input
              className={styles.input}
              name="username"
              type="text"
              autoComplete="username"
              autoCapitalize="none"
              spellCheck={false}
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              required
              disabled={pending}
            />
          </label>

          <label className={styles.field}>
            <span className={styles.label}>Password</span>
            <input
              className={styles.input}
              name="password"
              type="password"
              autoComplete="current-password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
              disabled={pending}
            />
          </label>

          <Button
            className={styles.submit}
            type="submit"
            disabled={pending}
          >
            {pending ? "Signing in…" : "Sign in"}
          </Button>

          {error ? (
            <p className={styles.error} role="alert">
              {error}
            </p>
          ) : null}
        </form>

        <p className={styles.meta}>
          Your learning progress is stored against your signed-in
          account.
        </p>
      </section>
    </main>
  );
}
