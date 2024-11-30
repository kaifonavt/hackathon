"use client"
import React, { useState, useEffect } from 'react';
import Link from "next/link";
import axios from 'axios';

interface Course {
  id: number;
  title: string;
  description: string;
  duration_weeks: number;
  total_lessons: number;
  instructor_id: number;
}

const CoursesDisplay = () => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  const BACKEND_URL = process.env.BACKEND_URL || "https://expera-5a7911691b55.herokuapp.com";

  useEffect(() => {
    const fetchCourses = async () => {
      if (typeof window === 'undefined') return;
      
      const access_token = localStorage.getItem('access_token');
      
      try {
        const response = await axios.get<Course[]>(`${BACKEND_URL}/courses`, {
          headers: {
            'Authorization': `Bearer ${access_token}`
          }
        });
        setCourses(response.data);
      } catch (err) {
        const error = err as any;
        setError(error.response?.data?.detail || error.message || 'Failed to fetch courses');
        if (error.response?.status === 401) {
          localStorage.removeItem('access_token');
        }
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen w-full text-white bg-gradient-to-b from-purple-950 to-black pt-24">
        <div className="container mx-auto px-4 flex justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-500" />
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen w-full text-white bg-gradient-to-b from-purple-950 to-black pt-24">
        <div className="container mx-auto px-4">
          <div className="text-red-400">Error loading courses: {error}</div>
        </div>
      </div>
    );
  }

  return (
    <div 
      className="min-h-screen w-full text-white bg-gradient-to-b from-purple-950 to-black pt-24"
      style={{
        backgroundImage: 'url("/images/profile_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <div className="container mx-auto px-4">
        <h1 className="font-pixel text-3xl text-white mb-8">Available Courses</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {courses.map((course) => (
            <Link href={`/dashboard/courses/${course.id}`} key={course.id}>
              <div className="backdrop-blur-sm bg-purple-950/30 border border-purple-500/20 hover:bg-purple-900/30 transition-all duration-300 cursor-pointer rounded-lg overflow-hidden group">
                <div className="p-6">
                  <h2 className="font-pixel text-xl text-pink-400 mb-4 group-hover:translate-x-1 transition-transform">
                    {course.title}
                  </h2>
                  
                  <p className="text-gray-300 mb-4">{course.description}</p>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-300">
                      {course.total_lessons} lessons
                    </span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CoursesDisplay;