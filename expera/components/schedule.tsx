"use client"

import { useEffect, useState } from 'react';
import axios from 'axios';

interface Schedule {
  id: number;
  code: string;
  day_of_week: number;
  start_time: string;
  end_time: string;
}

const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:8000";

const ScheduleTable = () => {
  const [schedules, setSchedules] = useState<Schedule[]>([]);

  useEffect(() => {
    const fetchSchedules = async () => {
      try {
        const response = await axios.get(`${BACKEND_URL}/schedules`);
        setSchedules(response.data);
      } catch (error) {
        console.error('Error fetching schedules:', error);
      }
    };

    fetchSchedules();
  }, []);

  // Helper function to format time from "HH:MM:SS" to "HH:MM"
  const formatTime = (time: string) => time.substring(0, 5);

  // Helper function to get class for a specific time slot and day
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
    <div className="container mx-auto mt-10">
      <table className="w-full table-auto border-collapse border border-gray-300 shadow-lg bg-[#2D1B69] text-white">
        <thead className="bg-[#1E1246]">
          <tr>
            <th className="border border-gray-600 px-4 py-2">Время</th>
            <th className="border border-gray-600 px-4 py-2">Понедельник</th>
            <th className="border border-gray-600 px-4 py-2">Вторник</th>
            <th className="border border-gray-600 px-4 py-2">Среда</th>
            <th className="border border-gray-600 px-4 py-2">Четверг</th>
            <th className="border border-gray-600 px-4 py-2">Пятница</th>
          </tr>
        </thead>
        <tbody>
          {timeSlots.map((timeSlot) => (
            <tr key={timeSlot}>
              <td className="border border-gray-600 px-4 py-2 font-mono">{timeSlot}</td>
              {[1, 2, 3, 4, 5].map((day) => (
                <td key={`${timeSlot}-${day}`} className="border border-gray-600 px-4 py-2 text-center font-mono">
                  {getClass(timeSlot, day)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ScheduleTable;