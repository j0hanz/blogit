import React from 'react';
import { Card as CustomCard } from 'react-bootstrap';

interface CardProps {
  title: string;
  text: string;
}

const Card: React.FC<CardProps> = ({ title, text }) => {
  return (
    <CustomCard>
      <CustomCard.Body>
        <CustomCard.Title>{title}</CustomCard.Title>
        <CustomCard.Text>{text}</CustomCard.Text>
      </CustomCard.Body>
    </CustomCard>
  );
};

export default Card;
