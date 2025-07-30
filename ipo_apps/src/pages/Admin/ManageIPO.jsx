import React, { useState } from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import IPOForm from '../../components/Admin/IPO/IPOForm';
import IPOList from '../../components/Admin/IPO/IPOList';

const ManageIPO = () => {
  const [ipoList, setIpoList] = useState([]);
  const [isFormVisible, setFormVisible] = useState(false);

  const handleAddIPO = (ipo) => {
    setIpoList((prev) => [...prev, ipo]); // Add IPO to local state
    setFormVisible(false);
  };

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold">Upcoming IPO Information</h2>
            <button onClick={() => setFormVisible(true)} className="bg-blue-600 text-white px-4 py-2 rounded">
              Register IPO
            </button>
          </div>

          {isFormVisible ? (
            <IPOForm onSubmit={handleAddIPO} onCancel={() => setFormVisible(false)} />
          ) : (
            <IPOList ipoList={ipoList} />
          )}
        </div>
      </div>
    </div>
  );
};

export default ManageIPO;