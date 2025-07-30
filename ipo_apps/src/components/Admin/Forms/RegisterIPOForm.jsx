import React, { useState } from 'react';
export default function RegisterIPOForm({ initialData={}, onSubmit, onCancel }) {
  const [data, setData] = useState({ ...initialData });
  const handleChange = e => setData({ ...data, [e.target.name]: e.target.value });
  const handleSubmit = e => { e.preventDefault(); onSubmit(data); };
  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        {['companyName','priceBand','openDate','closeDate','issueSize','issueType','listingDate','status'].map(field => (
          <div key={field} className="flex flex-col">
            <label className="text-sm font-medium capitalize">{field.replace(/([A-Z])/g, ' $1')}</label>
            <input
              name={field}
              value={data[field] || ''}
              onChange={handleChange}
              className="border p-2 rounded" />
          </div>
        ))}
      </div>
      <div className="flex space-x-4">
        <button type="submit" className="bg-indigo-600 text-white px-4 py-2 rounded">Register</button>
        <button type="button" onClick={onCancel} className="border px-4 py-2 rounded">Cancel</button>
      </div>
    </form>
  );
}