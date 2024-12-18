import axios from "axios";
import { logoutAccount } from "../api/auth-api"

const apiUrl = import.meta.env.VITE_API_URL;

const instance = axios.create({
  baseURL: apiUrl,
  headers: {
    "Content-Type": "application/json",
  },
});

instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access");
    if (token && config && config.headers) {
      config.headers["Authorization"] = "Bearer " + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

instance.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;

    if (err.response.status === 401) {
      // Attempt to refresh the token
      try {
        const refreshToken = localStorage.getItem("refresh");
        if (refreshToken) {
            console.log("refresh", `${apiUrl}/api/jwt/refresh/`)
          const response = await axios.post(
            `${apiUrl}/api/jwt/refresh/`,
            {
              refresh: refreshToken,
            }
          );

          const newAccessToken = response.data.access;
          localStorage.setItem("access", newAccessToken);

          // Retry the original request with the new token
          originalConfig.headers["Authorization"] = "Bearer " + newAccessToken;
          return axios(originalConfig);
        } else {
          // No refresh token available, log out and refresh the page
          logoutAccount();
          window.location.reload();
        }
      } catch (refreshError) {
        // Refresh token is invalid or expired, log out and refresh the page
        logoutAccount();
        window.location.reload();
      }
    } else if (
      originalConfig.url === "/api/jwt/refresh/" &&
      err.response.status === 404
    ) {
      logoutAccount();
      window.location.reload();
    }

    return Promise.reject(err);
  }
);

export const noAuthInstance = axios.create({
  baseURL: apiUrl
});

export default instance;
