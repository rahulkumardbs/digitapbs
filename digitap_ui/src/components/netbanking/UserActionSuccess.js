import React from "react";
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import { MdMailOutline } from "react-icons/md";
import {centerContent, successButton, successCard, successCardTitle, successIcon} from '../../AppStyle';

const SuccessComponent = () => {
    const successText="Your application has been created successfully and has been submitted for approval";
    const handleRetry = () => {
        window.location.href = "/";
    }
    return (
        <div style={centerContent}>
            <Card style={successCard}>
                <Card.Body>
                    <Card.Title style={successCardTitle}><MdMailOutline style={successIcon}></MdMailOutline></Card.Title>
                    <Card.Text>
                        {successText}
                    </Card.Text>
                    <ButtonToolbar>
                        <Button variant="outline-secondary" size='md' style={successButton} onClick={handleRetry}>OK</Button>
                    </ButtonToolbar>
                </Card.Body>
            </Card>
        </div>
    );
};

export default SuccessComponent;