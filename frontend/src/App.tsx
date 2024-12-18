// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import Header from './components/Header';
import ProtectedRoute from './components/ProtectedRoute/ProtectedRoute';
import useStore from './store/store'


function App() {
  const {
    profileID} = useStore(state => (state)) 

  return (
    <div className="app-container">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route element={<LoginPage />} path="/login" />
          <Route element={<ProtectedRoute  isAuth={!!profileID}/>}>
            <Route element={<HomePage />} path="/" />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
