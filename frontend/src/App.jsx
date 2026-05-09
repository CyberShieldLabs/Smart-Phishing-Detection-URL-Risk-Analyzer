import React from 'react'
import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Error404 from './pages/Error404';
import AppRouts from './routes/AppRouts';
function App() {
  return (
    <>
      <div>
        <AppRouts />
      </div>
    </>
  )
}

export default App
