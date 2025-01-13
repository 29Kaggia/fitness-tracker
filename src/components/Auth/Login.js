import React, { useState } from 'react';
import api from '../../utils/api';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      const response = await api.post('/auth/login', { email, password });
      localStorage.setItem('token', response.data.token);
      window.location.href = '/dashboard'; // Redirect to dashboard
    } catch (err) {
      setError('Invalid email or password');
    }
  };

  return (
    <div className="bg-gray-100 min-h-screen flex justify-center items-center">
      <form className="bg-white shadow-lg rounded-lg p-8">
        <h2 className="text-2xl font-bold text-center mb-4">Login</h2>
        {error && <p className="text-red-500 text-center">{error}</p>}
        <input
          type="email"
          placeholder="Email"
          className="border px-4 py-2 w-full rounded-md mb-4"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          className="border px-4 py-2 w-full rounded-md mb-4"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          className="bg-blue-600 text-white w-full py-2 rounded-md"
          onClick={(e) => {
            e.preventDefault();
            handleLogin();
          }}
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
