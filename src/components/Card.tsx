import React from 'react';
import Button from 'react-bootstrap/Button';
import { Card as CustomCard } from 'react-bootstrap';

interface CardProps {
  title: string;
  text: string;
  imgSrc: string;
  buttonText: string;
  buttonOnClick: () => void;
}

const Card: React.FC<CardProps> = ({
  title,
  text,
  imgSrc,
  buttonText,
  buttonOnClick,
}) => {
  return (
    <CustomCard style={{ width: '18rem' }}>
      <CustomCard.Img variant="top" src={imgSrc} />
      <CustomCard.Body>
        <CustomCard.Title>{title}</CustomCard.Title>
        <CustomCard.Text>{text}</CustomCard.Text>
        <Button variant="primary" onClick={buttonOnClick}>
          {buttonText}
        </Button>
      </CustomCard.Body>
    </CustomCard>
  );
};

export default Card;
