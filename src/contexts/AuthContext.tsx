import { createContext, useContext, useState, ReactNode } from 'react';
import { axiosReq } from '@/services/api';

// AuthContext type defining the context structure
interface AuthContextType {
  isAuthenticated: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

// Provide authentication state and functions
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Wrap around components that need authentication
export const AuthProvider = ({ children }: { children: ReactNode }) => {
  // State to track authentication status
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const fetchUser = async () => {
    try {
      const response = await axiosReq.get('/dj-rest-auth/user/');
      if (response.status === 200) {
        setIsAuthenticated(true);
      }
    } catch (error) {
      console.error('Fetching user failed:', error);
      setIsAuthenticated(false);
    }
  };

  const login = async (username: string, password: string) => {
    try {
      const response = await axiosReq.post('/dj-rest-auth/login/', {
        username,
        password,
      });

      if (response.status !== 200) {
        throw new Error('Login failed');
      }

      await fetchUser();
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  const logout = async () => {
    try {
      const response = await axiosReq.post('/dj-rest-auth/logout/');

      if (response.status !== 200) {
        throw new Error('Logout failed');
      }

      setIsAuthenticated(false);
    } catch (error) {
      console.error('Logout failed:', error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Access authentication context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
