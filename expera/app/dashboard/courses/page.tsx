'use client';

import Link from "next/link";

interface Course {
  id: string;
  name: string;
  description: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  progress: number;
  isStarted: boolean;
}

export default function CoursesPage() {
  const courses: Course[] = [
    {
      id: "python-basics",
      name: "Python Basics",
      description: "Learn the fundamentals of Python programming for robotic manipulations",
      difficulty: "Beginner",
      progress: 0,
      isStarted: false,
    },
    {
      id: "web-dev",
      name: "Web Development",
      description: "Master HTML, CSS, and JavaScript for UI comercial robotic interactions",
      difficulty: "Intermediate",
      progress: 30,
      isStarted: true,
    },
    {
      id: "ml-intro",
      name: "Machine Learning",
      description: "Introduction to ML algorithms and let AI into robotics",
      difficulty: "Advanced",
      progress: 0,
      isStarted: false,
    }
  ];

  const getDifficultyColor = (difficulty: Course['difficulty']) => {
    switch (difficulty) {
      case 'Beginner':
        return 'text-green-400';
      case 'Intermediate':
        return 'text-yellow-400';
      case 'Advanced':
        return 'text-red-400';
    }
  };

  return (
    <div className="min-h-screen w-full text-white bg-gradient-to-b from-purple-950 to-black pt-24"
      style={{
        backgroundImage: 'url("/images/profile_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}>
      <div className="container mx-auto px-4">
        <h1 className="font-pixel text-3xl text-white mb-8">Available Courses</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {courses.map((course) => (
            <Link href={`/dashboard/courses/${course.id}`} key={course.id}>
              <div className="backdrop-blur-sm bg-purple-950/30 border border-purple-500/20 hover:bg-purple-900/30 transition-colors cursor-pointer rounded-lg overflow-hidden">
                <div className="p-6">
                  <h2 className="font-pixel text-xl text-pink-400 mb-4">{course.name}</h2>
                  <p className="text-gray-300 mb-4">{course.description}</p>
                  <div className="flex justify-between text-sm mb-4">
                    <span className={getDifficultyColor(course.difficulty)}>
                      {course.difficulty}
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
}