import { useState } from "react";
import "./FAQAccordion.css";

const faqs = [
  {
    question: "How to Subscribe to an IPO?",
    answer: (
      <div>
        <p><strong>Step 1:</strong> Login to your respective service provider.</p>
        <p><strong>Step 2:</strong> Click on the IPO button.</p>
        <p><strong>Step 3:</strong> Select the IPO you want to bid and enter the relevant details.</p>
        <p><strong>Step 4:</strong> Your subscription will be completed once you make the payment or give permission.</p>
      </div>
    ),
  },
  {
    question: "Should I buy an IPO first day?",
    answer:
      "Buying an IPO on the first day (listing day) depends on several factors including market sentiment, listing price compared to IPO price, company fundamentals, and market conditions. It's advisable to analyze the company's prospects and wait for price stabilization before making investment decisions.",
  },
  {
    question: "How do you know if an IPO is good?",
    answer:
      "To evaluate if an IPO is good, consider factors like company's financial health, promoter background, business model sustainability, competitive positioning, valuation metrics, market opportunity, use of funds from IPO proceeds, and expert recommendations. Always read the prospectus carefully.",
  },
  {
    question: "How to check IPO start date?",
    answer:
      "You can check IPO start dates through various sources: SEBI website, stock exchange websites (BSE/NSE), financial news portals, broker platforms, IPO tracking apps like Bluestock, and official company announcements. The dates are also mentioned in the prospectus.",
  },
  {
    question: "What is issue size?",
    answer:
      "Issue size refers to the total amount of money a company aims to raise through its IPO. It's calculated by multiplying the number of shares offered with the price band. For example, if a company offers 1 crore shares at ₹100 each, the issue size would be ₹100 crores.",
  },
  {
    question: "How many shares in a lot?",
    answer:
      "The number of shares in a lot varies for each IPO and is decided by the company. Typically, lot sizes range from 10 to 200 shares, depending on the IPO price. The lot size is designed to make the minimum investment amount reasonable for retail investors, usually between ₹10,000 to ₹15,000.",
  },
  {
    question: "How is the lot size calculated?",
    answer:
      "Lot size is calculated to ensure the minimum investment amount falls within a reasonable range for retail investors. It's determined by dividing the desired minimum investment amount by the IPO price. SEBI guidelines suggest keeping minimum application amount between ₹10,000 to ₹15,000.",
  },
  {
    question: "Who decides the IPO price band?",
    answer:
      "The IPO price band is decided by the company in consultation with merchant bankers (book running lead managers). They consider factors like company valuation, peer comparison, market conditions, demand expectations, and financial metrics to arrive at an appropriate price range.",
  },
  {
    question: "What is IPO GMP?",
    answer:
      "IPO GMP (Grey Market Premium) is the premium at which IPO shares are traded in the unofficial grey market before listing. It indicates market sentiment and expected listing price. However, GMP is not regulated and should not be the sole factor for investment decisions as it can be manipulated.",
  },
  {
    question: "How many lots should I apply for IPO?",
    answer:
      "For retail investors, you can apply for a maximum of ₹2 lakhs worth of shares. It's often recommended to apply for multiple lots (if budget allows) to increase allotment chances, but ensure you have sufficient funds. Consider your risk appetite and portfolio allocation before deciding the number of lots.",
  },
];

export default function FAQAccordion() {
  const [openIndex, setOpenIndex] = useState(0); // First item open by default

  const toggleAccordion = (index) => {
    setOpenIndex(index === openIndex ? null : index);
  };

  return (
    <div className="faq-section">
      <div className="faq-header">
        <h2 className="faq-title">Frequently Asked Questions?</h2>
        <p className="faq-subtitle">Find answers to common questions that come in your mind related to IPO.</p>
      </div>

      <div className="faq-accordion">
        {faqs.map((faq, index) => (
          <div key={index} className={`faq-item ${openIndex === index ? 'faq-item-open' : ''}`}>
            <div 
              className="faq-question"
              onClick={() => toggleAccordion(index)}
            >
              <h3 className="faq-question-text">{faq.question}</h3>
              <div className="faq-icon">
                {openIndex === index ? (
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M18 12H6"/>
                  </svg>
                ) : (
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M12 6v12M6 12h12"/>
                  </svg>
                )}
              </div>
            </div>
            
            <div className={`faq-answer ${openIndex === index ? 'faq-answer-open' : ''}`}>
              <div className="faq-answer-content">
                {typeof faq.answer === 'string' ? (
                  <p>{faq.answer}</p>
                ) : (
                  faq.answer
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}