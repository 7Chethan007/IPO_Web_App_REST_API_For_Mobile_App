import React, { useState, useEffect } from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import RegisterIPOForm from '../../components/Admin/Forms/RegisterIPOForm';
import ipoService from '../../services/ipoService';

const ManageIPO = () => {
  const [ipoList, setIpoList] = useState([]);
  const [isFormVisible, setFormVisible] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchIPOs();
  }, []);

  const fetchIPOs = async () => {
    try {
      setLoading(true);
      const data = await ipoService.getAllIPOs();
      setIpoList(data.results || data);
      setError('');
    } catch (error) {
      console.error('Error fetching IPOs:', error);
      setError('Failed to load IPOs. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleAddIPO = async (ipo) => {
    await fetchIPOs(); // Refresh the list
    setFormVisible(false);
  };

  const handleUpdateIPO = async (ipoId) => {
    // Handle update IPO functionality
    console.log('Update IPO:', ipoId);
  };

  const handleDeleteIPO = async (ipoId) => {
    if (window.confirm('Are you sure you want to delete this IPO?')) {
      try {
        await ipoService.deleteIPO(ipoId);
        await fetchIPOs(); // Refresh the list
      } catch (error) {
        console.error('Error deleting IPO:', error);
        alert('Failed to delete IPO. Please try again.');
      }
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return '-';
    return new Date(dateString).toLocaleDateString('en-IN');
  };

  const formatCurrency = (amount) => {
    if (!amount) return '-';
    return `₹ ${amount}`;
  };

  const getStatusBadge = (status) => {
    const statusColors = {
      'UPCOMING': 'bg-blue-100 text-blue-800',
      'OPEN': 'bg-green-100 text-green-800',
      'CLOSED': 'bg-yellow-100 text-yellow-800',
      'LISTED': 'bg-gray-100 text-gray-800',
      'WITHDRAWN': 'bg-red-100 text-red-800'
    };
    
    return (
      <span className={`px-2 py-1 rounded-full text-xs font-medium ${statusColors[status] || 'bg-gray-100 text-gray-800'}`}>
        {status}
      </span>
    );
  };

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-semibold text-gray-900">Upcoming IPO Information</h2>
            <button 
              onClick={() => setFormVisible(true)} 
              className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-md font-medium"
            >
              Register IPO
            </button>
          </div>

          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}

          {isFormVisible ? (
            <RegisterIPOForm 
              onSubmit={handleAddIPO} 
              onCancel={() => setFormVisible(false)} 
            />
          ) : (
            <div className="bg-white shadow rounded-lg overflow-hidden">
              {loading ? (
                <div className="p-8 text-center">
                  <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
                  <p className="mt-2 text-gray-600">Loading IPOs...</p>
                </div>
              ) : ipoList.length === 0 ? (
                <div className="p-8 text-center text-gray-500">
                  <p>No IPOs found. Click "Register IPO" to add the first one.</p>
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50">
                      <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Company</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price Band</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Open</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Close</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Issue Size</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Issue Type</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Listing Date</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Delete/View</th>
                      </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                      {ipoList.map((ipo) => (
                        <tr key={ipo.id} className="hover:bg-gray-50">
                          <td className="px-6 py-4 whitespace-nowrap">
                            <div className="text-sm font-medium text-gray-900">
                              {ipo.company_name || ipo.company?.name}
                            </div>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <div className="text-sm text-gray-900">
                              ₹ {ipo.price_range_min} - {ipo.price_range_max}
                            </div>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {formatDate(ipo.open_date)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {formatDate(ipo.close_date)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {ipo.issue_size} Cr.
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {ipo.board === 'MAIN' ? 'Book Built' : 'SME'}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {formatDate(ipo.listing_date)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            {getStatusBadge(ipo.status)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <button
                              onClick={() => handleUpdateIPO(ipo.id)}
                              className="bg-indigo-600 hover:bg-indigo-700 text-white px-3 py-1 rounded text-sm"
                            >
                              Update
                            </button>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <div className="flex space-x-2">
                              <button
                                onClick={() => handleDeleteIPO(ipo.id)}
                                className="bg-red-600 hover:bg-red-700 text-white px-2 py-1 rounded text-sm"
                                title="Delete IPO"
                              >
                                🗑️
                              </button>
                              <button
                                onClick={() => console.log('View IPO:', ipo.id)}
                                className="bg-gray-600 hover:bg-gray-700 text-white px-2 py-1 rounded text-sm"
                                title="View IPO"
                              >
                                👁️
                              </button>
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ManageIPO;