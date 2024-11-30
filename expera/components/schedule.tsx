"use client";

import { useEffect, useState } from 'react';
import axios from 'axios';

interface Schedule {
  id: number;
  code: string;
  day_of_week: number;
  start_time: string;
  end_time: string;
}

export default function SchedulePage() {
  const [schedules, setSchedules] = useState<Schedule[]>([]);
  const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    const fetchSchedules = async () => {
      try {
        const { data } = await axios.get<Schedule[]>(`${BACKEND_URL}/schedules`);
        setSchedules(data);
      } catch (error) {
        console.error('Error fetching schedules:', error);
      }
    };
    fetchSchedules();
  }, []);

  const formatTime = (time: string) => time.substring(0, 5);

  const getClass = (timeSlot: string, day: number) => {
    const [startTime, endTime] = timeSlot.split('-');
    return schedules.find(
      schedule =>
        formatTime(schedule.start_time) === startTime &&
        formatTime(schedule.end_time) === endTime &&
        schedule.day_of_week === day
    )?.code || '';
  };

  const timeSlots = [
    '08:00-09:00',
    '09:10-10:10',
    '10:20-11:20',
    '11:30-12:30'
  ];

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
        <h1 className="font-pixel text-3xl text-pink-400 mb-8">Schedule</h1>
        <div className="backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 p-6">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-purple-900/50">
                <tr>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Time</th>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Monday</th>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Tuesday</th>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Wednesday</th>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Thursday</th>
                  <th className="border border-purple-500/20 px-4 py-2 font-pixel">Friday</th>
                </tr>
              </thead>
              <tbody>
                {timeSlots.map((timeSlot) => (
                  <tr key={timeSlot}>
                    <td className="border border-purple-500/20 px-4 py-2 font-mono">{timeSlot}</td>
                    {[1, 2, 3, 4, 5].map((day) => {
                      const classCode = getClass(timeSlot, day);
                      return (
                        <td 
                          key={`${timeSlot}-${day}`} 
                          className={`border border-purple-500/20 px-4 py-2 text-center font-mono
                            ${classCode ? 'bg-pink-500/10' : ''}`}
                        >
                          {classCode}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}