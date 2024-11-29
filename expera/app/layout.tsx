import { pixelFont } from './fonts'
import Navigation from '@/components/navigation'
import './globals.css'

export const metadata = {
  title: 'Expera - Gaming Store',
  description: 'Your one-stop gaming store',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={pixelFont.variable}>
      <body className="font-pixel">
        <Navigation />
        {children}
      </body>
    </html>
  )
}