export type ProgressProps = {
  value: number;
  label?: string;
};

export function Progress({ value, label = "Progress" }: ProgressProps) {
  const normalized = Math.min(100, Math.max(0, value));

  return (
    <div className="cx-progress" aria-label={`${label}: ${normalized}%`}>
      <div className="cx-progress__track" aria-hidden="true">
        <div className="cx-progress__value" style={{ width: `${normalized}%` }} />
      </div>
      <span className="cx-progress__text">{normalized}%</span>
    </div>
  );
}
