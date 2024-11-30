import { pixelFont } from './fonts'
import Navigation from '@/components/navigation'
import {AuthProvider} from '@/context/AuthContext'
import './globals.css'

export const metadata = {
  title: 'Expera',
  description: 'Future of robotics',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={pixelFont.variable}>
      <body className="font-pixel">
        <AuthProvider>
          <Navigation />
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
