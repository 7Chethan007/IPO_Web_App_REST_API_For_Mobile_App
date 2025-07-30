import React from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import IPOOverviewChart from '../../components/Admin/Charts/IPOOverviewChart';
import MainBoardChart from '../../components/Admin/Charts/MainBoardChart';

export default function DashboardOverview() {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6 grid grid-cols-2 gap-6">
          <div className="bg-white p-4 rounded shadow"><IPOOverviewChart /></div>
          <div className="bg-white p-4 rounded shadow"><MainBoardChart /></div>
        </div>
      </div>
    </div>
  );
}