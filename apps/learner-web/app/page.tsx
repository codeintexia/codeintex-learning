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
            href="/courses/backend-engineering"
          >
            View backend course →
          </a>
          <a className="cx-button cx-button--secondary" href="/my-learning">
            My Learning
          </a>
        </div>
      </div>
    </main>
  );
}
