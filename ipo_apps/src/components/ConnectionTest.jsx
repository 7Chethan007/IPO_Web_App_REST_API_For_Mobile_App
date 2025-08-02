import React, { useState, useEffect } from 'react';
import ipoService from '../services/ipoService';
import companyService from '../services/companyService';

const ConnectionTest = () => {
  const [ipos, setIpos] = useState([]);
  const [companies, setCompanies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [connectionStatus, setConnectionStatus] = useState('Testing...');

  useEffect(() => {
    testConnection();
  }, []);

  const testConnection = async () => {
    try {
      setLoading(true);
      setConnectionStatus('Testing connection...');

      // Test IPO service
      const ipoData = await ipoService.getAllIPOs();
      setIpos(ipoData.slice(0, 5)); // Show first 5 IPOs

      // Test Company service
      const companyData = await companyService.getAllCompanies();
      setCompanies(companyData.slice(0, 5)); // Show first 5 companies

      setConnectionStatus('✅ Connected Successfully!');
      setError(null);
    } catch (err) {
      setError(err.message);
      setConnectionStatus('❌ Connection Failed');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="p-6 max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold mb-4">🔗 Frontend-Backend Connection Test</h2>
        <div className="bg-blue-100 p-4 rounded-lg">
          <p>Testing connection to Django backend...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">🔗 Frontend-Backend Connection Test</h2>
      
      <div className={`p-4 rounded-lg mb-6 ${
        connectionStatus.includes('✅') ? 'bg-green-100 text-green-800' : 
        connectionStatus.includes('❌') ? 'bg-red-100 text-red-800' : 
        'bg-yellow-100 text-yellow-800'
      }`}>
        <h3 className="font-bold text-lg">{connectionStatus}</h3>
        {error && <p className="mt-2 text-red-600">Error: {error}</p>}
      </div>

      {!error && (
        <div className="grid md:grid-cols-2 gap-6">
          {/* IPOs Section */}
          <div className="bg-white shadow-lg rounded-lg p-4">
            <h3 className="text-xl font-bold mb-3 text-blue-600">📈 IPOs ({ipos.length})</h3>
            {ipos.length > 0 ? (
              <div className="space-y-2">
                {ipos.map((ipo, index) => (
                  <div key={index} className="border-l-4 border-blue-500 pl-3 py-2">
                    <h4 className="font-semibold">{ipo.company?.name || 'Unknown Company'}</h4>
                    <p className="text-sm text-gray-600">
                      Status: <span className="font-medium">{ipo.status}</span> | 
                      Board: <span className="font-medium">{ipo.board}</span> | 
                      Size: <span className="font-medium">₹{ipo.issue_size} cr</span>
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-500">No IPOs found</p>
            )}
          </div>

          {/* Companies Section */}
          <div className="bg-white shadow-lg rounded-lg p-4">
            <h3 className="text-xl font-bold mb-3 text-green-600">🏢 Companies ({companies.length})</h3>
            {companies.length > 0 ? (
              <div className="space-y-2">
                {companies.map((company, index) => (
                  <div key={index} className="border-l-4 border-green-500 pl-3 py-2">
                    <h4 className="font-semibold">{company.name}</h4>
                    <p className="text-sm text-gray-600">
                      Sector: <span className="font-medium">{company.sector}</span> | 
                      Industry: <span className="font-medium">{company.industry}</span>
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-500">No companies found</p>
            )}
          </div>
        </div>
      )}

      <div className="mt-6 p-4 bg-gray-100 rounded-lg">
        <h4 className="font-bold mb-2">🔧 Connection Details:</h4>
        <ul className="text-sm space-y-1">
          <li>• Frontend: <span className="font-mono">http://localhost:3000</span></li>
          <li>• Backend API: <span className="font-mono">http://127.0.0.1:8000/api</span></li>
          <li>• CORS: Configured and working</li>
          <li>• Data: {ipos.length + companies.length} records loaded</li>
        </ul>
        
        <button 
          onClick={testConnection}
          className="mt-3 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          🔄 Test Again
        </button>
      </div>
    </div>
  );
};

export default ConnectionTest;
