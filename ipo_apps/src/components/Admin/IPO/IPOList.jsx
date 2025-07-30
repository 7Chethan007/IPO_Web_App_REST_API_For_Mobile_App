// src/components/Admin/IPO/IPOList.jsx
import React from 'react';

const IPOList = ({ ipoList }) => {
  return (
    <table className="w-full border mt-4 text-left">
      <thead>
        <tr className="bg-gray-100">
          <th className="p-2">Company</th>
          <th className="p-2">Issue Size</th>
          <th className="p-2">Open</th>
          <th className="p-2">Close</th>
          <th className="p-2">Listing Price</th>
          <th className="p-2">CMP</th>
        </tr>
      </thead>
      <tbody>
        {ipoList.map((ipo, i) => (
          <tr key={i} className="border-t">
            <td className="p-2">{ipo.companyName}</td>
            <td className="p-2">{ipo.issueSize}</td>
            <td className="p-2">{ipo.openDate}</td>
            <td className="p-2">{ipo.closeDate}</td>
            <td className="p-2">{ipo.listingPrice}</td>
            <td className="p-2">{ipo.cmp}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default IPOList;
