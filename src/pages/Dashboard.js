import React, { useEffect, useState } from 'react';
import api from '../utils/api';

const Dashboard = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await api.get('/auth/profile');
        setProfile(response.data);
      } catch (err) {
        console.error('Error fetching profile:', err);
      }
    };
    fetchProfile();
  }, []);

  return (
    <div className="bg-gray-50 min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
      {profile ? (
        <div className="bg-white shadow-md p-6 rounded-lg">
          <h2 className="text-xl font-bold">Welcome, {profile.username}!</h2>
          <p>Email: {profile.email}</p>
        </div>
      ) : (
        <p>Loading profile...</p>
      )}
    </div>
  );
};

export default Dashboard;
