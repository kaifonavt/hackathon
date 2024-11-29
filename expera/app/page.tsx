export default function Home() {
  return (
    <div className="min-h-screen relative"
         style={{
           backgroundImage: 'url("images/main_back.png")',
           backgroundSize: 'cover',
           backgroundPosition: 'center',
           backgroundRepeat: 'no-repeat',
           backgroundAttachment: 'fixed'
         }}>
      <div className="absolute inset-0 bg-purple-950/70" />
    </div>
  );
}