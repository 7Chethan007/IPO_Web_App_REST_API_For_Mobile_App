import React from 'react';
export default function IPOTable({ items, onUpdate, onDelete, onView }) {
  return (
    <table className="min-w-full bg-white">
      <thead><tr className="bg-gray-100">
        {['Company','Price Band','Open','Close','ISSUE SIZE','Type','Listing','Status','Action','Delete'].map(h => <th key={h} className="p-2 text-left">{h}</th>)}
      </tr></thead>
      <tbody>
        {items.map((ipo,i) => (
          <tr key={i} className={i%2? 'bg-gray-50':'bg-white'}>
            <td className="p-2">{ipo.company}</td>
            <td className="p-2">{ipo.priceBand}</td>
            <td className="p-2">{ipo.openDate}</td>
            <td className="p-2">{ipo.closeDate}</td>
            <td className="p-2">{ipo.issueSize}</td>
            <td className="p-2">{ipo.issueType}</td>
            <td className="p-2">{ipo.listingDate}</td>
            <td className="p-2">
              <span className={`px-2 py-1 rounded-full text-sm bg-${ipo.statusColor}-100 text-${ipo.statusColor}-600`}>{ipo.status}</span>
            </td>
            <td className="p-2"><button onClick={()=>onUpdate(ipo)} className="bg-indigo-600 text-white px-3 py-1 rounded">Update</button></td>
            <td className="p-2 flex space-x-2">
              <button onClick={()=>onDelete(ipo)} className="text-red-600"><i className="fas fa-trash"></i></button>
              <button onClick={()=>onView(ipo)} className="text-gray-600"><i className="fas fa-eye"></i></button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}