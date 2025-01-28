import { useState, useEffect } from 'react';
import { axiosReq } from '../services/api';

// For fetching data from API
export const useApi = (url: string) => {
  // Data state to store fetched data
  const [data, setData] = useState<any>(null);
  // loading state to indicate loading status
  const [loading, setLoading] = useState(true);
  // Error state to store any error that occurs
  const [error, setError] = useState<unknown>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axiosReq.get(url);
        setData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
};
