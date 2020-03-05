import React, { Component } from "react";
import AppTopBar from "./components/header/AppTopBar";
import FooterMenu from "./components/footer/FooterMenu";
import Home from "./components/netbanking/Home";
import OtpComponent from './components/netbanking/UserActionOtp';
import CaptchaComponent from './components/netbanking/UserActionCaptcha';
import ErrorComponent from './components/netbanking/UserActionError';
import SuccessComponent from './components/netbanking/UserActionSuccess';
import QuestionComponent from './components/netbanking/UserActionQuestion';
import ProcessComponent from './components/netbanking/UserActionProcess';
import {contentStyles, appBody} from './AppStyle';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { CheckAuthentication} from './components/utils/appUtil';
import PageNotFound from "./components/netbanking/WrongUrl";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuthenticated: false
    }
  }

  componentDidMount = () => {

    
    // console.log(CheckAuthentication);
    
    // if(CheckAuthentication){
    //   console.log("Data");
    // }
    // else{
    //   console.log("Not Data");
    // }
  }

  render() {
    const menuItems = [
    ];
    const styles = contentStyles;
    return (
      <div style={appBody}>
        <AppTopBar />
        <Router>
          <div>
            <Route exact path="/" component={Home} />
            <Route path="/otp" component={OtpComponent} />
            <Route path="/captcha" component={CaptchaComponent} />
            <Route path="/error" component={ErrorComponent} />
            <Route path="/question" component={QuestionComponent} />
            <Route path="/success" component={SuccessComponent} />
            <Route path="/process" component={ProcessComponent} />
            <Route path="/wrongurl" component={PageNotFound} />
          </div>
        </Router>
        <FooterMenu menuItems={menuItems} styles={styles} />
      </div>
    );
  }
}

export default App;