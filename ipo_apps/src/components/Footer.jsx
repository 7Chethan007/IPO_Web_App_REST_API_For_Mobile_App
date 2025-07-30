import { Link } from "react-router-dom";
import logo from "../assets/logo/logo.png";
// Import social media icons
import twitterIcon from "../assets/icons/twitter.png";
import facebookIcon from "../assets/icons/facebook.png";
import youtubeIcon from "../assets/icons/youtube.png";
import instagramIcon from "../assets/icons/instagram.png";
import telegramIcon from "../assets/icons/telegram.png";
import linkedinIcon from "../assets/icons/linkedin.png";
import "./Footer.css";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        {/* Footer Links Grid */}
        <div className="footer-grid">
          {/* Resources Section */}
          <div className="footer-section">
            <h3 className="footer-title">Resources</h3>
            <ul className="footer-links">
              <li><Link to="/trading-view" className="footer-link">Trading View</Link></li>
              <li><Link to="/nse-holidays" className="footer-link">NSE Holidays</Link></li>
              <li><Link to="/e-voting-cdsl" className="footer-link">e-Voting CDSL</Link></li>
              <li><Link to="/e-voting-nsdl" className="footer-link">e-Voting NSDL</Link></li>
              <li><Link to="/market-timings" className="footer-link">Market Timings</Link></li>
            </ul>
          </div>

          {/* Company Section */}
          <div className="footer-section">
            <h3 className="footer-title">Company</h3>
            <ul className="footer-links">
              <li><Link to="/careers" className="footer-link">Careers</Link></li>
              <li><Link to="/contact" className="footer-link">Contact Us</Link></li>
              <li><Link to="/about" className="footer-link">About US</Link></li>
              <li><Link to="/community" className="footer-link">Community</Link></li>
              <li><Link to="/blogs" className="footer-link">Blogs</Link></li>
            </ul>
          </div>

          {/* Offerings Section */}
          <div className="footer-section">
            <h3 className="footer-title">Offerings</h3>
            <ul className="footer-links">
              <li><Link to="/compare-broker" className="footer-link">Compare Broker</Link></li>
              <li><Link to="/fin-calculators" className="footer-link">Fin Calculators</Link></li>
              <li><Link to="/ipo" className="footer-link">IPO</Link></li>
              <li><Link to="/all-brokers" className="footer-link">All Brokers</Link></li>
              <li><Link to="/products" className="footer-link">Products</Link></li>
            </ul>
          </div>

          {/* Links Section */}
          <div className="footer-section">
            <h3 className="footer-title">Links</h3>
            <ul className="footer-links">
              <li><Link to="/shark-investor" className="footer-link">Shark Investor</Link></li>
              <li><Link to="/mutual-funds" className="footer-link">Mutual Funds</Link></li>
              <li><Link to="/sitemap" className="footer-link">Sitemap</Link></li>
              <li><Link to="/indian-indices" className="footer-link">Indian Indices</Link></li>
              <li><Link to="/bug-bounty" className="footer-link">Bug Bounty Program</Link></li>
            </ul>
          </div>

          {/* Policy Section */}
          <div className="footer-section">
            <h3 className="footer-title">Policy</h3>
            <ul className="footer-links">
              <li><Link to="/terms" className="footer-link">Terms & Conditions</Link></li>
              <li><Link to="/privacy" className="footer-link">Privacy Policy</Link></li>
              <li><Link to="/refund" className="footer-link">Refund Policy</Link></li>
              <li><Link to="/disclaimer" className="footer-link">Disclaimer</Link></li>
              <li><Link to="/trust-security" className="footer-link">Trust & Security</Link></li>
            </ul>
          </div>
        </div>

        {/* Footer Bottom Section */}
        <div className="footer-bottom">
          {/* Left Side - Logo and Info */}
          <div className="footer-brand">
            {/* Social Media Icons */}
            <div className="footer-social">
              <a href="https://twitter.com/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={twitterIcon} alt="Twitter" className="footer-social-icon" />
              </a>
              <a href="https://facebook.com/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={facebookIcon} alt="Facebook" className="footer-social-icon" />
              </a>
              <a href="https://youtube.com/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={youtubeIcon} alt="YouTube" className="footer-social-icon" />
              </a>
              <a href="https://linkedin.com/company/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={linkedinIcon} alt="LinkedIn" className="footer-social-icon" />
              </a>
              <a href="https://instagram.com/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={instagramIcon} alt="Instagram" className="footer-social-icon" />
              </a>
              <a href="https://telegram.me/bluestock" className="footer-social-link" target="_blank" rel="noopener noreferrer">
                <img src={telegramIcon} alt="Telegram" className="footer-social-icon" />
              </a>
            </div>

            {/* Logo and Company Info */}
            <div className="footer-logo">
              <img src={logo} alt="Bluestock Logo" className="footer-logo-img" />
              <span className="footer-logo-text">BLUESTOCK</span>
            </div>

            <div className="footer-company-info">
              <p>Bluestock Fintech</p>
              <p>Pune, Maharashtra</p>
              <p className="footer-registration">
                MSME Registration No:<br />
                UDYAM-MH-01-v0138001
              </p>
            </div>

            {/* Startup India Logo */}
            <div className="footer-startup-india">
              <span className="startup-text">#startup</span>
              <span className="india-text">india</span>
            </div>

            <p className="footer-copyright">
              Bluestock Fintech All Rights Reserved.
            </p>
          </div>

          {/* Right Side - Disclaimers */}
          <div className="footer-disclaimers">
            <p>
              Investment in securities markets are subject to market risks, read all the related documents 
              carefully before investing as prescribed by SEBI. Issued in the interest of the investors.
            </p>
            
            <p>
              The users can write to <a href="mailto:hello@bluestock.in" className="footer-email">hello@bluestock.in</a> for 
              any app, website related queries. Also you can send IT / Tech related feedback to{' '}
              <a href="mailto:cto@bluestock.in" className="footer-email">cto@bluestock.in</a>
            </p>
            
            <p>
              Disclaimer: We are not a SEBI registered research analyst company. We do not provide any kind of 
              stock recommendations, buy/sell stock tips, or investment and trading advice. All the stock scripts 
              shown in the Bluestock app, website, all social media handles are for educational purposes only.
            </p>
            
            <p>
              Before making any investment in the financial market, it is advisable to consult with your financial 
              advisor. Remember that stock markets are subject to market risks.
            </p>

            <p className="footer-made-with">
              Made with ❤️ in Pune, Maharashtra
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}