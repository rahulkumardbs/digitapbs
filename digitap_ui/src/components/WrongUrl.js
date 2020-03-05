import React, { useState } from "react";
import { Card } from "react-bootstrap";
import {centerContent, primaryCard, notFoundCard} from '../AppStyle';

const PageNotFound = () => {
    return (
        <div style={centerContent}>
            <Card style={primaryCard}>
                <Card.Body style={{minWidth:'100%'}}>
                    <Card.Title style={notFoundCard}>404</Card.Title>
                </Card.Body>
            </Card>
        </div>
    );
};

export default PageNotFound;