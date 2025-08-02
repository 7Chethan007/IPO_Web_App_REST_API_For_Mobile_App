import React, { useState, useEffect } from 'react';
import Sidebar from '../../components/Admin/Sidebar';
import Header from '../../components/Admin/Header';
import IPOOverviewChart from '../../components/Admin/Charts/IPOOverviewChart';
import MainBoardChart from '../../components/Admin/Charts/MainBoardChart';
import apiClient from '../../services/apiClient';

export default function DashboardOverview() {
  const [stats, setStats] = useState({
    total_companies: 0,
    total_ipos: 0,
    total_users: 0,
    upcoming_ipos: 0,
    open_ipos: 0,
    listed_ipos: 0,
    recent_companies: 0,
    recent_ipos: 0,
    recent_users: 0
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchAdminStats();
  }, []);

  const fetchAdminStats = async () => {
    try {
      console.log('Fetching admin stats...');
      const data = await apiClient.get('/auth/admin/stats/');
      console.log('Raw response data:', data);
      
      // Transform the nested response to match the expected flat structure
      const transformedStats = {
        total_companies: data.overview?.total_companies || 0,
        total_ipos: data.overview?.total_ipos || 0,
        total_users: data.overview?.total_users || 0,
        upcoming_ipos: data.ipo_status?.upcoming || 0,
        open_ipos: data.ipo_status?.open || 0,
        listed_ipos: data.ipo_status?.listed || 0,
        recent_companies: data.recent_activity?.companies_added || 0,
        recent_ipos: data.recent_activity?.ipos_added || 0,
        total_issue_size: data.overview?.total_issue_size || 0
      };
      
      console.log('Transformed stats:', transformedStats);
      setStats(transformedStats);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching admin stats:', error);
      setError(`Failed to load dashboard data: ${error.message}`);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex">
        <Sidebar />
        <div className="flex-1">
          <Header />
          <div className="p-6 flex justify-center items-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-600"></div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex">
        <Sidebar />
        <div className="flex-1">
          <Header />
          <div className="p-6">
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
              {error}
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <div className="p-6">
          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                      <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3z" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">Total Users</dt>
                      <dd className="text-lg font-medium text-gray-900">{stats.total_users}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
                      <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M4 4a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h4a2 2 0 012 2v2a2 2 0 01-2 2H8a2 2 0 01-2-2v-2z" clipRule="evenodd" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">Total Companies</dt>
                      <dd className="text-lg font-medium text-gray-900">{stats.total_companies}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center">
                      <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clipRule="evenodd" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">Total IPOs</dt>
                      <dd className="text-lg font-medium text-gray-900">{stats.total_ipos}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-8 h-8 bg-yellow-500 rounded-full flex items-center justify-center">
                      <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">Upcoming IPOs</dt>
                      <dd className="text-lg font-medium text-gray-900">{stats.upcoming_ipos}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* IPO Status Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div className="bg-blue-50 overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <h3 className="text-lg font-medium text-blue-800">Open IPOs</h3>
                <p className="text-3xl font-bold text-blue-600">{stats.open_ipos}</p>
                <p className="text-sm text-blue-600">Currently accepting applications</p>
              </div>
            </div>

            <div className="bg-green-50 overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <h3 className="text-lg font-medium text-green-800">Listed IPOs</h3>
                <p className="text-3xl font-bold text-green-600">{stats.listed_ipos}</p>
                <p className="text-sm text-green-600">Successfully listed on exchange</p>
              </div>
            </div>

            <div className="bg-orange-50 overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <h3 className="text-lg font-medium text-orange-800">Recent Activity</h3>
                <p className="text-sm text-orange-600">
                  {stats.recent_companies} new companies, {stats.recent_ipos} new IPOs, {stats.recent_users} new users in last 7 days
                </p>
              </div>
            </div>
          </div>

          {/* Charts */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="bg-white p-4 rounded shadow">
              <IPOOverviewChart />
            </div>
            <div className="bg-white p-4 rounded shadow">
              <MainBoardChart />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}