import React, {  useState } from "react";

import { Navigate, Outlet, useLocation } from "react-router-dom";

// import useSnack from "hooks/useSnack";
// import useStore from "../../store/store"

// import { CURLANG, LOGIN } from "constants/url";

const ProtectedRoute = ({

    children,
}: {
    isAuth?: boolean;
    children?: React.ReactElement;
}) => {
    //   const openSnack = useSnack();
    //   const { currLanguage } = useStore((state:any) => state);
    const [accessToken] = useState(localStorage.getItem("access"));
    const [profileId] = useState(localStorage.getItem("profile_id"));
    const currentLocation = useLocation();

    if (!accessToken || !profileId) {
        // openSnack("You need to be logged in to see this page!", false);
        console.log("You need to be logged in to see this page!", `login?next=${currentLocation.pathname
                    }`)
        return (
            <Navigate
                to={`login?next=${currentLocation.pathname
                    }`}
                replace
            />
        );
    }

    return children ? children : <Outlet />;
};

export default ProtectedRoute;
