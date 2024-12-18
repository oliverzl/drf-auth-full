// import axios, { noAuthInstance as noAuthAxios } from "api/axiosConfig";
import axios from "axios";
import { AxiosError } from "axios";
const apiUrl = import.meta.env.VITE_API_URL;

export const loginAccount = async (accountData: any) => {
  try {
    const res = await axios.post(`${apiUrl}/authapi/login/`, accountData);
    const data: any = await res.data;
    return data;
  } catch (error: unknown) {
    if (error instanceof AxiosError && error.response) {
      const { status, statusText } = error.response;
      return {
        error: { status, statusText },
      };
    } else {
      console.log("error: ", error);
      return {
        error: { status: 500, statusText: "Internal Server Error" },
      };
    }
  }
};

export const logoutAccount = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  localStorage.removeItem("profile_id");
};
