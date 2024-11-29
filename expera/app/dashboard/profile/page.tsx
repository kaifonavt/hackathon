'use client';

import Link from "next/link";
import Image from "next/image";
import { useState, useEffect } from "react";

interface Course {
  name: string;
  description: string;
  progress: number;
}

export default function ProfilePage() {
  const [contributions, setContributions] = useState<number[][]>([]);
  
  useEffect(() => {
    setContributions(
      Array(52).fill(0).map(() => 
        Array(7).fill(0).map(() => Math.floor(Math.random() * 5))
      )
    );
  }, []);

  const repositories: Course[] = [
    {
      name: "metadata",
      description: "Changing photo metadata",
      progress: 50,
    },
    {
      name: "hackathon",
      description: "Hackathon project",
      progress: 100,
    },
  ];

  return (
    <div
      className="min-h-screen text-white w-full bg-gradient-to-b from-purple-950 to-black pt-12"
      style={{
        backgroundImage: 'url("/images/profile_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-col lg:flex-row gap-8">   
          <div className="w-full lg:w-1/4">
            <div className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-4">
              <Image
                src="/api/placeholder/256/256"
                alt="Profile"
                width={256}
                height={256}
                className="rounded-full mb-4"
              />
              <h1 className="font-pixel text-2xl text-pink-400 mb-2">Username</h1>
              <p className="font-pixel text-gray-300 text-sm mb-4">Bio goes here</p>
            </div>
          </div>

          <div className="w-full lg:w-3/4">
          <h2 className="font-pixel text-xl mb-4">Contributions</h2>
            <div className="backdrop-blur-sm bg-purple-950/30 p-6 rounded-xl border border-purple-500/20 mb-8">
              <div className="w-full overflow-x-auto">
                <div className="inline-grid grid-flow-col gap-1 min-w-full pb-4">
                  {contributions.map((week, weekIndex) => (
                    <div key={weekIndex} className="grid grid-rows-7 gap-1">
                      {week.map((count, dayIndex) => (
                        <div
                          key={`${weekIndex}-${dayIndex}`}
                          className={`w-3 h-3 rounded-sm ${
                            count === 0 ? "bg-purple-950/50" :
                            count === 1 ? "bg-pink-900" :
                            count === 2 ? "bg-pink-800" :
                            count === 3 ? "bg-pink-700" :
                            "bg-pink-600"
                          }`}
                        />
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            </div>
            <h2 className="font-pixel text-xl mb-4">Courses</h2>
            <div className="space-y-4">
              {repositories.map((repo) => (
                <div
                  key={repo.name}
                  className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-6"
                >
                  <div className="flex justify-between items-start mb-4">
                    <Link
                      href={`/repo/${repo.name}`}
                      className="font-pixel text-pink-400 hover:underline"
                    >
                      {repo.name}
                    </Link>
                    <span className="text-xs text-gray-400 px-2 py-1 rounded-full border border-gray-700">
                      Public
                    </span>
                  </div>
                  <p className="text-gray-300 mb-4">{repo.description}</p>
                  <div className="w-full bg-gray-700 rounded-full h-2.5">
                    <div 
                      className="bg-pink-500 h-2.5 rounded-full transition-all duration-300"
                      style={{ width: `${repo.progress}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}