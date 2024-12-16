// import React from 'react'
import useStore from '../store/store'
import { Box } from "@mui/material";
// import { Navigate, useSearchParams } from "react-router-dom";
// import { Navigate,  } from "react-router-dom";

import LoginForm from '../components/AuthForm/LoginForm';


const LoginPage = () => {

    const { profileID  } = useStore((state) => state)
    // const [searchParams, setSearchParams] = useSearchParams();

    // const { login, error, isLoading } = useLogin();

    // const handleLogin = async () => {
    //     login(formData);
    //   };
   
      return !profileID ? (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        m: "auto",
        flex: 1,
      }}
    >
      <LoginForm />
    </Box>
  ) : (
    // <Navigate
    //   to={searchParams.get("next") !== null ? searchParams.get("next")! : "/"}
    // />
    // <Navigate to={<LoginPage />}
    <h1>hello</h1>
  );
}

export default LoginPage