import React from "react";
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import {centerContent, errorButton, primaryButton, errorCard, errorCardTitle} from '../AppStyle';

const ErrorComponent = () => {
    //const errorText="Validation failed- The credential you have entered is not valid, you can try again."
    const errorText = sessionStorage.getItem('error_msg');
    const handleRetry = () => {
        window.location.href = "/";
    }
    return (
        <div style={centerContent}>
            <Card style={errorCard}>

                <Card.Body style={{minWidth:'100%'}}>
                    <Card.Title style={errorCardTitle}>There Was an Error</Card.Title>
                    <Card.Text>
                        {errorText}
                    </Card.Text>
                    <ButtonToolbar>
                        <Button variant="outline-secondary" size='md' style={primaryButton} onClick={handleRetry}>Try Again</Button>
                        <Button variant="outline-error" size='md' style={errorButton}>Take Me Back</Button>
                    </ButtonToolbar>
                </Card.Body>
            </Card>
        </div>
    );
};

export default ErrorComponent;