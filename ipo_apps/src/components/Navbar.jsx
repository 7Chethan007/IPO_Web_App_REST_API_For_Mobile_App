import { Link } from "react-router-dom";
import { useState } from "react";
import logo from "../assets/logo/logo.png";
import "./Navbar.css";

export default function Navbar() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <header className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <Link to="/" className="navbar-logo">
          <img src={logo} alt="Bluestock Logo" className="navbar-logo-img" />
          <span className="navbar-logo-text">BLUESTOCK</span>
        </Link>

        {/* Single Navigation - CSS handles desktop/mobile display */}
        <nav className={`navbar-nav ${isMobileMenuOpen ? 'navbar-nav-open' : ''}`}>
          <Link to="/ipo" className="navbar-link" onClick={() => setIsMobileMenuOpen(false)}>
            IPO
          </Link>
          <Link to="/community" className="navbar-link" onClick={() => setIsMobileMenuOpen(false)}>
            COMMUNITY
          </Link>
          
          <div className="navbar-dropdown">
            <button className="navbar-dropdown-btn">
              <span>PRODUCTS</span>
              <svg className="navbar-dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>

          <div className="navbar-dropdown">
            <button className="navbar-dropdown-btn">
              <span>BROKERS</span>
              <svg className="navbar-dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>

          <div className="navbar-news">
            <Link to="/live-news" className="navbar-link" onClick={() => setIsMobileMenuOpen(false)}>
              LIVE NEWS
            </Link>
            <span className="navbar-badge">NEW</span>
          </div>

          {/* Auth section inside nav for mobile */}
          <div className="navbar-auth">
            <Link to="/admin/signin" className="navbar-signin" onClick={() => setIsMobileMenuOpen(false)}>
              Sign In
            </Link>
            <Link to="/admin/signup" className="navbar-signup" onClick={() => setIsMobileMenuOpen(false)}>
              Sign Up Now
            </Link>
          </div>
        </nav>

        {/* Grid button - separate from nav */}
        <button className="navbar-grid-btn">
          <svg className="navbar-grid-icon" fill="currentColor" viewBox="0 0 20 20">
            <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
          </svg>
        </button>

        {/* Mobile menu toggle */}
        <button
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          className="navbar-mobile-toggle"
        >
          <svg className="navbar-mobile-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {isMobileMenuOpen ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>
    </header>
  );
}