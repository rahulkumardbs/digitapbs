import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import {centerContent, primaryButton, errorButton, primaryCard, primaryCardTitle} from '../../AppStyle';
import { UserAction } from "../utils/appUtil";

const ErrorComponent = () => {
    const [userOtp, setUserOtp] = useState('');
    const handleSubmit = () => {
        UserAction('otp', userOtp);
    }
    const handleCancel = () => {
        window.location.href = "/";
    }
    const handleChange = (e) => {
        let value = e.target.value;
        setUserOtp(value);
    }
    return (
        <div style={centerContent}>
            <Card style={primaryCard}>
                <Card.Body>
                    <Card.Title style={primaryCardTitle}>User Action Required</Card.Title>
                    <Form>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Label>Please enter OTP received in your mobile/e-mail from HDFC Bank</Form.Label>
                            <Form.Control type="text" placeholder="Enter OTP" value={userOtp} name='setOtp' onChange={handleChange} />

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

export default ErrorComponent;