'use client';

import { useEffect, useState } from 'react';
import Link from "next/link";
import axios from 'axios';

const Navigation = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const BACKEND_URL = process.env.BACKEND_URL || "https://expera-5a7911691b55.herokuapp.com";

  useEffect(() => {
    const verifyToken = async () => {
      if (typeof window === 'undefined') return;
      
      const access_token = localStorage.getItem('access_token');
      
      if (!access_token) {
        setIsLoggedIn(false);
        return;
      }

      try {
        await axios.get(`${BACKEND_URL}/users/verify-token`, {
          headers: {
            'Authorization': `Bearer ${access_token}`
          }
        });
        setIsLoggedIn(true);
      } catch (error) {
        console.error('Token verification failed:', error);
        setIsLoggedIn(false);
        localStorage.removeItem('access_token');
      }
    };

    verifyToken();
  }, []);

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
            {isLoggedIn ? (
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