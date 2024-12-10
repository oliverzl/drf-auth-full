import React from 'react'



const LoginPage = () => {
    return (
        <div style={{
            display: "flex",
            width: '100%',
            height: '100vh',
            alignItems: 'center',
            justifyContent: " center",

        }}>
            <form >

                <input type="text" name='username' placeholder="Enter Username" style={{ height: "5vh" }} />
                <input type="password" name='password' placeholder="Enter Password" style={{ height: "5vh" }} />
                <input type="submit" style={{ height: "5vh" }} />

            </form>

        </div>
    )
}

export default LoginPage