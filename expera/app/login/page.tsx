"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

const BACKEND_URL = process.env.BACKEND_URL || "https://expera-5a7911691b55.herokuapp.com";

export default function LoginPage() {
  const router = useRouter();
  const [mounted, setMounted] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    setMounted(true);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch(`${BACKEND_URL}/users/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        const { access_token } = data;
        
        // Сохранение токена
        localStorage.setItem("access_token", access_token);
        console.log("Saved token:", access_token);

        // Перенаправление
        console.log("Before redirect");
        router.push("/dashboard");
        console.log("After redirect");
      } else {
        const errorData = await response.json();
        setErrorMessage(errorData.message || "Ошибка авторизации.");
      }
    } catch (error) {
      
      setErrorMessage("Ошибка соединения. Проверьте подключение к интернету.");
      console.log(error)
    }
  };

  if (!mounted) {
    return null;
  }

  return (
    <div
      className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
      style={{
        backgroundImage: 'url("/images/main_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <div className="w-full max-w-md">
        <div className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-8">
          <h2 className="font-pixel text-3xl text-white text-center mb-8">
            Логин
          </h2>

          {errorMessage && (
            <div className="bg-red-500/70 text-white font-pixel text-sm rounded-lg px-4 py-2 mb-4">
              {errorMessage}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="email" className="font-pixel text-gray-200 block text-sm mb-2">
                Email
              </label>
              <input
                id="email"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="w-full px-4 py-2 rounded-lg bg-purple-900/50 border border-purple-500/50 text-white font-pixel focus:outline-none focus:border-pink-500 transition"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              />
            </div>

            <div>
              <label htmlFor="password" className="font-pixel text-gray-200 block text-sm mb-2">
                Пароль
              </label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="w-full px-4 py-2 rounded-lg bg-purple-900/50 border border-purple-500/50 text-white font-pixel focus:outline-none focus:border-pink-500 transition"
                value={formData.password}
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              />
            </div>

            <button
              type="submit"
              className="w-full font-pixel text-xl bg-pink-600 text-white px-8 py-3 rounded-lg hover:bg-pink-700 transition transform hover:scale-105 shadow-lg"
            >
              Войти
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="font-pixel text-sm text-gray-300 mb-2">
              Впервые?
            </p>
            <button
              onClick={() => router.push("/register")}
              className="font-pixel text-pink-400 hover:text-pink-300 transition"
            >
              Зарегистрироваться
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
