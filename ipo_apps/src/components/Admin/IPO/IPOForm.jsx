// src/components/Admin/IPO/IPOForm.jsx
import React, { useState } from 'react';

const IPOForm = ({ onSubmit, initialData = {}, onCancel }) => {
  const [formData, setFormData] = useState({
    companyName: '',
    priceBand: '',
    openDate: '',
    closeDate: '',
    issueSize: '',
    issueType: '',
    listingDate: '',
    status: '',
    ipoPrice: '',
    listingPrice: '',
    listingGain: '',
    cmp: '',
    currentReturn: '',
    rhp: '',
    drhp: '',
    ...initialData,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData); // This will pass data up to ManageIPO.jsx
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 bg-white rounded shadow">
      <div className="grid grid-cols-2 gap-4">
        <input name="companyName" placeholder="Company Name" value={formData.companyName} onChange={handleChange} className="input" required />
        <input name="priceBand" placeholder="Price Band" value={formData.priceBand} onChange={handleChange} className="input" />
        <input name="openDate" placeholder="Open Date" value={formData.openDate} onChange={handleChange} className="input" />
        <input name="closeDate" placeholder="Close Date" value={formData.closeDate} onChange={handleChange} className="input" />
        <input name="issueSize" placeholder="Issue Size" value={formData.issueSize} onChange={handleChange} className="input" />
        <input name="issueType" placeholder="Issue Type" value={formData.issueType} onChange={handleChange} className="input" />
        <input name="listingDate" placeholder="Listing Date" value={formData.listingDate} onChange={handleChange} className="input" />
        <input name="status" placeholder="Status" value={formData.status} onChange={handleChange} className="input" />
        <input name="ipoPrice" placeholder="IPO Price" value={formData.ipoPrice} onChange={handleChange} className="input" />
        <input name="listingPrice" placeholder="Listing Price" value={formData.listingPrice} onChange={handleChange} className="input" />
        <input name="listingGain" placeholder="Listing Gain" value={formData.listingGain} onChange={handleChange} className="input" />
        <input name="cmp" placeholder="CMP" value={formData.cmp} onChange={handleChange} className="input" />
        <input name="currentReturn" placeholder="Current Return" value={formData.currentReturn} onChange={handleChange} className="input" />
        <input name="rhp" placeholder="RHP PDF Link" value={formData.rhp} onChange={handleChange} className="input" />
        <input name="drhp" placeholder="DRHP PDF Link" value={formData.drhp} onChange={handleChange} className="input" />
      </div>

      <div className="flex justify-end gap-2">
        <button type="button" onClick={onCancel} className="bg-gray-200 px-4 py-2 rounded">Cancel</button>
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Register</button>
      </div>
    </form>
  );
};

export default IPOForm;
