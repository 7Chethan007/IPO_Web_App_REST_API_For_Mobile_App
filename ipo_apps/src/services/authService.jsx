import apiClient from './apiClient';

// Authentication Service - handles login, logout, and user management
class AuthService {
  
  // Login user
  async login(username, password) {
    try {
      const data = await apiClient.post('/auth/signin/', {
        username,
        password
      });
      
      if (data.access) {
        // Store tokens in localStorage
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        localStorage.setItem('user', JSON.stringify(data.user));
      }
      
      return data;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  }

  // Logout user
  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');
  }

  // Register new user
  async register(userData) {
    try {
      const data = await apiClient.post('/auth/register/', userData);
      return data;
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  }

  // Get current user
  getCurrentUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }

  // Check if user is authenticated
  isAuthenticated() {
    const token = localStorage.getItem('access_token');
    return !!token;
  }

  // Get access token
  getAccessToken() {
    return localStorage.getItem('access_token');
  }

  // Refresh access token
  async refreshToken() {
    try {
      const refresh = localStorage.getItem('refresh_token');
      if (!refresh) {
        throw new Error('No refresh token available');
      }

      const data = await apiClient.post('/auth/token/refresh/', {
        refresh: refresh
      });

      localStorage.setItem('access_token', data.access);
      return data.access;
    } catch (error) {
      console.error('Token refresh error:', error);
      this.logout(); // Clear invalid tokens
      throw error;
    }
  }

}

const authService = new AuthService();
export default authService;