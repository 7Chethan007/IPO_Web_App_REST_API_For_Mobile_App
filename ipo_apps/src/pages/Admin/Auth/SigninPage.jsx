import React from "react";
import SigninForm from "../../../components/Auth/SigninForm";
import logoWithName from '../../../assets/logo/logo_with_name.jpg';

const SigninPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full bg-white p-8 rounded-lg shadow-lg">
        <div className="text-center mb-6">
          <img src={logoWithName} alt="Bluestock Logo" className="w-24 mx-auto mb-2" />
        </div>
        <SigninForm />
      </div>
    </div>
  );
};

export default SigninPage;
