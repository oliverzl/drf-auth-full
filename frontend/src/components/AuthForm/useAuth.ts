import { useState } from "react";
import { useNavigate } from "react-router-dom";

import useStore from "../../store/store";
import { loginAccount } from "../../api/auth-api";
// import useSnack from "hooks/useSnack";

// import { translation } from "constants/translation";
// import { CURLANG, WELCOME_BACK_PAGE } from "constants/url";
// import {
//   AuthAccountData,
//   LoginAccountResponse,
//   ErrorMessageV2,
// } from "types/auth";

export const useLogin = () => {
  const { setProfileID } = useStore((state) => state);

  //   const openSnack = useSnack();
  const navigate = useNavigate();

  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<
    { status: number; message: string } | undefined
  >();

  const handleLogin = async (authData: any) => {
    setIsLoading(true);
    const response: any = await loginAccount(authData);
    console.log(response);
    if ("error" in response) {
      setError({
        status: response.error.status,
        message: "please check email and password",
      });
    } else {
      localStorage.setItem("access", response.access);
      localStorage.setItem("refresh", response.refresh);
      localStorage.setItem("profile_id", response.id.toString());
      console.log(response);
      setProfileID(response.id.toString());

      //   if (response.schoolID) {
      //     localStorage.setItem("school_id", response.schoolID.toString());
      //     setSchoolID(response.schoolID.toString());
      //   }

      //   openSnack("Login successful", true);
      //   setRefreshGroup(true);
      //   navigate(`${CURLANG(currLanguage)}/${WELCOME_BACK_PAGE}`);
      navigate("/");
    }
    setIsLoading(false);
  };

  return { isLoading, login: handleLogin, error };
};
