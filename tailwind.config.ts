import type { Config } from 'tailwindcss'
import typography from '@tailwindcss/typography'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './content/**/*.{md,mdx}',
  ],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '68ch',
            color: '#1e293b',
            fontFamily: "'Inter', ui-sans-serif, system-ui, sans-serif",
            fontSize: '18px',
            lineHeight: '1.85',
            h2: {
              fontSize: '22px',
              fontWeight: '700',
              color: '#0f172a',
              marginTop: '48px',
              marginBottom: '16px',
            },
            h3: {
              fontSize: '18px',
              fontWeight: '600',
              color: '#0f172a',
              marginTop: '32px',
              marginBottom: '12px',
            },
            p: {
              marginBottom: '24px',
              marginTop: '0',
            },
            strong: {
              color: '#0f172a',
              fontWeight: '600',
            },
            blockquote: {
              borderLeftWidth: '3px',
              borderLeftColor: '#0d9488',
              paddingLeft: '20px',
              paddingTop: '4px',
              paddingBottom: '4px',
              color: '#475569',
              fontStyle: 'normal',
              marginTop: '32px',
              marginBottom: '32px',
              quotes: 'none',
              '&::before': { content: 'none' },
              '&::after': { content: 'none' },
            },
            a: {
              color: '#0d9488',
              textDecoration: 'underline',
              textUnderlineOffset: '3px',
              '&:hover': {
                color: '#0f766e',
              },
            },
            'ul, ol': {
              paddingLeft: '24px',
              marginBottom: '24px',
            },
            li: {
              marginBottom: '8px',
              marginTop: '0',
            },
            table: {
              width: '100%',
              borderCollapse: 'collapse',
              fontSize: '15px',
              marginTop: '32px',
              marginBottom: '32px',
            },
            th: {
              backgroundColor: '#f8fafc',
              color: '#0f172a',
              fontWeight: '600',
              textAlign: 'left',
              padding: '10px 14px',
              borderBottomWidth: '2px',
              borderBottomColor: '#e2e8f0',
            },
            td: {
              padding: '10px 14px',
              borderBottomWidth: '1px',
              borderBottomColor: '#e2e8f0',
              color: '#334155',
            },
            code: {
              backgroundColor: '#f1f5f9',
              color: '#0f172a',
              padding: '2px 6px',
              borderRadius: '4px',
              fontSize: '15px',
              fontWeight: 'normal',
              '&::before': { content: 'none' },
              '&::after': { content: 'none' },
            },
          },
        },
      },
    },
  },
  plugins: [typography],
}

export default config
