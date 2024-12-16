// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import {  BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import Header from './components/Header';




function App() {


  return (
    <div className="app-container">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route element={<HomePage />} path="/" />
          <Route element={<LoginPage />} path="/login" />
          {/* <Route element={<ProtectedRoute isAuth={!!profileID} />}>

</Route> */}
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
