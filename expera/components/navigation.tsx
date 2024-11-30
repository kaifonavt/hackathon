'use client';

import Link from "next/link";
const nigga = true
const Navigation = () => {
  return (
    <nav className="bg-purple-900/50 backdrop-blur-sm fixed w-full z-50">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <Link href="/" className="text-3xl font-pixel font-bold text-white">
              EXPERA
            </Link>
          </div>
          <div className="hidden md:flex items-center space-x-8">
            <Link
              href="/dashboard"
              className="font-pixel text-white hover:text-pink-400 transition"
            >
              Home
            </Link>
            <Link
              href="/dashboard/schedule"
              className="font-pixel text-white hover:text-pink-400 transition"
            >
              Schedule
            </Link>
            <Link
              href="/dashboard/courses"
              className="font-pixel text-white hover:text-pink-400 transition"
            >
              Courses
            </Link>
            {nigga ? (
              <Link
                href="/dashboard/profile"
                className="font-pixel text-white hover:text-pink-400 transition"
              >
                Profile
              </Link>
            ) : (
              <Link
                href="/login"
                className="font-pixel text-white hover:text-pink-400 transition"
              >
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;