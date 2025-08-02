import React, { useState, useEffect } from 'react';
import ipoService from '../../../services/ipoService';
import companyService from '../../../services/companyService';

export default function RegisterIPOForm({ initialData = {}, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    company: '',
    issue_size: '',
    price_range_min: '',
    price_range_max: '',
    open_date: '',
    close_date: '',
    listing_date: '',
    board: 'MAIN',
    status: 'UPCOMING',
    lot_size: '',
    ...initialData
  });

  const [companies, setCompanies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    fetchCompanies();
  }, []);

  const fetchCompanies = async () => {
    try {
      const companiesData = await companyService.getAllCompanies();
      setCompanies(companiesData.results || companiesData);
    } catch (error) {
      console.error('Error fetching companies:', error);
      setError('Failed to load companies');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    try {
      // Validate required fields
      const requiredFields = ['company', 'issue_size', 'price_range_min', 'price_range_max', 'open_date', 'close_date', 'listing_date', 'lot_size'];
      const missingFields = requiredFields.filter(field => !formData[field]);
      
      if (missingFields.length > 0) {
        setError(`Please fill in all required fields: ${missingFields.join(', ')}`);
        setLoading(false);
        return;
      }

      // Create the IPO
      const result = await ipoService.createIPO(formData);
      setSuccess('IPO registered successfully!');
      
      // Reset form
      setFormData({
        company: '',
        issue_size: '',
        price_range_min: '',
        price_range_max: '',
        open_date: '',
        close_date: '',
        listing_date: '',
        board: 'MAIN',
        status: 'UPCOMING',
        lot_size: '',
      });

      if (onSubmit) {
        onSubmit(result);
      }
    } catch (error) {
      console.error('Error creating IPO:', error);
      setError(error.response?.data?.error || 'Failed to register IPO. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6 bg-white p-6 rounded-lg shadow">
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}
      {success && (
        <div className="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded">
          {success}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Company Selection */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Company *</label>
          <select
            name="company"
            value={formData.company}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          >
            <option value="">Select a company</option>
            {companies.map(company => (
              <option key={company.id} value={company.id}>
                {company.name}
              </option>
            ))}
          </select>
        </div>

        {/* Issue Size */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Issue Size (₹ Crores) *</label>
          <input
            name="issue_size"
            type="number"
            step="0.01"
            value={formData.issue_size}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., 1000.00"
            required
          />
        </div>

        {/* Price Range Min */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Price Range Min (₹) *</label>
          <input
            name="price_range_min"
            type="number"
            step="0.01"
            value={formData.price_range_min}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., 100.00"
            required
          />
        </div>

        {/* Price Range Max */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Price Range Max (₹) *</label>
          <input
            name="price_range_max"
            type="number"
            step="0.01"
            value={formData.price_range_max}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., 110.00"
            required
          />
        </div>

        {/* Open Date */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Open Date *</label>
          <input
            name="open_date"
            type="date"
            value={formData.open_date}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Close Date */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Close Date *</label>
          <input
            name="close_date"
            type="date"
            value={formData.close_date}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Listing Date */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Expected Listing Date *</label>
          <input
            name="listing_date"
            type="date"
            value={formData.listing_date}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Lot Size */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Lot Size *</label>
          <input
            name="lot_size"
            type="number"
            value={formData.lot_size}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., 100"
            required
          />
        </div>

        {/* Board */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Board</label>
          <select
            name="board"
            value={formData.board}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="MAIN">Main Board</option>
            <option value="SME">SME Board</option>
          </select>
        </div>

        {/* Status */}
        <div className="flex flex-col">
          <label className="text-sm font-medium text-gray-700 mb-2">Status</label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="border border-gray-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="UPCOMING">Upcoming</option>
            <option value="OPEN">Open</option>
            <option value="CLOSED">Closed</option>
            <option value="LISTED">Listed</option>
          </select>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex space-x-4 pt-4">
        <button
          type="submit"
          disabled={loading}
          className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-md font-medium disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Registering...' : 'Register IPO'}
        </button>
        <button
          type="button"
          onClick={onCancel}
          className="border border-gray-300 hover:bg-gray-50 text-gray-700 px-6 py-3 rounded-md font-medium"
        >
          Cancel
        </button>
      </div>
    </form>
  );
}