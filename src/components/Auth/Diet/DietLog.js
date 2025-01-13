import React, { useState, useEffect } from 'react';
import api from '../../utils/api';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from 'recharts';

// Process logs for chart
const processChartData = (logs) => {
  return logs.map((log) => ({
    date: log.date,
    calories: parseInt(log.calories, 10),
  }));
};

const DietLog = () => {
  const [foodItem, setFoodItem] = useState('');
  const [calories, setCalories] = useState('');
  const [date, setDate] = useState('');
  const [logs, setLogs] = useState([]);

  // Fetch diet logs
  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const response = await api.get('/diet/');
        setLogs(response.data.logs);
      } catch (err) {
        console.error('Error fetching diet logs:', err);
      }
    };
    fetchLogs();
  }, []);

  // Add a diet log
  const handleAddLog = async () => {
    try {
      const response = await api.post('/diet/', { food_item: foodItem, calories, date });
      setLogs([...logs, response.data]); // Update the logs state
      setFoodItem('');
      setCalories('');
      setDate('');
    } catch (err) {
      console.error('Error adding diet log:', err);
    }
  };

  return (
    <div className="bg-gray-50 min-h-screen p-8">
      <h1 className="text-2xl font-bold mb-4">Diet Tracker</h1>
      <form className="bg-white p-6 shadow-md rounded-md">
        <div className="mb-4">
          <label className="block text-gray-700">Food Item</label>
          <input
            type="text"
            className="border px-4 py-2 w-full rounded-md"
            value={foodItem}
            onChange={(e) => setFoodItem(e.target.value)}
            placeholder="E.g., Apple"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Calories</label>
          <input
            type="number"
            className="border px-4 py-2 w-full rounded-md"
            value={calories}
            onChange={(e) => setCalories(e.target.value)}
            placeholder="E.g., 95"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Date</label>
          <input
            type="date"
            className="border px-4 py-2 w-full rounded-md"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
        </div>
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded-md"
          type="button"
          onClick={handleAddLog}
        >
          Add Diet Log
        </button>
      </form>

      <h2 className="text-xl font-bold mt-8">Diet Logs</h2>
      <ul className="mt-4">
        {logs.map((log, index) => (
          <li key={index} className="border-b py-2">
            {log.date}: {log.food_item} - {log.calories} kcal
          </li>
        ))}
      </ul>

      <h2 className="text-xl font-bold mt-8">Calories Over Time</h2>
      <div className="mt-4 bg-white p-6 shadow-md rounded-md">
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={processChartData(logs)}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="calories" stroke="#8884d8" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default DietLog;
