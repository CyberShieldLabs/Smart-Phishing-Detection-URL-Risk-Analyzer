import React from 'react'
import NavBar from '../components/NavBar'
import AmbBg from '../components/AmbBg'
import Hero from '../components/Hero'
import Footer from '../components/Footer'

function Home() {
  return (
    <div>
      <div className="min-h-screen bg-[#0a0a0b] text-zinc-200 font-sans antialiased selection:bg-zinc-700">
        {/* Background */}
        <AmbBg />

        <div className="relative z-10 m-auto flex min-h-screen max-w-[80%] flex-col px-6 py-10">
          {/* NavBar */}
          <nav>
            <NavBar />
          </nav>
          {/* Hero */}
          <Hero />
          {/* footer */}
          <Footer />
        </div>
      </div>
    </div>
  )
}

export default Home
