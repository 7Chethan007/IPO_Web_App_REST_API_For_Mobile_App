import apiClient from './apiClient';

// IPO Service - handles all IPO-related API calls
class IPOService {
  
  // Get all IPOs
  async getAllIPOs() {
    try {
      const data = await apiClient.get('/ipos/');
      return data;
    } catch (error) {
      console.error('Error fetching all IPOs:', error);
      throw error;
    }
  }

  // Get IPOs by status
  async getIPOsByStatus(status) {
    try {
      const data = await apiClient.get(`/ipos/?status=${status}`);
      return data;
    } catch (error) {
      console.error(`Error fetching ${status} IPOs:`, error);
      throw error;
    }
  }

  // Get upcoming IPOs
  async getUpcomingIPOs() {
    return this.getIPOsByStatus('UPCOMING');
  }

  // Get open IPOs
  async getOpenIPOs() {
    return this.getIPOsByStatus('OPEN');
  }

  // Get closed IPOs
  async getClosedIPOs() {
    return this.getIPOsByStatus('CLOSED');
  }

  // Get listed IPOs
  async getListedIPOs() {
    return this.getIPOsByStatus('LISTED');
  }

  // Get IPOs by board type
  async getIPOsByBoard(board) {
    try {
      const data = await apiClient.get(`/ipos/?board=${board}`);
      return data;
    } catch (error) {
      console.error(`Error fetching ${board} board IPOs:`, error);
      throw error;
    }
  }

  // Get Main Board IPOs
  async getMainBoardIPOs() {
    return this.getIPOsByBoard('MAIN');
  }

  // Get SME Board IPOs
  async getSMEBoardIPOs() {
    return this.getIPOsByBoard('SME');
  }

  // Get featured IPOs
  async getFeaturedIPOs() {
    try {
      const data = await apiClient.get('/ipos/?is_featured=true');
      return data;
    } catch (error) {
      console.error('Error fetching featured IPOs:', error);
      throw error;
    }
  }

  // Get recommended IPOs
  async getRecommendedIPOs() {
    try {
      const data = await apiClient.get('/ipos/?is_recommended=true');
      return data;
    } catch (error) {
      console.error('Error fetching recommended IPOs:', error);
      throw error;
    }
  }

  // Get single IPO by ID
  async getIPOById(id) {
    try {
      const data = await apiClient.get(`/ipos/${id}/`);
      return data;
    } catch (error) {
      console.error(`Error fetching IPO ${id}:`, error);
      throw error;
    }
  }

  // Get IPO documents
  async getIPODocuments(ipoId) {
    try {
      const data = await apiClient.get(`/ipos/${ipoId}/documents/`);
      return data;
    } catch (error) {
      console.error(`Error fetching documents for IPO ${ipoId}:`, error);
      throw error;
    }
  }

  // Get IPO news
  async getIPONews(ipoId) {
    try {
      const data = await apiClient.get(`/ipos/${ipoId}/news/`);
      return data;
    } catch (error) {
      console.error(`Error fetching news for IPO ${ipoId}:`, error);
      throw error;
    }
  }

  // Search IPOs
  async searchIPOs(query) {
    try {
      const data = await apiClient.get(`/ipos/?search=${query}`);
      return data;
    } catch (error) {
      console.error(`Error searching IPOs with query "${query}":`, error);
      throw error;
    }
  }

  // Create new IPO
  async createIPO(ipoData) {
    try {
      const data = await apiClient.post('/ipos/', ipoData);
      return data;
    } catch (error) {
      console.error('Error creating IPO:', error);
      throw error;
    }
  }

  // Update existing IPO
  async updateIPO(ipoId, ipoData) {
    try {
      const data = await apiClient.put(`/ipos/${ipoId}/`, ipoData);
      return data;
    } catch (error) {
      console.error(`Error updating IPO ${ipoId}:`, error);
      throw error;
    }
  }

  // Delete IPO (admin only)
  async deleteIPO(ipoId) {
    try {
      await apiClient.delete(`/ipos/${ipoId}/`);
      return { success: true };
    } catch (error) {
      console.error(`Error deleting IPO ${ipoId}:`, error);
      throw error;
    }
  }

}

const ipoService = new IPOService();
export default ipoService;
