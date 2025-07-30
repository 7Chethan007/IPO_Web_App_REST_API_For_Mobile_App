import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UpcomingIPOs from "./pages/User/UpcomingIPOs";
import AdminDashboard from "./pages/Admin/AdminDashboard";
import IPOListing from './components/IPOListing';
import SigninPage from "./pages/Admin/Auth/SigninPage";
import SignupPage from './pages/Admin/Auth/SignupPage';
import ForgotPasswordPage from "./pages/Admin/Auth/ForgotPasswordPage"

import DashboardOverview from './pages/Admin/DashboardOverview';
import ManageIPO from './pages/Admin/ManageIPO';
import RegisterIPO from './pages/Admin/RegisterIPO';
import './utils/chartConfig'; 


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UpcomingIPOs />} />
        <Route path="/upcoming-ipo" element={<UpcomingIPOs />} />
        <Route path="/ipo-listing" element={<IPOListing />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/admin/signup" element={<SignupPage />} />
        <Route path="/admin/signin" element={<SigninPage />} />
        <Route path="/admin/forgot-password" element={<ForgotPasswordPage />} />

        <Route path="/admin/dashboard" element={<DashboardOverview />} />
        <Route path="/admin/manage-ipo" element={<ManageIPO />} />
        <Route path="/admin/register-ipo" element={<RegisterIPO />} />
      </Routes>
    </Router>
  );
}

export default App;