import React, { useState } from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import IPOTable from '../../components/Admin/Table/IPOTable';

const sampleData = [
  { company:'Adani Power', priceBand:'₹329-136', openDate:'2023-06-03', closeDate:'2024-06-05', issueSize:'45530.15 Cr.', issueType:'Book Built', listingDate:'2023-06-10', status:'Ongoing', statusColor:'green' },
  // ... more rows
];

export default function ManageIPO() {
  const [data, setData] = useState(sampleData);
  const handleUpdate = ipo => console.log('Update', ipo);
  const handleDelete = ipo => setData(d=>d.filter(x=>x!==ipo));
  const handleView = ipo => console.log('View', ipo);

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6">
          <div className="flex justify-between items-center mb-4">
            <h1 className="text-xl font-semibold">Upcoming IPO | Dashboard</h1>
            <button className="bg-indigo-600 text-white px-4 py-2 rounded">Register IPO</button>
          </div>
          <IPOTable
            items={data}
            onUpdate={handleUpdate}
            onDelete={handleDelete}
            onView={handleView}
          />
        </div>
      </div>
    </div>
  );
}