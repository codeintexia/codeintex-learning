'use client'
import { useEffect, useState } from 'react'

// ReadingProgress client component renders a thin teal progress bar fixed at the top of the viewport
export function ReadingProgress() {
  const [progress, setProgress] = useState(0)
  
  useEffect(() => {
    // Calculates scroll percentage as the user moves down the lesson page
    const updateProgress = () => {
      const scrollTop = window.scrollY
      const docHeight = document.documentElement.scrollHeight - window.innerHeight
      const progressVal = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0
      setProgress(progressVal)
    }
    window.addEventListener('scroll', updateProgress)
    return () => window.removeEventListener('scroll', updateProgress)
  }, [])
  
  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        height: '3px',
        width: `${progress}%`,
        backgroundColor: '#0d9488',
        zIndex: 100,
        transition: 'width 100ms linear',
      }}
    />
  )
}
