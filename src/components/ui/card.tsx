import { ReactNode } from 'react';
import { Card as ChakraCard } from '@chakra-ui/react';

interface CardProps {
  title: string;
  content: string;
  footer: ReactNode;
}

// Card component with title, content, and footer
export const Card = ({ title, content, footer }: CardProps) => {
  return (
    <ChakraCard.Root width="320px">
      <ChakraCard.Body padding={5} gap={2}>
        <ChakraCard.Title>{title}</ChakraCard.Title>
        <ChakraCard.Description>{content}</ChakraCard.Description>
      </ChakraCard.Body>
      <ChakraCard.Footer justifyContent="flex-end">{footer}</ChakraCard.Footer>
    </ChakraCard.Root>
  );
};
