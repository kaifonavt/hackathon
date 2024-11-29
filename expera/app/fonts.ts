import localFont from 'next/font/local'

export const pixelFont = localFont({
  src: [
    {
      path: '../public/fonts/pixel.ttf',
      weight: '400',
      style: 'normal',
    },
    {
      path: '../public/fonts/pixel-bold.ttf',
      weight: '700',
      style: 'normal',
    }
  ],
  variable: '--font-pixel'
})