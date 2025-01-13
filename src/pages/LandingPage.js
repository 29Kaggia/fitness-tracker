import React from 'react';

const LandingPage = () => {
  return (
    <div className="bg-gray-100 min-h-screen flex flex-col justify-center items-center">
      <h1 className="text-4xl font-bold text-blue-600">Welcome to Fitness Tracker</h1>
      <p className="mt-4 text-gray-600">Track your fitness journey effortlessly.</p>
      <div className="mt-8">
        <button className="bg-blue-600 text-white px-6 py-2 rounded-md mx-2">Login</button>
        <button className="bg-green-500 text-white px-6 py-2 rounded-md mx-2">Signup</button>
      </div>
    </div>
  );
};

export default LandingPage;
