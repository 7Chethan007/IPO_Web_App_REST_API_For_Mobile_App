import IPOCard from "./IPOCard";
import "./IPOListing.css";

// Complete data for all 9 companies from the image
const ipoData = [
  {
    id: 1,
    name: "Nova Agritech Ltd.",
    logo: null,
    priceBand: "Rs 39 - 41",
    openDate: "2024-01-22",
    closeDate: "2024-01-24",
    issueSize: "143.61 Cr.",
    issueType: "Book Built",
    listingDate: "2024-01-30",
    status: "Open"
  },
  {
    id: 2,
    name: "EPACK Durable Ltd.",
    logo: null,
    priceBand: "Rs 218 - 230",
    openDate: "2024-01-18",
    closeDate: "2024-01-23",
    issueSize: "640.05 Cr.",
    issueType: "Book Built",
    listingDate: "2024-01-29",
    status: "Open"
  },
  {
    id: 3,
    name: "RK Swamy Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "Not Issued",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 4,
    name: "Gravel Stays Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "9430 Cr.",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 5,
    name: "Imagine Marketing Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "2000 Cr.",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 6,
    name: "Kids Clinic India Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "Not Issued",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 7,
    name: "OLA Electric Mobility Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "Not Issued",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 8,
    name: "One Mobikwik Systems Ltd.",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "1900 Cr.",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  },
  {
    id: 9,
    name: "Le Travenues Technology",
    logo: null,
    priceBand: "Not Issued",
    openDate: "Not Issued",
    closeDate: "Not Issued",
    issueSize: "1600 Cr.",
    issueType: "Book Built",
    listingDate: "Not Issued",
    status: "Not Issued"
  }
];

export default function IPOListing() {
  console.log("IPOListing rendered with", ipoData.length, "companies"); // Debug log

  return (
    <div className="ipo-listing-section">
      <div className="ipo-listing-header">
        <h2 className="section-title">Upcoming IPO Updates</h2>
        <p className="section-subtitle">
          Stay updated with the latest Initial Public Offerings in the market
        </p>
      </div>

      <div className="ipo-grid">
        {ipoData.map((ipo) => {
          console.log("Rendering IPO:", ipo.name); // Debug log
          return <IPOCard key={ipo.id} data={ipo} />;
        })}
      </div>

      <div className="load-more-section">
        <button className="load-more-btn">
          Load More IPOs
        </button>
      </div>
    </div>
  );
}