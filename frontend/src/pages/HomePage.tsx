// import React from 'react'

import { useNavigate } from "react-router-dom";
import { logoutAccount } from "../api/auth-api";
import useStore from "../store/store"
// import useStore from '../store/store'
const HomePage = () => {
    const navigate = useNavigate();

    const {
        profileID,
        setProfileID,
    } = useStore((state) => state);


    const handleLogout = () => {
        logoutAccount();
        setProfileID("");
        navigate('/login')
    };

    // const { count, increment, incrementAsync, decrement } = useStore((state) => state)
    return (
        <div>
            <h2 onClick={() => {
                console.log(profileID)
            }}>You are logged in to the HomePage!</h2>
            {/* <h1>Count: {count}</h1> */}
            {/* <button onClick={incrementAsync}>Increment</button> */}
            {/* <button onClick={decrement}>Decrement</button> */}
            <button onClick={() => {
                handleLogout()
            }}>logout</button>
        </div>
    )
}

export default HomePage