import "./IPOCard.css";

export default function IPOCard({ data }) {
  // Add fallback data to prevent errors
  const safeData = {
    name: data?.name || 'Company Name',
    logo: data?.logo || null,
    priceBand: data?.priceBand || 'Not Available',
    openDate: data?.openDate || 'Not Available',
    closeDate: data?.closeDate || 'Not Available',
    issueSize: data?.issueSize || 'Not Available',
    issueType: data?.issueType || 'Book Built',
    listingDate: data?.listingDate || 'Not Available',
    status: data?.status || 'Not Issued',
    rhpStatus: data?.rhpStatus || null
  };

  const getStatusColor = (status) => {
    switch (status?.toLowerCase()) {
      case 'open':
        return 'status-open';
      case 'close':
      case 'closed':
        return 'status-closed';
      case 'not issued':
        return 'status-not-issued';
      default:
        return 'status-default';
    }
  };

  const getIssueTypeColor = (type) => {
    switch (type?.toLowerCase()) {
      case 'book built':
        return 'type-book-built';
      case 'fixed price':
        return 'type-fixed-price';
      default:
        return 'type-default';
    }
  };

  const getCompanyInitials = (name) => {
    if (!name) return 'C';
    const words = name.split(' ');
    if (words.length === 1) return words[0].charAt(0).toUpperCase();
    return words.slice(0, 2).map(word => word.charAt(0).toUpperCase()).join('');
  };

  return (
    <div className="ipo-card">
      {/* Company Header */}
      <div className="ipo-card-header">
        <div className="company-logo">
          {safeData.logo ? (
            <img src={safeData.logo} alt={`${safeData.name} logo`} className="logo-img" />
          ) : (
            <div className="logo-placeholder">
              {getCompanyInitials(safeData.name)}
            </div>
          )}
        </div>
        <div className="company-info">
          <h3 className="company-name">{safeData.name}</h3>
        </div>
      </div>

      {/* IPO Details Grid */}
      <div className="ipo-details">
        {/* Price Band Row */}
        <div className="detail-row">
          <div className="detail-group">
            <label className="detail-label">PRICE BAND</label>
            <div className="detail-value price-value">{safeData.priceBand}</div>
          </div>
          <div className="detail-group">
            <label className="detail-label">OPEN</label>
            <div className="detail-value">{safeData.openDate}</div>
          </div>
          <div className="detail-group">
            <label className="detail-label">CLOSE</label>
            <div className="detail-value">{safeData.closeDate}</div>
          </div>
        </div>

        {/* Issue Details Row */}
        <div className="detail-row">
          <div className="detail-group">
            <label className="detail-label">ISSUE SIZE</label>
            <div className="detail-value">{safeData.issueSize}</div>
          </div>
          <div className="detail-group">
            <label className="detail-label">ISSUE TYPE</label>
            <div className={`detail-value tag ${getIssueTypeColor(safeData.issueType)}`}>
              {safeData.issueType}
            </div>
          </div>
          <div className="detail-group">
            <label className="detail-label">LISTING DATE</label>
            <div className="detail-value">{safeData.listingDate}</div>
          </div>
        </div>
      </div>

      {/* Status Tags */}
      <div className="status-section">
        <div className={`status-tag ${getStatusColor(safeData.status)}`}>
          {safeData.status}
        </div>
        
        {/* RHP/DRHP Tags */}
        {safeData.rhpStatus && (
          <div className="document-tags">
            {safeData.rhpStatus.includes('RHP') && (
              <span className="doc-tag rhp-tag">RHP</span>
            )}
            {safeData.rhpStatus.includes('DRHP') && (
              <span className="doc-tag drhp-tag">DRHP</span>
            )}
          </div>
        )}
      </div>

      {/* Action Button */}
      <div className="card-actions">
        <button className="view-details-btn">
          View Details
        </button>
      </div>
    </div>
  );
}