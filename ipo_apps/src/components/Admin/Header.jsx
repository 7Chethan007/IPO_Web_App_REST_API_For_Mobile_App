import React from 'react';
export default function Header() {
  return (
    <header className="flex items-center justify-between p-4 bg-white shadow-sm">
      <input
        type="text"
        placeholder="Search"
        className="flex-1 mx-4 px-3 py-2 border rounded-lg"
      />
      <div className="flex items-center space-x-4">
        <span>Hi, Vishal</span>
        <button><i className="fas fa-bell text-gray-500"></i></button>
      </div>
    </header>
  );
}