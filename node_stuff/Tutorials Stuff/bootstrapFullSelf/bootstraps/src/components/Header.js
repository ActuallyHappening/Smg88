/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react'
import Summary from './Summary'

const Header = ({ icon }) => {
  return (
    <nav className="navbar sticky-top navbar-expand-lg navbar-dark bg-primary p-3">
      <img src={icon} width="30" height="30" alt="Smg88 Icon (Swift)" /* className="navbar-brand" */ href="#"/>
      <button className="btn btn-primary" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Features</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Pricing</a>
          </li>
          <li className="nav-item">
            <a className="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
      </div>
      <Summary />
    </nav>
  )
}

export default Header