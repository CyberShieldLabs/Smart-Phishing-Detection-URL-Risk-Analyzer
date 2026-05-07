import React from 'react'
import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Error404 from './pages/Error404';
import AppRouts from './routes/AppRouts';
function App() {
  return (
    <Router>
      <div className='w-full min-h-[100vh] bg-amber-100'>
        <div>
          <AppRouts />
        </div>
      </div>
    </Router>
  )
}

export default App
