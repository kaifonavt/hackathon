'use client';
import { useAuth } from '@/context/AuthContext';
import Link from "next/link";

const Navigation = () => {
  const { isLoggedIn } = useAuth();

  return (
    <nav className="bg-purple-900/50 backdrop-blur-sm fixed w-full z-50 shadow-lg">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          {/* Логотип */}
          <div className="flex items-center">
            <Link href="/">
              <a className="text-3xl font-pixel font-bold text-white">
                EXPERA
              </a>
            </Link>
          </div>

          {/* Навигация */}
          <div className="hidden md:flex items-center space-x-8">
            <Link href="/dashboard">
              <a className="font-pixel text-white hover:text-pink-400 transition">
                Home
              </a>
            </Link>
            <Link href="/dashboard/schedule">
              <a className="font-pixel text-white hover:text-pink-400 transition">
                Schedule
              </a>
            </Link>
            <Link href="/dashboard/courses">
              <a className="font-pixel text-white hover:text-pink-400 transition">
                Courses
              </a>
            </Link>
            {isLoggedIn ? (
              <Link href="/dashboard/profile">
                <a className="font-pixel text-white hover:text-pink-400 transition">
                  Profile
                </a>
              </Link>
            ) : (
              <Link href="/login">
                <a className="font-pixel text-white hover:text-pink-400 transition">
                  Login
                </a>
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
