// import React from 'react'
import useStore from '../store/store'
import { Box, Button } from "@mui/material";
// import { Navigate, useSearchParams } from "react-router-dom";
import { Navigate  } from "react-router-dom";

import LoginForm from '../components/AuthForm/LoginForm';


const LoginPage = () => {

  const profileID = useStore((state) => state.profileID)
  console.log("ProfileID in Component:", profileID);
  if (profileID) {
    return <Navigate to="/" replace />;
  }

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        m: "auto",
        flex: 1,
      }}
    >
      <Button onClick={() => { console.log(profileID); }}>hello</Button>
      <LoginForm />
    </Box>
  );
 
}

export default LoginPage