import React from "react";
import logo from '../../static/images/logo1.svg';
import {Navbar} from 'react-bootstrap';
import {topBarStyle} from '../../AppStyle';

const AppTopBar = () => {
  return (
    <div style={topBarStyle}>
      <Navbar>
        <Navbar.Brand href="#">
            <img
                src={logo}
                width="150"
                height="150"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
            />
        </Navbar.Brand>
      </Navbar>
    </div>
  );
};

export default AppTopBar;