import { useState } from 'react';
import { Box, Button, Input, VStack, Text } from '@chakra-ui/react';
import { Card } from '@/components/ui/card';
import { InputGroup } from '@/components/ui/input-group';
import { useAuth } from '@/contexts/AuthContext';

const SignIn = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(username, password);
    } catch (err) {
      setError('Login failed. Please check your credentials and try again.');
    }
  };

  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      height="100vh"
    >
      <Card
        title="Sign In"
        content={
          <form onSubmit={handleSubmit}>
            <VStack gap={4} width="100%">
              <InputGroup width="100%">
                <Input
                  placeholder="Username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  width="100%"
                />
              </InputGroup>
              <InputGroup width="100%">
                <Input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  width="100%"
                />
              </InputGroup>
              {error && <Text color="red.500">{error}</Text>}
              <Button type="submit" colorScheme="blue" width="full">
                Sign In
              </Button>
            </VStack>
          </form>
        }
        footer={<Text>Don't have an account? Sign Up</Text>}
      />
    </Box>
  );
};

export default SignIn;
