import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import captcha from '../../static/images/captcha.png';
import {centerContent, errorButton, primaryButton, primaryCard, primaryCardTitle, captchaImageStyle} from '../../AppStyle';
import { UserAction } from "../utils/appUtil";
import { captchaBaseUrl } from "../../Config";

const CaptchaComponent = () => {
    var captchaUrl = sessionStorage.getItem("captcha_url");
    captchaUrl = captchaBaseUrl+captchaUrl ;
    console.log(captchaUrl);
    
    //var captchaUrl = 'https://static01.nyt.com/images/2018/02/26/crosswords/26wordplay-heck-captcha1/26wordplay-heck-captcha1-jumbo.png?quality=90&auto=webp';    
    const [userCaptcha, setUserCaptcha] = useState('');
    const captchaImage=captcha;
    const handleSubmit = () => {
        console.log(userCaptcha);
        
        UserAction('captcha', userCaptcha);
    }    
    const handleCancel = () => {
        window.location.href = "/";
    }
    const handleChange = (e) => {
        let value = e.target.value;
        setUserCaptcha(value);
    }
    return (
        <div style={centerContent}>
            <Card style={primaryCard}>
                <Card.Body style={{minWidth:'50%'}}>
                    <Card.Title style={primaryCardTitle}>Captcha Verification</Card.Title>
                    <Form>
                        <Card.Img variant="top" src={captchaUrl} style={captchaImageStyle} alt="Captcha not found" />
                        <Form.Group controlId="formBasicEmail">
                            <br></br>
                            <Form.Control type="text" placeholder="Type above captcha" value={userCaptcha} name='setCaptcha' onChange={handleChange} />
                        </Form.Group>
                    </Form>
                    <ButtonToolbar>
                        <Button variant="outline-secondary" style={primaryButton} onClick={handleSubmit}>Submit</Button>
                        <Button variant="outline-error" style={errorButton} onClick={handleCancel}>Cancel</Button>
                    </ButtonToolbar>
                </Card.Body>
            </Card>
        </div>
    );
};

export default CaptchaComponent;