import React from 'react';
import { NavLink } from 'react-router-dom';
const Sidebar = () => (
  <aside className="w-60 bg-gray-50 h-screen p-4">
    <h2 className="font-bold text-lg mb-8">Bluestock Fintech</h2>
    <nav className="space-y-2">
      <NavLink to="/admin/dashboard" className={({isActive}) => isActive ? 'block p-2 bg-indigo-100 rounded' : 'block p-2'}>Dashboard</NavLink>
      <NavLink to="/admin/manage-ipo" className={({isActive}) => isActive ? 'block p-2 bg-indigo-100 rounded' : 'block p-2'}>Manage IPO</NavLink>
      <NavLink to="/admin/register-ipo" className={({isActive}) => isActive ? 'block p-2 bg-indigo-100 rounded' : 'block p-2'}>Register IPO</NavLink>
      <NavLink to="/admin/subscription" className="block p-2 text-gray-400">IPO Subscription</NavLink>
      <NavLink to="/admin/allotment" className="block p-2 text-gray-400">IPO Allotment</NavLink>
    </nav>
  </aside>
);
export default Sidebar;