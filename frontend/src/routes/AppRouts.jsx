import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from '../pages/Home'
import Error404 from '../pages/Error404'
import Analyzer from '../pages/Analyzer'

function AppRouts() {
  return (
    <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/' element={<Analyzer />}></Route>
        <Route path='*' element={<Error404 />}></Route>
    </Routes>
  )
}

export default AppRouts
