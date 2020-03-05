import React, { Component } from "react";
import AppTopBar from "./components/AppTopBar";
import FooterMenu from "./components/FooterMenu";
import Home from "./components/Home";
import OtpComponent from './components/UserActionOtp';
import CaptchaComponent from './components/UserActionCaptcha';
import ErrorComponent from './components/UserActionError';
import SuccessComponent from './components/UserActionSuccess';
import QuestionComponent from './components/UserActionQuestion';
import ProcessComponent from './components/UserActionProcess';
import {contentStyles, appBody} from './AppStyle';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { CheckAuthentication} from './components/utils/appUtil';
import PageNotFound from "./components/WrongUrl";


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