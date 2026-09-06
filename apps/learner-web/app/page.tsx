export default function Home() {
  return (
    <main className="home-shell">
      <div className="home-card">
        <div className="foundation-kicker">CODEINTEX LEARNING</div>
        <h1>Learning experience foundation</h1>
        <p>
          The product is pulling the design system from real learner needs,
          not from a speculative component catalog.
        </p>
        <div className="home-actions">
          <a
            className="cx-button cx-button--primary"
            href="/learn/backend-engineering"
          >
            Open Learning Player →
          </a>
          <a className="cx-button cx-button--secondary" href="/dev/ui">
            UI foundation
          </a>
        </div>
      </div>
    </main>
  );
}
