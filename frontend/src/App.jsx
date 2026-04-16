import React from 'react'
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
function App() {
  return (
    <BrowserRouter>

    <Link to='/' >
      <h2 className='text-xl font-semibold text-gray-900'>Home</h2>
    </Link>

      <Routes>
        <Route path='/' element={<Home />} >Home</Route>
      </Routes>
      
    </BrowserRouter>
  )
}

export default App
