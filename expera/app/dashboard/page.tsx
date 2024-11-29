"use client";
import { useRouter } from "next/navigation";

export default function Home() {
  return (
    <div
      className="min-h-screen relative flex items-center"
      style={{
        backgroundImage: 'url("images/main_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <div className="relative w-full">
        <div className="max-w-7xl mx-auto px-4 py-24">
          <div className="flex gap-8 items-center">
            <div className="w-[720px]">
              <div className="backdrop-blur-sm bg-purple-950/30 p-8 rounded-xl border border-purple-500/20 h-[400px] flex items-center">
                <div className="space-6">
                  <p className="font-pixel text-xl text-gray-100 leading-relaxed">
                    Мы живем в эпоху, где традиционное образование сталкивается
                    с новыми вызовами.
                  </p>
                  <p className="font-pixel text-xl text-gray-100 leading-relaxed">
                    Expera — это уникальная платформа, разработанная, чтобы
                    вдохновлять учеников, поддерживать их мотивацию и
                    обеспечивать качественное образование с помощью современных
                    технологий.
                  </p>
                </div>
              </div>
            </div>

            <div className="flex-1 backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 h-[400px] flex flex-col">
              <div className="flex-1 flex items-center justify-center p-4">
                <img
                  src="/images/hero-boy.png"
                  alt="Educational Platform"
                  className="max-h-[400px] w-auto object-contain"
                  style={{
                    filter: "drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.3))",
                  }}
                />
              </div>
            </div>
          </div>
          <div className="p-4 text-center space-y-2">
            <div className="text-sm space-y-1">
              <p className="font-pixel text-gray-300">Впервые?</p>
              <a
                href="/register"
                className="font-pixel text-pink-400 hover:text-pink-300 transition"
              >
                Зарегистрироваться
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
