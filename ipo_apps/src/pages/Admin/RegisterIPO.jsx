import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import RegisterIPOForm from '../../components/Admin/Forms/RegisterIPOForm';

export default function RegisterIPO() {
  const navigate = useNavigate();
  const [notification, setNotification] = useState('');

  const handleSubmit = (data) => {
    console.log('IPO registered successfully:', data);
    setNotification('IPO registered successfully!');
    
    // Clear notification after 3 seconds
    setTimeout(() => {
      setNotification('');
    }, 3000);
  };

  const handleCancel = () => {
    navigate('/admin/dashboard');
  };

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6 bg-gray-50 min-h-screen">
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-gray-900">Register New IPO</h1>
            <p className="text-gray-600 mt-2">Fill in the details to register a new IPO offering</p>
          </div>
          
          {notification && (
            <div className="mb-6 bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg">
              {notification}
            </div>
          )}
          
          <RegisterIPOForm onSubmit={handleSubmit} onCancel={handleCancel} />
        </div>
      </div>
    </div>
  );
}