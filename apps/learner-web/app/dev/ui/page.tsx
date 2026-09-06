import { Button, Progress } from "@codeintex/ui-primitives";

const swatches = [
  ["Canvas", "var(--surface-canvas)"],
  ["Default", "var(--surface-default)"],
  ["Subtle", "var(--surface-subtle)"],
  ["Primary action", "var(--action-primary)"],
  ["Success", "var(--feedback-success)"],
  ["Danger", "var(--feedback-danger)"],
];

export default function UIFoundationPage() {
  return (
    <main className="foundation">
      <header className="foundation-header">
        <div className="foundation-kicker">INTERNAL · DEV</div>
        <h1>UI Foundation</h1>
        <p>
          A deliberately small visual bench for the semantic contract currently
          required by the Learning Player.
        </p>
      </header>

      <section className="foundation-section">
        <h2>Color roles</h2>
        <div className="swatch-grid">
          {swatches.map(([name, value]) => (
            <div className="swatch-card" key={name}>
              <div className="swatch" style={{ background: value }} />
              <strong>{name}</strong>
              <code>{value}</code>
            </div>
          ))}
        </div>
      </section>

      <section className="foundation-section">
        <h2>Typography</h2>
        <div className="type-stack">
          <div className="type-display">Build systems worth learning from.</div>
          <div className="type-heading">Authentication & Authorization</div>
          <p>
            Body text should be calm enough for sustained technical reading
            while retaining the density of a professional tool.
          </p>
          <code>const principle = "content dominates chrome";</code>
        </div>
      </section>

      <section className="foundation-section">
        <h2>Current primitives</h2>
        <div className="primitive-row">
          <Button>Primary action</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="ghost">Ghost</Button>
          <Button disabled>Disabled</Button>
        </div>
        <div className="progress-demo">
          <Progress value={38} label="Course progress" />
        </div>
      </section>

      <section className="foundation-section">
        <h2>Stop rule</h2>
        <div className="foundation-callout">
          Do not add more primitives until a real product surface requires
          them. Build the product first; extract the repeated pattern second.
        </div>
      </section>
    </main>
  );
}
