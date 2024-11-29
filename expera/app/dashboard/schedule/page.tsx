import ScheduleTable from "@/components/schedule";
import Image from 'next/image';

export default function Home() {
  return (
    <div
      className="min-h-screen text-white flex items-center justify-center py-12 px-4 sm:px-6 "
      style={{
        backgroundImage: 'url("/images/schedule_back.png")',
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >          <div className="flex gap-8 items-center">
        <div className="flex-1 backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 h-[400px] flex flex-col">
        <div className="flex-1 flex items-center justify-center p-4">
          <Image
            src="/images/coin.png"
            alt="Educational Platform"
            className="max-h-[400px] w-auto object-contain"
            style={{
              filter: "drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.3))",
            }}
          />
        </div>
      </div>
      <div className="flex-1 backdrop-blur-sm bg-purple-950/30 rounded-xl border border-purple-500/20 h-[400px] flex flex-col">
        <div className="flex flex-col items-center justify-center">
          <h1 className="text-3xl font-bold mb-5">Расписание занятий</h1>
          <ScheduleTable />
        </div>
      </div>
      
    </div></div>    
  );
}
