import React from 'react'
import { Link } from "react-router-dom"
const Header = () => {
    return (
        <div>

            <Link to='/' style={{ fontSize: '50px' }}>
                Home</Link>
            <span>||</span>
            <Link to='/login' style={{ fontSize: '50px' }}>
                Login</Link>
        </div>
    )
}

export default Header