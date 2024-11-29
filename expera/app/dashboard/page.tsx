"use client";
import Image from "next/image";
interface Student {
  name: string;
  skillPoints: number;
  rank: number;
}

interface StreakStats {
  currentStreak: number;
  bestStreak: number;
  totalDays: number;
  lastActive: string;
}

export default function StreakPage() {
  const streakData: StreakStats = {
    currentStreak: 7,
    bestStreak: 14,
    totalDays: 45,
    lastActive: "Today",
  };

  const getStreakImage = (streak: number) => {
    if (streak < 1) return "/fires/1.png";
    if (streak < 10) return "/fires/2.png";
    return "/fires/3.png";
  };
  const topStudents: Student[] = [
    { name: "Alex", skillPoints: 2500, rank: 1 },
    { name: "Maria", skillPoints: 2350, rank: 2 },
    { name: "John", skillPoints: 2200, rank: 3 },
    { name: "Sara", skillPoints: 2100, rank: 4 },
    { name: "Mike", skillPoints: 2000, rank: 5 },
    { name: "Lisa", skillPoints: 1950, rank: 6 },
    { name: "David", skillPoints: 1900, rank: 7 },
    { name: "Emma", skillPoints: 1850, rank: 8 },
    { name: "James", skillPoints: 1800, rank: 9 },
    { name: "Anna", skillPoints: 1750, rank: 10 },
  ];

  return (
    <div
      className="min-h-screen w-full text-white bg-gradient-to-b from-purple-950 to-black pt-12"
      style={{
        backgroundImage: 'url("/images/profile_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-6">
            <h2 className="font-pixel text-2xl text-pink-400 mb-6">
              Your Streak
            </h2>
            <div className="grid grid-cols-2 gap-6">
              <div className="text-center">
                <div className="font-pixel text-4xl text-pink-400 mb-2">
                  {streakData.currentStreak}
                </div>
                <div className="text-gray-300">Current Streak</div>
              </div>
              <div className="text-center">
                <div className="font-pixel text-4xl text-pink-400 mb-2">
                  {streakData.bestStreak}
                </div>
                <div className="text-gray-300">Best Streak</div>
              </div>
              <div className="text-center">
                <div className="font-pixel text-4xl text-pink-400 mb-2">
                  {streakData.totalDays}
                </div>
                <div className="text-gray-300">Total Days</div>
              </div>
              <div className="text-center">
                <div className="font-pixel text-xl text-pink-400 mb-2">
                  {streakData.lastActive}
                </div>
                <div className="text-gray-300">Last Active</div>
              </div>
            </div>
            <div>
              <Image
                src={getStreakImage(streakData.currentStreak)}
                width={400}
                height={400}
                alt={`Streak: ${streakData.currentStreak} days`}
                className="max-h-[400px] w-auto object-contain"
              />
            </div>
          </div>

          <div className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-6">
            <h2 className="font-pixel text-2xl text-pink-400 mb-6">
              Top Students
            </h2>
            <div className="space-y-4">
              {topStudents.map((student) => (
                <div
                  key={student.rank}
                  className="flex items-center justify-between p-3 rounded-lg bg-purple-900/30 hover:bg-purple-800/30 transition-colors"
                >
                  <div className="flex items-center gap-4">
                    <span className="font-pixel text-xl w-8">
                      {student.rank}
                    </span>
                    <span className="font-pixel text-lg">{student.name}</span>
                  </div>
                  <div className="font-pixel text-pink-400">
                    {student.skillPoints}
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
