import { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
import { Stack, TextField, Typography, Button } from "@mui/material";

import useStore from "../../store/store"

// import Button from "components/Button/Button";
// import { AuthAccountData } from "types/auth";
// import { translation } from "constants/translation";

// import { CURLANG, FORGOTTEN_PASSWORD } from "constants/url";

import { useLogin } from "./useAuth";

// uncomment!!!!!!!!!
// import AuthError from "./AuthError";

const LoginRegisterForm = () => {
    const { setProfileID } = useStore((state) => state);
    const [formData, setFormData] = useState<any>({
        email: "",
        password: "",
    });

    useEffect(() => {
        // To get profile data after re-login (refresh token expired)
        setProfileID("");
        // eslint-disable-next-line react-hooks/exhaustive-deps
      }, []);




    // const navigate = useNavigate();
    const { login, error, isLoading} = useLogin();

    const handleLogin = async () => {
        console.log(formData)
        login(formData);
    };

    return (
        <Stack
            component="form"
            sx={{
                display: "flex",
                flexDirection: "column",
                maxWidth: 800,
                minWidth: { xs: 300, sm: 400, md: 500 },
                flex: 1,
                justifyContent: "center",
                alignItems: "center",
                mt: "-30px",
            }}
            spacing={3}
            noValidate
            autoComplete="off"
        >
            <Typography
                sx={{
                    fontSize: "2rem",
                    fontWeight: "500",
                    textAlign: "center",
                }}
            >
                Login to the Little Lab
            </Typography>
            <TextField
                required
                label={"username"}
                value={formData.email}
                onChange={(event) => {
                    setFormData((prev: any) => ({ ...prev, email: event.target.value }));
                }}
                fullWidth
            />
            <TextField
                required
                label={"password"}
                type="password"
                value={formData.password}
                onChange={(event) => {
                    setFormData((prev: any) => ({ ...prev, password: event.target.value }));
                }}
                fullWidth
            />
            <Button onClick={handleLogin}>Login</Button>
            {/* UNCOMMENT!!!!!!!! */}
            {/* <AuthError error={error} /> */}
            {/* <Button onClick={handleLogin}>Login</Button> */}
            {/* <Typography
                sx={{
                    color: "txt.secondary",
                    cursor: "pointer",
                }}
                onClick={() => {
                    navigate(`${CURLANG(currLanguage)}/${FORGOTTEN_PASSWORD}`);
                }}
            >
                {translation.forgottenPassword}
            </Typography> */}
        </Stack>
    );
};

export default LoginRegisterForm;
