import React from 'react';
import SignupForm from '../../../components/Auth/SignupForm';

const Signup = () => {
  const handleSignup = (formData) => {
    console.log("Signup Data:", formData);
    // You can call API here if backend is connected
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <SignupForm onSignup={handleSignup} />
    </div>
  );
};

export default Signup;
