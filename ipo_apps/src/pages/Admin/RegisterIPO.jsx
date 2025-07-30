import React, { useState } from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import RegisterIPOForm from '../../components/Admin/Forms/RegisterIPOForm';

export default function RegisterIPO() {
  const handleSubmit = data => console.log('Registering IPO:', data);
  const handleCancel = () => console.log('Cancel');

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6 bg-gray-50 min-h-screen">
          <h1 className="text-xl font-semibold mb-4">IPO Information</h1>
          <RegisterIPOForm onSubmit={handleSubmit} onCancel={handleCancel} />
        </div>
      </div>
    </div>
  );
}