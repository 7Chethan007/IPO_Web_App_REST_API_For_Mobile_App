import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import IPOCard from "../../components/IPOCard";
import FAQAccordion from "../../components/FAQAccordion";
import IPOListing from '../../components/IPOListing';

const ipoData = [
  {
    name: "EMS",
    date: "Aug 4, 2025",
    price: "₹100-₹120",
    status: "Open",
  },
  {
    name: "Yatra Online",
    date: "Aug 10, 2025",
    price: "₹150-₹180",
    status: "Upcoming",
  },
  // Add more IPOs based on screenshot...
];

export default function UpcomingIPO() {
  return (
    <div className="bg-gray-50 text-gray-900">
      <Navbar />
      
      {/* <div className="max-w-7xl mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-6">Upcoming IPOs</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {ipoData.map((ipo, index) => (
            <IPOCard key={index} data={ipo} />
          ))}
        </div>
      </div> */}

      <div>
        <IPOListing />
      </div>

      <div className="max-w-4xl mx-auto px-4 py-10">
        <FAQAccordion />
      </div>

      <Footer />
    </div>
  );
}
