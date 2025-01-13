import React from 'react';
import { BrowserRouter as Router, Routes, Route, Switch } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import Login from './components/Auth/Login';
import Dashboard from './pages/Dashboard';import DietLog from './components/Diet/DietLog';


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/diet" component={DietLog} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
};

export default App;
