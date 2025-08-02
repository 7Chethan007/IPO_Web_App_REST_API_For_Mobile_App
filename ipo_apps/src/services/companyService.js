import apiClient from './apiClient';

// Company Service - handles all company-related API calls
class CompanyService {
  
  // Get all companies
  async getAllCompanies() {
    try {
      const data = await apiClient.get('/companies/');
      return data;
    } catch (error) {
      console.error('Error fetching all companies:', error);
      throw error;
    }
  }

  // Get companies by sector
  async getCompaniesBySector(sector) {
    try {
      const data = await apiClient.get(`/companies/?sector=${sector}`);
      return data;
    } catch (error) {
      console.error(`Error fetching companies in ${sector} sector:`, error);
      throw error;
    }
  }

  // Get single company by ID
  async getCompanyById(id) {
    try {
      const data = await apiClient.get(`/companies/${id}/`);
      return data;
    } catch (error) {
      console.error(`Error fetching company ${id}:`, error);
      throw error;
    }
  }

  // Search companies
  async searchCompanies(query) {
    try {
      const data = await apiClient.get(`/companies/?search=${query}`);
      return data;
    } catch (error) {
      console.error(`Error searching companies with query "${query}":`, error);
      throw error;
    }
  }

  // Get available sectors
  async getSectors() {
    try {
      const companies = await this.getAllCompanies();
      const sectors = [...new Set(companies.map(company => company.sector).filter(Boolean))];
      return sectors;
    } catch (error) {
      console.error('Error fetching sectors:', error);
      throw error;
    }
  }

  // Create new company
  async createCompany(companyData) {
    try {
      const data = await apiClient.post('/companies/', companyData);
      return data;
    } catch (error) {
      console.error('Error creating company:', error);
      throw error;
    }
  }

  // Update existing company
  async updateCompany(companyId, companyData) {
    try {
      const data = await apiClient.put(`/companies/${companyId}/`, companyData);
      return data;
    } catch (error) {
      console.error(`Error updating company ${companyId}:`, error);
      throw error;
    }
  }

  // Delete company (admin only)
  async deleteCompany(companyId) {
    try {
      await apiClient.delete(`/companies/${companyId}/`);
      return { success: true };
    } catch (error) {
      console.error(`Error deleting company ${companyId}:`, error);
      throw error;
    }
  }

}

const companyService = new CompanyService();
export default companyService;
