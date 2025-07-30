import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import logoWithName from '../../../assets/logo/logo_with_name.jpg';

const ForgotPasswordPage = () => {
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Password reset link sent to:', email);
    // You can add your API call here
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-white px-4">
      <div className="max-w-md w-full space-y-8 text-center">
        <img src={logoWithName} alt="Logo" className="mx-auto h-10 w-auto" />

        <h2 className="mt-6 text-2xl font-bold text-gray-900">Forgot Password?</h2>
        <p className="mt-2 text-sm text-gray-500">
          Enter your email address to get the password reset link.
        </p>

        <form onSubmit={handleSubmit} className="mt-8 space-y-6">
          <div>
            <input
              type="email"
              placeholder="hello@bluestock.in"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-violet-600"
            />
          </div>

          <button
            type="submit"
            className="w-full py-3 bg-violet-600 text-white rounded-md hover:bg-violet-700 font-semibold"
          >
            Password Reset
          </button>
        </form>

        <div className="mt-4">
          <Link to="/login" className="text-sm text-gray-600 hover:text-violet-600">
            Back to login
          </Link>
        </div>
      </div>
    </div>
  );
};

export default ForgotPasswordPage;
